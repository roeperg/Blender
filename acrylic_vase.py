
from greg_blender import *
import bpy
import random
import pathlib
import os

cwd = os. getcwd()

C = bpy.context

output_blend =	pathlib.PurePath(__file__).stem
join_list = ["tube", "flap", "deflector"]

if True:
	bpy.ops.object.select_all(action="DESELECT")

	objectToSelect = bpy.data.objects['Base_Pot']
	objectToSelect.select_set(True)

	bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}
		, TRANSFORM_OT_translate={"value":(0, 0, 0), "orient_axis_ortho":'X', "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1))
		, "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, False), "mirror":False, "use_proportional_edit":False
		, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False
		, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False
		, "snap_target":'CLOSEST', "use_snap_self":False, "use_snap_edit":False, "use_snap_nonedit":False, "use_snap_selectable":False
		, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False
		, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False
		, "use_automerge_and_split":False})

	bpy.ops.object.select_all(action="DESELECT")
	objectToSelect = bpy.data.objects['Base_Pot.001']

	objectToSelect.select_set(True)
	objectToSelect.name = "Base_Pot_Liner"
	print(objectToSelect.location)
	objectToSelect.scale.x = .99 * objectToSelect.scale.x
	objectToSelect.scale.y = .99 * objectToSelect.scale.y

	boolean_difference('Base_Pot', 'cut1' )

	print(objectToSelect.scale.x, objectToSelect.scale.y, objectToSelect.scale.z)

else:
	print("Option 2")
	copy_object ('Base_Pot', 'Base_Pot_Liner', data=True, actions=True, collection=None)

print ("\n\n\n%s/%s.blend\n\n\n" %(cwd, output_blend))
bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd, output_blend))

#bpy.ops.export_mesh.stl(filepath="%s/%s.stl" %(cwd, output_blend))

