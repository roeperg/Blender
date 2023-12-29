
from bpy import context, data, ops
from greg_blender import *
from math import cos, pi, sin, tan
from mathutils import Euler, Matrix, Quaternion
from mathutils import Vector
from random import TWOPI, randint, uniform
import bpy
import math
import os
import pathlib
import pdb
import random

cwd = os. getcwd()
output_blend =  pathlib.PurePath(__file__).stem

C = bpy.context
join_list = []

# delete_all_objects()

###############################################################################################
###############################################################################################
def simple_curve():
	#bpy.context.object.data.splines[0].resolution_u = 40

	output_blend =  pathlib.PurePath(__file__).stem

	ops.curve.primitive_bezier_curve_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
	#bpy.ops.curve.subdivide(number_cuts=2)
	bpy.ops.object.editmode_toggle()
	#bpy.ops.transform.rotate(value=-0.41778, orient_axis='Z', orient_type='VIEW', orient_matrix=((1, -0, 0), (-0, 1, -0), (0, -0, 1)), orient_matrix_type='VIEW', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=False, use_snap_edit=False, use_snap_nonedit=False, use_snap_selectable=False)
	#bpy.ops.transform.rotate(value=-1.00891, orient_axis='Z', orient_type='VIEW', orient_matrix=((1, -0, 0), (-0, 1, -0), (0, -0, 1)), orient_matrix_type='VIEW', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=False, use_snap_edit=False, use_snap_nonedit=False, use_snap_selectable=False)
	#bpy.ops.object.editmode_toggle()
	#bpy.context.space_data.context = 'DATA'
	bpy.context.object.data.bevel_depth = 0.1
	bpy.context.object.data.bevel_resolution = 40
	# Cache a reference to the curve.
	#bpy.ops.transform.resize(value=(2.565,2.565,2.565), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=False, use_snap_edit=False, use_snap_nonedit=False, use_snap_selectable=False)

	curve = context.active_object

	# Locate the array of bezier points.
	bez_points = curve.data.splines[0].bezier_points

	sz = len(bez_points)
	print(len(bez_points))
	for i in range(0, sz, 1):
		print(bez_points[i].co.x,bez_points[i].co.y,bez_points[i].co.z )
	bez_points[0].co = Vector((4,0,0))
	bez_points[1].co = Vector((-4,0,0))

	bez_points[0].handle_right = (2,-2, 0)
	bez_points[0].handle_left =  (2, 2, 0)
	bez_points[1].handle_right = (0, .2, 0)
	bez_points[1].handle_left =  (0,-.2, 0)

	rename_object('BezierCurve','simple_curve')
	#move_object('simple_curve', (25,-7,12))

###############################################################################################
###############################################################################################
def greggo():

	# print all objects
	for obj in bpy.data.objects:
	    print(obj.name)
	    if("Curve" in obj.name):
	        print("found")
	        bpy.data.scenes["Scene"].objects.unlink(obj)
	        bpy.data.objects.remove(obj)

	for cur in bpy.data.curves:
	    print(cur.name)
	    bpy.data.curves.remove(cur)

	# sample data
	coords = [(1,0,1), (2,0,0), (3,0,1)]

	# create the Curve Datablock
	curveData = bpy.data.curves.new('myCurve', type='CURVE')
	curveData.dimensions = '3D'
	curveData.resolution_u = 2

	# map coords to spline
	polyline = curveData.splines.new('POLY')
	polyline.points.add(len(coords)-1)
	for i, coord in enumerate(coords):
	    x,y,z = coord
	    polyline.points[i].co = (x, y, z, 1)

	# create Object
	curveOB = bpy.data.objects.new('myCurve', curveData)
	curveData.bevel_depth = 0.01

