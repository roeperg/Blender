
from greg_blender import *
from math import *
from mathutils import Vector
import bpy
import math
import mathutils
import numpy
import os
import pathlib
import random
import sys
import types

cwd = os. getcwd()

C = bpy.context

output_blend =  pathlib.PurePath(__file__).stem

#delete_all_objects()

object_1 = "oven.obj"
###############################################################################################
###############################################################################################

if True:
	print("C:\\Users\\roepe\\OneDrive\\Desktop\\Imaging and Music\\Blender\\objects\\%s" %object_1)
	bpy.ops.wm.obj_import(filepath="C:\\Users\\roepe\\OneDrive\\Desktop\\Imaging and Music\\Blender\\objects\\%s" %object_1, directory="C:\\Users\\roepe\\OneDrive\\Desktop\\Imaging and Music\\Blender\\objects\\", files=[{"name":"%s" %object_1, "name":"%s" %object_1}])
	bpy.context.active_object.name = "Oven1"
	bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')
	bpy.ops.wm.obj_import(filepath="C:\\Users\\roepe\\OneDrive\\Desktop\\Imaging and Music\\Blender\\objects\\%s" %object_1, directory="C:\\Users\\roepe\\OneDrive\\Desktop\\Imaging and Music\\Blender\\objects\\", files=[{"name":"%s" %object_1, "name":"%s" %object_1}])
	bpy.context.active_object.name = "Oven2"
	bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')
	move_object("Oven1", (0,0,0))
	move_object("Oven2", (0,0,50))

if 1:
	print ("\n\n\n%s/%s.blend\n\n\n" %(cwd,output_blend))
	bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))
	#bpy.ops.export_mesh.stl(filepath="%s/%s.stl" %(cwd,output_blend))
	#bpy.ops.export_scene.obj(filepath="%s/%s.obj" %(cwd,output_blend))

#BMESH?

