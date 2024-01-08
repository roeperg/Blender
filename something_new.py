
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
def mirror(original, factors):
	return (original[0]*factors[0], original[1]*factors[1], original[2]*factors[2])

###############################################################################################
###############################################################################################
def add_text(in_name, in_text, in_location, bevel=0.002, SCALE=(5, 5, 5)):

	in_text = in_text.strip()
	bpy.data.fonts.load(r"C:\Windows\Fonts\PLAYBILL.TTF")
	#bpy.ops.font.open(filepath=r"C:\Windows\Fonts\ITCKRIST.TTF")
	bpy.ops.object.text_add(location=in_location)
	ob=bpy.context.object
	sd=	bpy.context

	ob.data.body = str(in_text)
	ob.data.space_character = 1.4

	ob.name = in_name
	ob.data.extrude = .25
	ob.data.bevel_depth = bevel
	bpy.ops.object.convert(target='MESH')

	scale_object(ob.name, SCALE)

###############################################################################################
###############################################################################################
def set_door(in_object_name, DIRECTION="left"):
	print(in_object_name)
	dimensions = get_object_dimensions(in_object_name)
	print("\n\n\nDimensions")
	for foo in dimensions:
		print(foo)

	location = get_object_location(in_object_name)
	print("\n\n\nLocation")
	for foo in location:
		print(foo)
	print("\n\n\n")

	bpy.ops.object.select_all(action="DESELECT")
	obj = bpy.data.objects[in_object_name]

	if DIRECTION == "right":
		print("location x = ", location[0])
		new_x = location[0] + (dimensions[0]/2)
		print("new origin = ", (new_x, 0, 0))
		set_3d_cursor(LOCATION=(new_x, 0, 0))
		set_object_center(in_object_name, "ORIGIN_CURSOR")
		rotate_object(in_object_name, (0, 0, 90))
		set_3d_cursor()

###############################################################################################
###############################################################################################
def set_3d_cursor(LOCATION=(0, 0, 0)):
	saved_location = C.scene.cursor.location.copy()
	C.scene.cursor.location = LOCATION
	print(saved_location)
	return saved_location

###############################################################################################
###############################################################################################
def build_base(in_name):
	print("build_base ", in_name)

	verts = []    # x, y, z
	edges = []    # p1, p2
	faces = []    # p1 - pN

	verts.append([0.0, 0.0, 0.0, ])                         # index 0
	verts.append([to_sh3d_dim(30), 0.0, 0.0, ])             # index 1
	verts.append([0.0, to_sh3d_dim(29), 0.0, ])             # index 2

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
, "use_dissolve_ortho_edges":False
, "mirror":False}
, TRANSFORM_OT_translate={"value":(0, 0, to_sh3d_dim(96.0))
, "orient_axis_ortho":'X'
, "orient_type":'GLOBAL'
, "orient_matrix":((1, 0, 0)
, (0, 1, 0)
, (0, 0, 1))
, "orient_matrix_type":'GLOBAL'
, "constraint_axis":(False
, False
, True)
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
	bpy.ops.object.editmode_toggle()
	bpy.ops.object.modifier_add(type='SOLIDIFY')
	bpy.context.object.modifiers["Solidify"].thickness = to_sh3d_dim(-.5)
	bpy.ops.object.modifier_apply(modifier="Solidify")

###############################################################################################
###############################################################################################
def build_shelf(in_name):
	print("build_shelf ", in_name)

	verts = []    # x, y, z
	edges = []    # p1, p2
	faces = []    # p1 - pN

	verts.append([0.0, 0.0, 0.0, ])                         # index 0
	verts.append([to_sh3d_dim(30), 0.0, 0.0])            # index 1
	verts.append([to_sh3d_dim(6.6), to_sh3d_dim(22), 0.0]) # index 2
	verts.append([0.0, to_sh3d_dim(22), 0.0])              # index 3

	#for foo in range(len(verts)):
	#	add_text("t%d" %foo, "%d" %foo, verts[foo])

	edges.append([0, 1])
	edges.append([1, 2])
	edges.append([2, 3])
	edges.append([0, 3])

	faces.append([0, 1, 2, 3])
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
, "use_dissolve_ortho_edges":False
, "mirror":False}
, TRANSFORM_OT_translate={"value":(0, 0, to_sh3d_dim(.5))
, "orient_axis_ortho":'X'
, "orient_type":'GLOBAL'
, "orient_matrix":((1, 0, 0)
, (0, 1, 0)
, (0, 0, 1))
, "orient_matrix_type":'GLOBAL'
, "constraint_axis":(False
, False
, True)
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
	bpy.ops.object.editmode_toggle()
	bpy.ops.object.modifier_add(type='SOLIDIFY')
	bpy.context.object.modifiers["Solidify"].thickness = to_sh3d_dim(.5)
	bpy.ops.object.modifier_apply(modifier="Solidify")

###############################################################################################
###############################################################################################

delete_all_objects()

build_base("my_base")

build_cube("upright"
	, (to_sh3d_dim(3.75), to_sh3d_dim(22.0), to_sh3d_dim(48.0))     # position
	, (to_sh3d_dim(6.6), to_sh3d_dim(0.5), to_sh3d_dim(96.0))      # size
)

build_cube("cut"
	, (to_sh3d_dim(18.9), to_sh3d_dim(10.8), to_sh3d_dim(50.0))     # position
	, (to_sh3d_dim(27), to_sh3d_dim(1.0), to_sh3d_dim(88.0))      # size
  , ROTATION = (0.0, 0.0, -44.9))

boolean_difference("my_base", "cut", SOLVER='FAST')
remove_object("cut")
build_shelf("shelf_1")
move_object("shelf_1", (40, 10, 6))
#base_cabinet_material = define_material_hsv ("base_cabinet_material", .226, .300, .220, 1.0)
#cabinet_door_material =  define_material_hsv ("cabinet_door_material", 0.02, 0.04, 0.6, 1.0)

#MATERIALset_material('my_cab', base_cabinet_material)

print ("\n\n\n%s/%s.blend\n\n\n" %(cwd, output_blend))
bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd, output_blend))
#bpy.ops.export_mesh.stl(filepath="%s/%s.stl" %(cwd, output_blend))
bpy.ops.export_scene.obj(filepath="%s/%s.obj" %(cwd, output_blend))
#remove_object("cutout")