###############################################################################################
###############################################################################################
def complicated_circle():

	# Create a bezier circle and enter edit mode.
	ops.curve.primitive_bezier_circle_add(radius=1.0,
																				location=(0.0, 0.0, 0.0),
																				enter_editmode=True)
	# Subdivide the curve by a number of cuts, giving the
	# random vertex function more points to work with.
	ops.curve.subdivide(number_cuts=2)

	if False:
		# Randomize the vertices of the bezier circle.
		# offset [-inf .. inf], uniform [0.0 .. 1.0],
		# normal [0.0 .. 1.0], RNG seed [0 .. 10000].
		ops.transform.vertex_random(offset=1.0, uniform=0.1, normal=0.0, seed=0)

		# Scale the curve while in edit mode.
		ops.transform.resize(value=(2.0, 2.0, 3.0))

		# Return to object mode.
		ops.object.mode_set(mode='OBJECT')

	# Store a shortcut to the curve object's data.
	obj_data = context.active_object.data

	# Which parts of the curve to extrude ['HALF', 'FRONT', 'BACK', 'FULL'].
	obj_data.fill_mode = 'FULL'

	# Breadth of extrusion.
	obj_data.extrude = 0.125

	# Depth of extrusion.
	obj_data.bevel_depth = 0.125

	# Smoothness of the segments on the curve.
	obj_data.resolution_u = 20
	obj_data.render_resolution_u = 32
	bpy.ops.object.editmode_toggle()
	rename_object('BezierCircle','complex_circle')

	return

	# Create bevel control curve.
	ops.curve.primitive_bezier_circle_add(radius=0.25, enter_editmode=True)
	ops.curve.subdivide(number_cuts=4)
	ops.transform.vertex_random(offset=1.0, uniform=0.1, normal=1.0, seed=0)
	bevel_control = context.active_object
	bevel_control.data.name = bevel_control.name = 'Bevel Control'

	# Store a shortcut to the curve object's data.
	obj_data = context.active_object.data

	# Set the main curve's bevel control to the bevel control curve.
	obj_data.bevel_object = bevel_control
	ops.object.mode_set(mode='OBJECT')
	rename_object('Bevel Control','bevel_control')

	# Create taper control curve.
	ops.curve.primitive_bezier_curve_add(enter_editmode=True)
	ops.curve.subdivide(number_cuts=3)
	ops.transform.vertex_random(offset=1.0, uniform=0.1, normal=1.0, seed=0)
	taper_control = context.active_object
	taper_control.data.name = taper_control.name = 'Taper Control'

	# Set the main curve's taper control to the taper control curve.
	obj_data.taper_object = taper_control
	ops.object.mode_set(mode='OBJECT')

	rename_object('Taper Control','taper_control')

	move_object('complex_circle', (6,0,0))
	move_object('taper_control', (6,0,0))
	move_object('bevel_control', (6,0,0))

###############################################################################################
###############################################################################################
def curve_to_mesh():

	ops.curve.primitive_bezier_circle_add(enter_editmode=True)
	ops.curve.subdivide(number_cuts=18)

	# Cache a reference to the curve.
	curve = context.active_object

	# Locate the array of bezier points.
	bez_points = curve.data.splines[0].bezier_points

	sz = len(bez_points)
	i_to_theta = TWOPI / sz
	for i in range(0, sz, 1):

			# Set every sixth coordinate's z to 0.5.
			if i % 6 == 0:
					bez_points[i].co.z = 0.5

			if i % 2 == 0:
					bez_points[i].handle_right *= 2.0
					bez_points[i].handle_left *= 0.5
			elif i % 4 == 0:
					bez_points[i].handle_right.z -= 5.0
					bez_points[i].handle_left.z += 5.0
			else:
					bez_points[i].co *= 0.5

			# Shift cos(t) from -1 .. 1 to 0 .. 4.
			scalar = 2.0 + 2.0 * cos(i * i_to_theta)

			# Multiply coordinate by cos(t).
			bez_points[i].co *= scalar

	# Resize within edit mode.
	ops.transform.resize(value=(3.0, 3.0, 1.0))

	# Return to object mode.
	ops.object.mode_set(mode='OBJECT')

	# Convert from a curve to a mesh.
	ops.object.convert(target='MESH')

	# Append modifiers.
	skin_mod = curve.modifiers.new(name='Skin', type='SKIN')
	subsurf_mod = curve.modifiers.new(name='Subsurf', type='SUBSURF')
	stretch_mod = curve.modifiers.new(name='SimpleDeform', type='SIMPLE_DEFORM')

	# Adjust modifier options.
	skin_mod.use_smooth_shade = True
	subsurf_mod.levels = 3
	subsurf_mod.render_levels = 3
	stretch_mod.deform_method = 'STRETCH'
	stretch_mod.factor = 0.5

	rename_object('BezierCircle','meshed')

	move_object('meshed', (-6,0,0))

