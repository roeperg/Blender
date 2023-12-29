
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

delete_all_objects()
join_list = ["Text_0"]  # ["upper_curve", "lower_curve"]

dim_lower_cabinet_cutout  =  (71.12, 60.96, 121.92)
dim_lower_cabinet_door_base  =  (37.465, 1.27, 124.46)
dim_cabinet_base  =  (76.2, 60.96, 243.84)
dim_upper_cabinet_cutout  =  (71.12, 60.96, 101.6)
dim_upper_cabinet_door_base  =  (37.465, 1.27, 104.14)

loc_lower_cabinet_cutout    = (0, -4, 72)
loc_lower_cabinet_door_base    = (18.7325,-31.5,72)
loc_cabinet_base    = (0, 0, 121.92)
loc_upper_cabinet_cutout    = (0, -4, 188)
loc_upper_cabinet_door_base    = (18.7325,-31.5,188)

if True:
	build_cube("cabinet",        loc_cabinet_base, dim_cabinet_base)
	build_cube("upper_cut",        loc_upper_cabinet_cutout, dim_upper_cabinet_cutout)
	build_cube("lower_cut",        loc_lower_cabinet_cutout, dim_lower_cabinet_cutout)

	build_cube("lower_door_right",        loc_lower_cabinet_door_base, dim_lower_cabinet_door_base)
	if True:
		move_object("lower_door_right", (37.2,-50,72))
		rotate_object("lower_door_right", (0,0,-90))
	loc_mirror_door = mirror(loc_lower_cabinet_door_base, (-1,1,1))
	build_cube("lower_door_left",       loc_mirror_door, dim_lower_cabinet_door_base)

	build_cube("upper_door_right",        loc_upper_cabinet_door_base, dim_upper_cabinet_door_base)
	if True:
		move_object("upper_door_right", (24.6,-45.2,188))
		rotate_object("upper_door_right", (0,0,47))
	loc_mirror_door = mirror(loc_upper_cabinet_door_base, (-1,1,1))
	build_cube("upper_door_left",       loc_mirror_door, dim_upper_cabinet_door_base)

	#join_objects_by_name(["upper_curve", "lower_curve", "compass"])

	boolean_difference("cabinet", "upper_cut")
	remove_object("upper_cut")
	boolean_difference("cabinet", "lower_cut")
	remove_object("lower_cut")


join_objects_by_name( [ "lower_door_left", "lower_door_right", "upper_door_left", "upper_door_right", "cabinet"])

print ("\n\n\n%s/%s.blend\n\n\n" %(cwd,output_blend))
bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))

#remove_object("cutout")

