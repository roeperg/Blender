
from greg_blender import *
import bpy
import random
import pathlib
import os
import math
import types

cwd = os. getcwd()
from inspect import getmembers, isfunction
from mathutils import Vector

"""
obj = bpy.context.object
object_details = bounds(obj)

a = object_details.z.max
b = object_details.z.min
c = object_details.z.distance

print(a, b, c)

"""

# LAMBDA function to convert inches to Blender/Sweet Home 3D
to_sh3d_dim = (lambda s: s*2.54)

C = bpy.context

output_blend =  pathlib.PurePath(__file__).stem

base_cabinet_material = define_material_hsv ("base_cabinet_material",  .001, .077, .078,1.0)
cabinet_door_material =  define_material_hsv ("cabinet_door_material", .226, .300, .220,1.0)

###############################################################################################
###############################################################################################
def to_sh3d_dim(invalue):
	# function to convert inches to millimeter equivalent of Blender/Sweet Home 3D
	output = []
	for foo in invalue:
		output.append(foo*2.54)
	return output

###############################################################################################
###############################################################################################
def to_inches(invalue):
	# function to convert Blender/Sweet Home 3D to inches
	output = []
	for foo in invalue:
		output.append(foo/2.54)
	return output

###############################################################################################
###############################################################################################
def mirror(original, factors):
	return (original[0]*factors[0],original[1]*factors[1],original[2]*factors[2])

###############################################################################################
###############################################################################################
def set_door(in_object_name, DIRECTION="left"):
	print(in_object_name)
	dimensions = get_object_dimensions(in_object_name)
	print("\n\n\nDimensions")
	for foo in dimensions:
		print(foo)

	location = get_object_location(in_object_name)
	print("\n\n\nLocation")
	for foo in location:
		print(foo)
	print("\n\n\n")

	bpy.ops.object.select_all(action="DESELECT")
	obj = bpy.data.objects[in_object_name]

	if DIRECTION == "right":
		print("location x = ", location[0])
		new_x = location[0] + (dimensions[0]/2)
		print("new origin = ", (new_x, 0,0))
		set_3d_cursor(LOCATION=(new_x, 0,0))
		set_object_center(in_object_name, "ORIGIN_CURSOR")
		rotate_object(in_object_name, (0,0,90))
		set_3d_cursor()

	return (new_x, 0,0)

###############################################################################################
###############################################################################################
def set_3d_cursor(LOCATION=(0,0,0)):
	saved_location = C.scene.cursor.location.copy()
	C.scene.cursor.location = LOCATION
	print(saved_location)
	return saved_location

###############################################################################################
###############################################################################################
def build_24_inch_cabinet(in_object_name, LOCATION = (0,0,0), ROTATION = (0,0,0), OPEN_DOORS = False):
	delete_all_objects()
	dim_lower_cabinet_cutout     =  [55.88, 60.96, 121.92]
	dim_lower_cabinet_door_base  =  [29.845, 1.27, 124.46]
	dim_cabinet_base             =  [60.96, 60.96, 243.84]
	dim_upper_cabinet_cutout     =  [55.88, 60.96, 101.6]
	dim_upper_cabinet_door_base  =  [29.845, 1.27, 104.14]

	loc_lower_cabinet_cutout     = [0, -4, 72]
	loc_lower_cabinet_door_base  = [15.5,-31.5,72]
	loc_cabinet_base             = [0, 0, 121.92]
	loc_upper_cabinet_cutout     = [0, -4, 188]
	loc_upper_cabinet_door_base  = [15.5,-31.5,188]

	build_cube(in_object_name,        loc_cabinet_base, dim_cabinet_base)

	build_cube("lower_right_door", loc_lower_cabinet_door_base, dim_lower_cabinet_door_base)
	set_material('lower_right_door', cabinet_door_material)
	loc_mirror_door = mirror(loc_lower_cabinet_door_base, (-1,1,1))
	build_cube("lower_left_door",       loc_mirror_door, dim_lower_cabinet_door_base)
	set_material('lower_left_door', cabinet_door_material)
	build_cube("upper_right_door",        loc_upper_cabinet_door_base, dim_upper_cabinet_door_base)
	set_material('upper_right_door', base_cabinet_material)
	loc_mirror_door = mirror(loc_upper_cabinet_door_base, (-1,1,1))
	build_cube("upper_left_door",       loc_mirror_door, dim_upper_cabinet_door_base)
	set_material('upper_left_door', base_cabinet_material)

	if OPEN_DOORS:
		object_details  = set_door("lower_right_door", DIRECTION="right")
		print("lower right door has been set, ", object_details)
		if loc_lower_cabinet_door_base[0] > 0:
			loc_lower_cabinet_door_base[0] += dim_lower_cabinet_door_base[0]/2
		else:
			loc_lower_cabinet_door_base[0] -= dim_lower_cabinet_door_base[0]/2
	move_object("lower_right_door", loc_lower_cabinet_door_base)

	build_cube("temp_upper_cut",        loc_upper_cabinet_cutout, dim_upper_cabinet_cutout)
	build_cube("temp_lower_cut",        loc_lower_cabinet_cutout, dim_lower_cabinet_cutout)

	if False:
		move_object("upper_right_door", (20.75,-42,188))
		rotate_object("upper_right_door", (0,0,45))

	boolean_difference(in_object_name, "temp_upper_cut")
	remove_object("temp_upper_cut")
	boolean_difference(in_object_name, "temp_lower_cut")
	remove_object("temp_lower_cut")
	#join_objects_by_name( [ "lower_left_door", "lower_right_door", "upper_left_door", "upper_right_door", in_object_name])

###############################################################################################
###############################################################################################

dim_cabinet_base             =  [60.96, 60.96, 243.84]

print(dim_cabinet_base, to_inches(dim_cabinet_base))

build_24_inch_cabinet("my_cab",LOCATION = (0,0,36), ROTATION = (0,0,0), OPEN_DOORS = True)

set_material('my_cab', base_cabinet_material)

#set_3d_cursor(LOCATION=(30,-31.5,188))

print ("\n\n\n%s/%s.blend\n\n\n" %(cwd,output_blend))
bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))

#remove_object("cutout")

