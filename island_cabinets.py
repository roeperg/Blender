
from greg_cabinet_stuff import *
import random
import pathlib
import os
import math
import types

cwd = os. getcwd()
from inspect import getmembers, isfunction
from mathutils import Vector

C = bpy.context

output_blend =  pathlib.PurePath(__file__).stem

###############################################################################################
###############################################################################################

if __name__ == "__main__":

	delete_all_objects()
	build_3_drawer_cabinet ("cabinet_1", 18, OPEN_DRAWER=0, JOIN_OBJS = False)
	build_3_drawer_cabinet ("cabinet_2", 24, OPEN_DRAWER=3, JOIN_OBJS = False)
	build_3_drawer_cabinet ("cabinet_3", 24, OPEN_DRAWER=0, JOIN_OBJS = False)

	move_object("cabinet_2", to_sh3d_dim((21,0,17.5)))
	move_object("cabinet_3", to_sh3d_dim((-21,0,17.5)))
	#join_objects_by_name(["cabinet_3", "cabinet_2", "cabinet_1"])
	print ("\n\n\n%s/%s.blend\n\n\n" %(cwd,output_blend))
	bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))
	bpy.ops.export_scene.obj(filepath="%s/%s.obj" %(cwd,output_blend))

