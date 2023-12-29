
from greg_cabinet_stuff import *
import random
import pathlib
import os
import math
import types

"""

to_sh3d_dim translates x, y, z to Sweet Home 3D dimensions

"""

cwd = os. getcwd()
from inspect import getmembers, isfunction
from mathutils import Vector

output_blend =  pathlib.PurePath(__file__).stem

###############################################################################################
###############################################################################################

if __name__ == "__main__":

	delete_all_objects()
	build_glass_cabinet("my_cabinet", 36,12,42)
	build_glass_cabinet("my_cabinet2", 36,12,36)
	move_object_relative("my_cabinet2", to_sh3d_dim([40,0,0]))

	print ("\n\n\n%s/%s.blend\n\n\n" %(cwd,output_blend))
	bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))
	bpy.ops.export_scene.obj(filepath="%s/%s.obj" %(cwd,output_blend))