###############################################################################################
###############################################################################################
def heart():

	# Create curve and cache reference.
	ops.curve.primitive_bezier_circle_add(enter_editmode=False)
	curve = context.active_object
	curve.name = 'Heart Curve'
	bez_points = curve.data.splines[0].bezier_points

	# Set handles to desired handle type.
	for bez_point in bez_points:
			bez_point.handle_left_type = 'FREE'
			bez_point.handle_right_type = 'FREE'

	# Left point.
	bez_points[0].co = Vector((-1.0, 0.3, 0.0))
	bez_points[0].handle_left = Vector((-1.0, -0.25, 0.0))
	bez_points[0].handle_right = Vector((-1.0, 1.0, 0.0))

	# Top-middle point.
	bez_points[1].co = Vector((0.0, 0.5, 0.0))
	bez_points[1].handle_left = Vector((0.0, 1.0, 0.0))
	bez_points[1].handle_right = Vector((0.0, 1.0, 0.0))

	# Right point.
	bez_points[2].co = Vector((1.0, 0.3, 0.0))
	bez_points[2].handle_left = Vector((1.0, 1.0, 0.0))
	bez_points[2].handle_right = Vector((1.0, -0.25, 0.0))

	# Bottom point.
	bez_points[3].co = Vector((0.0, -1.0, 0.0))
	bez_points[3].handle_left = Vector((0.5, -0.5, 0.0))
	bez_points[3].handle_right = Vector((-0.5, -0.5, 0.0))

###############################################################################################
###############################################################################################
def heart2():
	# Create curve and cache reference.
	ops.curve.primitive_bezier_circle_add(enter_editmode=False)
	curve = context.active_object
	curve.name = 'Heart Curve'
	bez_points = curve.data.splines[0].bezier_points

	# Set handles to desired handle type.
	for bez_point in bez_points:
			bez_point.handle_left_type = 'FREE'
			bez_point.handle_right_type = 'FREE'

	# Left point.
	bez_points[0].co = Vector((-1.0, 0.3, 0.0))
	bez_points[0].handle_left = Vector((-1.0, -0.25, 0.0))
	bez_points[0].handle_right = Vector((-1.0, 1.0, 0.0))

	# Top-middle point.
	bez_points[1].co = Vector((0.0, 0.5, 0.0))
	bez_points[1].handle_left = Vector((0.0, 1.0, 0.0))
	bez_points[1].handle_right = Vector((0.0, 1.0, 0.0))

	# Right point.
	bez_points[2].co = Vector((1.0, 0.3, 0.0))
	bez_points[2].handle_left = Vector((1.0, 1.0, 0.0))
	bez_points[2].handle_right = Vector((1.0, -0.25, 0.0))

	# Bottom point.
	bez_points[3].co = Vector((0.0, -1.0, 0.0))
	bez_points[3].handle_left = Vector((0.5, -0.5, 0.0))
	bez_points[3].handle_right = Vector((-0.5, -0.5, 0.0))

	# Instead of replacing the curve with a mesh, keep the original curve.
	ops.object.convert(target='MESH', keep_original=True)

	# Cache reference to heart object.
	heart_mesh = context.active_object
	heart_mesh.name = 'Heart Mesh'

	# Switch to edit mode.
	ops.object.mode_set(mode='EDIT')

	# Select all the vertices on the boundary of the mesh.
	ops.mesh.select_all(action='SELECT')

	# Fill in with a face.
	ops.mesh.edge_face_add()

	# Convert n-gon face to triangles.
	# Ngon method options: ['BEAUTY', 'CLIP']
	ops.mesh.quads_convert_to_tris(ngon_method='CLIP')

	# Heart has bilateral symmetry.
	ops.mesh.symmetrize(direction='NEGATIVE_X', threshold=0.0001)

	# Reselect all faces.
	ops.mesh.select_all(action='SELECT')

	# Convert triangles to quadrilaterals.
	ops.mesh.tris_convert_to_quads(face_threshold=1.396264, shape_threshold=1.396264)

	# Inset faces.
	iter_range = range(0, 2, 1)
	for i in iter_range:
			ops.mesh.inset(thickness=0.25, use_relative_offset=True)

	# Switch to object mode.
	ops.object.mode_set(mode='OBJECT')

	# Add solidify modifier.
	solidify = heart_mesh.modifiers.new(type='SOLIDIFY', name='Solidify')
	solidify.offset = 0.0
	solidify.thickness = 0.125

	# Add Subsurface modifier.
	subsurf = heart_mesh.modifiers.new(type='SUBSURF', name='Subsurf')
	subsurf.levels = subsurf.render_levels = 3

