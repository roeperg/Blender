
from greg_blender import *
import bpy
import random
import pathlib
import os

cwd = os. getcwd()

C = bpy.context

cntr2cntr = 33.5
side2side = cntr2cntr - 7

cntr2cntr *= .5

output_blend =  pathlib.PurePath(__file__).stem

delete_all_objects()
join_list = []

if True:
	build_cylinder("tube_1", ( cntr2cntr, 0, 0), (8, 8, 5), VERTICES=128)
	build_cylinder("cutout_1", ( cntr2cntr, 0, 0), (6, 6, 100), VERTICES=128)
	boolean_difference("tube_1", "cutout_1")
	remove_object("cutout_1")

	build_cylinder("tube_2", ( -cntr2cntr, 0, 0), (8, 8, 5), VERTICES=128)
	build_cylinder("cutout_2", ( -cntr2cntr, 0, 0), (6, 6, 100), VERTICES=128)
	boolean_difference("tube_2", "cutout_2")
	remove_object("cutout_2")

	build_cube("plate", (0,7.5,0), (cntr2cntr*2,4,5))
	build_cube("cutout_4", (0,7.5,0), (30,2,8))
	boolean_difference("plate", "cutout_4")
	remove_object("cutout_4")

	newx = 75
	newy = 30*.95
	newz = 2*.95

	build_cube("label", (0,28,-1.55), (newx,newy,newz))

	build_cube("cutout_3", (0,-5.5,0), (60,8,8))
	boolean_difference("tube_1", "cutout_3")
	boolean_difference("tube_2", "cutout_3")
	remove_object("cutout_3")

	build_cube("spacer_1", (-cntr2cntr,6.5,0), (1,6,5))
	build_cube("spacer_2", ( cntr2cntr,6.5,0), (1,6,5))

	join_objects_by_name(["tube_1", "tube_2", "spacer_1", "spacer_2", "plate"])

if True:
	bpy.ops.object.select_all(action="DESELECT")
	objectToSelect = bpy.data.objects["plate"]
	objectToSelect.select_set(True)

	bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False
			,  "mode":'TRANSLATION'}
			,  TRANSFORM_OT_translate={"value":(-0, -16, -0)
			,  "orient_axis_ortho":'X'
			,  "orient_type":'GLOBAL'
			,  "orient_matrix":((1, 0, 0)
			,  (0, 1, 0)
			,  (0, 0, 1))
			,  "orient_matrix_type":'GLOBAL'
			,  "constraint_axis":(False
			,  True
			,  False)
			,  "mirror":False
			,  "use_proportional_edit":False
			,  "proportional_edit_falloff":'SMOOTH'
			,  "proportional_size":1, "use_proportional_connected":False
			,  "use_proportional_projected":False
			,  "snap":False
			,  "snap_elements":{'INCREMENT'}
			,  "use_snap_project":False
			,  "snap_target":'CLOSEST'
			,  "use_snap_self":False
			,  "use_snap_edit":False
			,  "use_snap_nonedit":False
			,  "use_snap_selectable":False
			,  "snap_point":(0, 0, 0)
			,  "snap_align":False
			,  "snap_normal":(0, 0, 0)
			,  "gpencil_strokes":False
			,  "cursor_transform":False
			,  "texture_space":False
			,  "remove_on_cancel":False
			,  "view2d_edge_pan":False
			,  "release_confirm":False
			,  "use_accurate":False
			,  "use_automerge_and_split":False})
	bpy.ops.object.select_all(action="DESELECT")

print ("\n\n\n%s/%s.blend\n\n\n" %(cwd,output_blend))
bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))
bpy.ops.export_mesh.stl(filepath="%s/%s.stl" %(cwd,output_blend))

