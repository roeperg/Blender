
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

if True:
	build_cylinder("compass", ( 0, 0, 0), ( 40,160, 2), VERTICES=256)
	#build_cube("compass",        (0,0,0), (16,140,2))
	move_object("compass", (0,70,0))
	#build_cylinder("upper_curve", ( 0, 140, 0), (16,16, 2), VERTICES=128)
	#build_cylinder("lower_curve", ( 0,   0, 0), (16,16, 2), VERTICES=128)
	#join_objects_by_name(["upper_curve", "lower_curve", "compass"])

	build_cylinder("cutout", ( 0, 0, 0), (3, 3, 100), VERTICES=128)
	build_cylinder("cutout1", ( 0, 0, 0), (2, 2, 100), VERTICES=128)
	build_cylinder("cutout2", ( 0, 0, 0), (4, 4, 100), VERTICES=128)

	boolean_difference("compass", "cutout2")
	add_text("Text_0", "CNTR", ( -5,-6,1), bevel=.04, SCALE=(3,3,3))

if True:
	for foo in range(1,15):
		point = get_y_from_x(foo*10,5)

		move_object("cutout1", (-1*point[0],point[1],0))
		boolean_difference("compass", "cutout1", SOLVER='FAST')
		move_object("cutout2", (point[0], point[1],0))
		boolean_difference("compass", "cutout2", SOLVER='FAST')
		move_object("cutout", (0,10*foo,0))
		boolean_difference("compass", "cutout", SOLVER='FAST')
		join_list.append("Text_%d" %foo)
		add_text("Text_%d" %foo, "%d0mm" %foo, ( -4, (foo*10)-6,1), bevel=.04, SCALE=(3,3,3))

join_list.append("compass")
print(join_list)
join_objects_by_name(join_list)

move_object("cutout", (0,10*foo,0))
boolean_difference("compass", "cutout", SOLVER='FAST')

print("objects joined")
remove_object("cutout")
remove_object("cutout1")
remove_object("cutout2")

print ("\n\n\n%s/%s.blend\n\n\n" %(cwd,output_blend))
bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))

#remove_object("cutout")

"""
import addons
	preferences   import =export: import images a planes

	add plane  90% along y access
	add image as plane
	choose picture
	align to plane and overlap it
	size image
	CAN JUST TRIM IMAGE in PLACE WHICH LEAVES IT TEXTURED.  :)
"""

"""
location 12,9,0
scale 2.5
text
"""

