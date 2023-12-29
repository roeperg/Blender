
from greg_blender import *
import bpy
import random
import pathlib
import os
import math
cwd = os. getcwd()

C = bpy.context

output_blend =  pathlib.PurePath(__file__).stem

###############################################################################################
###############################################################################################
def get_y_from_x(radius, x):
	l2 = radius*radius
	x2 = x * x
	return (x,math.sqrt(l2-x2))

###############################################################################################
###############################################################################################
def add_text(in_name, in_text, in_location, bevel=0.002, SCALE=(5,5,5)):

	in_text = in_text.strip()
	bpy.data.fonts.load(r"C:\Windows\Fonts\PLAYBILL.TTF")
	#bpy.ops.font.open(filepath=r"C:\Windows\Fonts\ITCKRIST.TTF")
	bpy.ops.object.text_add(location=in_location)
	ob=bpy.context.object
	sd=	bpy.context

	ob.data.body = str(in_text)
	ob.data.space_character = 1.4

	ob.name = in_name
	ob.data.extrude = .25
	ob.data.bevel_depth = bevel
	bpy.ops.object.convert(target='MESH')

	scale_object(ob.name, SCALE)

###############################################################################################
###############################################################################################
def mirror(original, factors):
	return (original[0]*factors[0],original[1]*factors[1],original[2]*factors[2])

###############################################################################################
###############################################################################################
def text_cut(inbase, inname,intext,inlocation,bevel=.04, SCALE=(5,5,5)):
	add_text(inname,intext,inlocation,bevel,SCALE)
	boolean_difference(inbase, inname, SOLVER='FAST')
	remove_object(inname)

###############################################################################################
###############################################################################################
to_sh3d_dim = (lambda s: s*2.54)

delete_all_objects()
join_list = ["Text_0"]  # ["upper_curve", "lower_curve"]

dim_cabinet_base  =  (to_sh3d_dim(33), 60.96, 243.84)
loc_cabinet_base = (0,0,0)
if True:
	build_cube("cabinet",        loc_cabinet_base, dim_cabinet_base)

print ("\n\n\n%s/%s.blend\n\n\n" %(cwd,output_blend))
bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))
bpy.ops.export_scene.obj(filepath="%s/%s.obj" %(cwd,output_blend))

#remove_object("cutout")