###############################################################################################
###############################################################################################
def not_sure():
	delete_all_objects()

	# Create curve and cache reference.
	ops.curve.primitive_bezier_circle_add(enter_editmode=False)
	curve = context.active_object
	curve.name = 'Heart Curve'
	bez_points = curve.data.splines[0].bezier_points

	# Set handles to desired handle type.
	for bez_point in bez_points:
			bez_point.handle_left_type = 'FREE'
			bez_point.handle_right_type = 'FREE'

	# Left point.
	bez_points[0].co = Vector((-1.0, 0.3, 0.0))
	bez_points[0].handle_left = Vector((-1.0, -0.25, 0.0))
	bez_points[0].handle_right = Vector((-1.0, 1.0, 0.0))

	# Top-middle point.
	bez_points[1].co = Vector((0.0, 0.5, 0.0))
	bez_points[1].handle_left = Vector((0.0, 1.0, 0.0))
	bez_points[1].handle_right = Vector((0.0, 1.0, 0.0))

	# Right point.
	bez_points[2].co = Vector((1.0, 0.3, 0.0))
	bez_points[2].handle_left = Vector((1.0, 1.0, 0.0))
	bez_points[2].handle_right = Vector((1.0, -0.25, 0.0))

	# Bottom point.
	bez_points[3].co = Vector((0.0, -1.0, 0.0))
	bez_points[3].handle_left = Vector((2, 0.0, 0.0))
	bez_points[3].handle_right = Vector((-0.5, -0.5, 0.0))

	# Instead of replacing the curve with a mesh, keep the original curve.
	ops.object.convert(target='MESH', keep_original=True)

	# Cache reference to heart object.
	heart_mesh = context.active_object
	heart_mesh.name = 'Heart Mesh'

	# Switch to edit mode.
	ops.object.mode_set(mode='EDIT')

	# Select all the vertices on the boundary of the mesh.
	ops.mesh.select_all(action='SELECT')

	# Fill in with a face.
	ops.mesh.edge_face_add()

	# Convert n-gon face to triangles.
	# Ngon method options: ['BEAUTY', 'CLIP']
	ops.mesh.quads_convert_to_tris(ngon_method='CLIP')

	# Heart has bilateral symmetry.
	ops.mesh.symmetrize(direction='NEGATIVE_X', threshold=0.0001)

	# Reselect all faces.
	ops.mesh.select_all(action='SELECT')

	# Convert triangles to quadrilaterals.
	ops.mesh.tris_convert_to_quads(face_threshold=1.396264, shape_threshold=1.396264)

	# Inset faces.
	iter_range = range(0, 2, 1)
	for i in iter_range:
			ops.mesh.inset(thickness=0.25, use_relative_offset=True)

	# Switch to object mode.
	ops.object.mode_set(mode='OBJECT')

	# Add solidify modifier.
	solidify = heart_mesh.modifiers.new(type='SOLIDIFY', name='Solidify')
	solidify.offset = 0.0
	solidify.thickness = 0.125

	# Add Subsurface modifier.
	subsurf = heart_mesh.modifiers.new(type='SUBSURF', name='Subsurf')
	subsurf.levels = subsurf.render_levels = 3

