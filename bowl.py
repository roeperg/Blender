
from greg_blender import *
import bpy
import random
import pathlib
import os

cwd = os. getcwd()

C = bpy.context

output_blend =  pathlib.PurePath(__file__).stem

delete_all_objects()
join_list = []

if True:
	build_cylinder("tube", ( 0, 0, 0), (8, 8, 2), VERTICES=6)
	rotate_object("tube",(0,0,30))

	#build_cube("section",(0,0,0),(15.24,6,5))
print ("\n\n\n%s/%s.blend\n\n\n" %(cwd,output_blend))
bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))

