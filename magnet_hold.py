
from greg_blender import *
import bpy
import random
import pathlib
import os
import math
cwd = os. getcwd()

C = bpy.context
join_list = []

output_blend =  pathlib.PurePath(__file__).stem

delete_all_objects()

inner_d = 12
outer_d = 15
height = 4
hole = 4

if True:
	build_cube("base",        (0,0, 0), (20,20,20))
	cutout_cube("base", (5,5, 5), (20,20,20), ROTATION=(0,4,15) , SOLVER='EXACT')
	build_sphere("sp", (0,0,0), (10,8,4), SEGMENTS=60, RINGS=40 )
	cutout_sphere("sp", (0,0,0), (5,4,8), SOLVER='EXACT' )

if False:
	build_cylinder("shaft", (0,0,0), (outer_d,outer_d,height), VERTICES=128, ROTATION=(0,0,0))
	cutout_cylinder("shaft", (0,0,1), (inner_d,inner_d,height), VERTICES=128, ROTATION=(0,0,0))
	cutout_cylinder("shaft", (0,0,0), (8,5,12), VERTICES=128, ROTATION=(0,0,0))

bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))

