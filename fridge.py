
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
def text_cut(inbase, inname,intext,inlocation,bevel=.04, SCALE=(5,5,5)):
	add_text(inname,intext,inlocation,bevel,SCALE)
	boolean_difference(inbase, inname, SOLVER='FAST')
	remove_object(inname)

###############################################################################################
###############################################################################################

delete_all_objects()
join_list = ["Text_0"]  # ["upper_curve", "lower_curve"]

height = SAE2Metric(70)/10
width  = SAE2Metric(36)/10
depth  = SAE2Metric(30)/10

height = 70
width  = 36
depth  = 30

if True:
	build_cube("fridge",        (0,0,height/2), (width,depth,height))

	# join_objects_by_name(["upper_curve", "lower_curve", "compass"])

	# boolean_difference("fridge", "upper_cut")
	# remove_object("upper_cut")
	# boolean_difference("fridge", "lower_cut")
	# remove_object("lower_cut")
print ("\n\n\n%s/%s.blend\n\n\n" %(cwd,output_blend))
bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))

#remove_object("cutout")

