
from greg_blender import *
import bpy
import random
import pathlib
import os
import math
import types
from mathutils import Vector

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
C = bpy.context

output_blend =  pathlib.PurePath(__file__).stem
#to_sh3d_dim = (lambda s: s*2.54)
to_sh3d_dim = (lambda s: s*1.0)
###############################################################################################
###############################################################################################
def build_base(in_name):
	print("build_base ", in_name)

	verts = []    # x,y,z
	edges = []    # p1,p2
	faces = []    # p1 - pN

	verts.append([0.0,0.0,0.0,])                         # index 0
	verts.append([to_sh3d_dim(30),0.0,0.0,])             # index 1
	verts.append([0.0,to_sh3d_dim(29),0.0,])             # index 2

	#for foo in range(len(verts)):
	#	add_text("t%d" %foo, "%d" %foo, verts[foo])

	edges.append([0, 1])
	edges.append([1, 2])
	edges.append([0, 2])

	name = in_name
	mesh = bpy.data.meshes.new(name)
	obj = bpy.data.objects.new(name, mesh)
	print("collection length = ", len(bpy.data.collections))
	col = bpy.data.collections[0]
	print(col)
	col.objects.link(obj)
	bpy.context.view_layer.objects.active = obj
	mesh.from_pydata(verts, edges, faces)
	bpy.ops.object.editmode_toggle()
	bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False
,  "use_dissolve_ortho_edges":False
,  "mirror":False}
,  TRANSFORM_OT_translate={"value":(0, 0, to_sh3d_dim(96.0))
,  "orient_axis_ortho":'X'
,  "orient_type":'GLOBAL'
,  "orient_matrix":((1, 0, 0)
,  (0, 1, 0)
,  (0, 0, 1))
,  "orient_matrix_type":'GLOBAL'
,  "constraint_axis":(False
,  False
,  True)
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
	bpy.ops.object.editmode_toggle()
	bpy.ops.object.modifier_add(type='SOLIDIFY')
	bpy.context.object.modifiers["Solidify"].thickness = to_sh3d_dim(-.5)
	bpy.ops.object.modifier_apply(modifier="Solidify")

###############################################################################################
###############################################################################################

delete_all_objects()

build_base("my_base")

print ("\n\n\n%s/%s.blend\n\n\n" %(cwd,output_blend))
bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))
#bpy.ops.export_mesh.stl(filepath="%s/%s.stl" %(cwd,output_blend))
bpy.ops.export_scene.obj(filepath="%s/%s.obj" %(cwd,output_blend))
#remove_object("cutout")

