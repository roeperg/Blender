
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
def text_cut(inbase, inname,intext,inlocation,bevel=.04, SCALE=(5,5,5)):
	add_text(inname,intext,inlocation,bevel,SCALE)
	boolean_difference(inbase, inname, SOLVER='FAST')
	remove_object(inname)

###############################################################################################
###############################################################################################

delete_all_objects()
join_list =  []   #  ["upper_curve", "T", "base"]

tscale      =   0.5

width       =  40 * tscale
length      =  30 * tscale
text_offset = -13 * tscale
text_final  =  17 * tscale
text_scale  =   6 * tscale
circle_cir  =  10 * tscale
depth       =   2

if True:
	build_cube("base",        (0,0,0), (width,length,depth))
	build_cylinder("upper_curve", ( width/2,0, 0), (circle_cir,circle_cir, 2*depth), VERTICES=128)

	boolean_difference("base", "upper_curve")
	move_object("upper_curve", ( -(width/2),0, 0))
	scale_object("upper_curve", (circle_cir,circle_cir,depth))

	add_text("T", "T T", ( 0, 0,0), bevel=0, SCALE=(text_scale,text_scale,2*text_scale))
	set_object_center("T")
	move_object("T", ( 0, text_offset, 0))

	boolean_difference("base", "T", SOLVER='FAST')
	move_object("T", (0 , text_final, 0))
	scale_object("T", (text_scale,text_scale,depth))

if len(join_list):
	print(join_list)
	join_objects_by_name(join_list)

print ("\n\n\n%s/%s.blend\n\n\n" %(cwd,output_blend))
bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))

#remove_object("cutout")

bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')