###############################################################################################
###############################################################################################
def wtf():
	# Create curve and cache reference.
	ops.curve.primitive_bezier_circle_add(enter_editmode=False)
	curve = context.active_object
	curve.name = 'Heart Curve'
	bez_points = curve.data.splines[0].bezier_points

	# Set handles to desired handle type.
	for bez_point in bez_points:
			bez_point.handle_left_type = 'FREE'
			bez_point.handle_right_type = 'FREE'

	# Left point.
	bez_points[0].co = Vector((-1.0, 0.3, 0.0))
	bez_points[0].handle_left = Vector((-1.0, -0.25, 0.0))
	bez_points[0].handle_right = Vector((-1.0, 1.0, 0.0))

	# Top-middle point.
	bez_points[1].co = Vector((0.0, 0.5, 0.0))
	bez_points[1].handle_left = Vector((0.0, 1.0, 0.0))
	bez_points[1].handle_right = Vector((0.0, 1.0, 0.0))

	# Right point.
	bez_points[2].co = Vector((1.0, 0.3, 0.0))
	bez_points[2].handle_left = Vector((1.0, 1.0, 0.0))
	bez_points[2].handle_right = Vector((1.0, -0.25, 0.0))

	# Bottom point.
	bez_points[3].co = Vector((0.0, -1.0, 0.0))
	bez_points[3].handle_left = Vector((0.5, -0.5, 0.0))
	bez_points[3].handle_right = Vector((-0.5, -0.5, 0.0))

		# Create mesh.
	ops.object.mode_set(mode='OBJECT')
	ops.object.convert(target='MESH', keep_original=True)
	heart_mesh = context.active_object
	heart_mesh_data = heart_mesh.data
	heart_mesh_data.name = heart_mesh.name = 'Heart Mesh'

	# Grid Fill.
	# Span is an integer within the rage range [1, 1000]. Set it to zero to disable.
	# Offset is an integer within the range [-1000, 1000]. Set it to zero to disable.
	ops.object.mode_set(mode='EDIT')
	ops.mesh.select_all(action='SELECT')
	ops.mesh.fill_grid(span=5, offset=0, use_interp_simple=False)
	ops.object.mode_set(mode='OBJECT')

	# Add mirror modifier.
	mirror = heart_mesh.modifiers.new(name='Mirror', type='MIRROR')

	# Add solidify modifier.
	solidify = heart_mesh.modifiers.new(name='Solidify', type='SOLIDIFY')
	solidify.thickness = 0.025

	# Add subsurface modifier.
	subsurf = heart_mesh.modifiers.new(name='Subsurf', type='SUBSURF')
	subsurf.levels = 2
	subsurf.render_levels = 4

	# Apply mirror and solidify modifiers.
	#ops.object.modifier_apply_as('DATA', modifier='Mirror')
	#ops.object.modifier_apply_as('DATA', modifier='Solidify')

###############################################################################################
###############################################################################################
def examine():
	print("\n\n\n\n")
	for obj in bpy.context.scene.objects:
		if fnmatch.fnmatch(obj.name, "*urve*"):
			print("\n\n")
			obj.select_set(True)
			print("Object at ", obj.location)
			curve = obj
			print(curve.name)
			bez_points = curve.data.splines[0].bezier_points
			for bez_point in bez_points:
				print("co          ", bez_point.co)
				print("handle_right", bez_point.handle_left)
				print("handle_right", bez_point.handle_right)

	print("\n\n\n\n")

###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################

#greggo()
#delete_all_objects()

simple_curve()

#not_sure()

#complicated_circle()

#curve_to_mesh()

#wtf()
#examine()

bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))

