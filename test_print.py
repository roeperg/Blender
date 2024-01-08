
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

thick = 12
half_thick = thick/2

if True:
	build_cube("base", (0, 0, 2), (16, 10, 4))
	build_cylinder("bevel_edge", (0, 0, 0), (4, 4, 16), VERTICES=128)
	rotate_object("bevel_edge", (0, 90, 0))
	move_object("bevel_edge", (0, 5, 2))
print ("\n\n\n%s/%s.blend\n\n\n" %(cwd, output_blend))
bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd, output_blend))
bpy.ops.export_mesh.stl(filepath="%s/%s.stl" %(cwd, output_blend))
#remove_object("cutout")

