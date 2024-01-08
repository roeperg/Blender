
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
#bpy.context.area.ui_type = 'INFO'
bpy.ops.mesh.primitive_circle_add(radius=1, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1), vertices=256)
bpy.ops.transform.resize(value=(4, 4, 4), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=False, use_snap_edit=False, use_snap_nonedit=False, use_snap_selectable=False)
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 2), "orient_axis_ortho":'X', "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":False, "use_snap_edit":False, "use_snap_nonedit":False, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
bpy.ops.object.editmode_toggle()
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False
, "use_dissolve_ortho_edges":False
, "mirror":False}
, TRANSFORM_OT_translate={"value":(0, 0, 5)
, "orient_axis_ortho":'X'
, "orient_type":'GLOBAL'
, "orient_matrix":((1, 0, 0)
, (0, 1, 0)
, (0, 0, 1))
, "orient_matrix_type":'GLOBAL'
, "constraint_axis":(False, False, True)
, "mirror":False
, "use_proportional_edit":False
, "proportional_edit_falloff":'SMOOTH'
, "proportional_size":1, "use_proportional_connected":False
, "use_proportional_projected":False
, "snap":False
, "snap_elements":{'INCREMENT'}
, "use_snap_project":False
, "snap_target":'CLOSEST'
, "use_snap_self":False
, "use_snap_edit":False
, "use_snap_nonedit":False
, "use_snap_selectable":False
, "snap_point":(0, 0, 0)
, "snap_align":False
, "snap_normal":(0, 0, 0)
, "gpencil_strokes":False
, "cursor_transform":False
, "texture_space":False
, "remove_on_cancel":False
, "view2d_edge_pan":False
, "release_confirm":False
, "use_accurate":False
, "use_automerge_and_split":False})
bpy.ops.transform.resize(value=(.95, .95, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=False, use_snap_edit=False, use_snap_nonedit=False, use_snap_selectable=False)
bpy.ops.object.editmode_toggle()
#bpy.context.space_data.context = 'MODIFIER'
bpy.ops.object.modifier_add(type='SOLIDIFY')
bpy.context.object.modifiers["Solidify"].thickness = 0.1
bpy.ops.object.modifier_apply(modifier="Solidify")

print ("\n\n\n%s/%s.blend\n\n\n" %(cwd, output_blend))
bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd, output_blend))

