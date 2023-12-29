
from greg_blender import *
from mathutils import Vector
import bpy
import random
import pathlib
import os
import math
cwd = os. getcwd()

C = bpy.context
join_list = []

output_blend =  pathlib.PurePath(__file__).stem

###############################################################################################
###############################################################################################
def simple_curve():
	#bpy.context.object.data.splines[0].resolution_u = 40

	output_blend =  pathlib.PurePath(__file__).stem

	bpy.ops.curve.primitive_bezier_curve_add(enter_editmode=True, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
	#bpy.ops.curve.subdivide(number_cuts=2)
	bpy.ops.curve.subdivide(number_cuts=2)

	bpy.ops.object.editmode_toggle()
	#bpy.ops.transform.rotate(value=-0.41778, orient_axis='Z', orient_type='VIEW', orient_matrix=((1, -0, 0), (-0, 1, -0), (0, -0, 1)), orient_matrix_type='VIEW', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=False, use_snap_edit=False, use_snap_nonedit=False, use_snap_selectable=False)
	#bpy.ops.transform.rotate(value=-1.00891, orient_axis='Z', orient_type='VIEW', orient_matrix=((1, -0, 0), (-0, 1, -0), (0, -0, 1)), orient_matrix_type='VIEW', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=False, use_snap_edit=False, use_snap_nonedit=False, use_snap_selectable=False)
	#bpy.ops.object.editmode_toggle()
	#bpy.context.space_bpy.data.context = 'DATA'
	bpy.context.object.data.bevel_depth = 1.32
	bpy.context.object.data.bevel_resolution = 24
	# Cache a reference to the curve.
	curve = bpy.context.active_object
	curve.name = 'first curve'
	bez_points = curve.data.splines[0].bezier_points
	bez_points[0].co = Vector((12.0, 13, 0.0))
	bez_points[1].co = Vector((13.0,  12, 0.0))
	bez_points[2].co = Vector((13.0, 11, 0.0))
	bez_points[3].co = Vector((12.0, 10, 0.0))

	#bpy.ops.transform.resize(value=(2.565,2.565,2.565), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=False, use_snap_edit=False, use_snap_nonedit=False, use_snap_selectable=False)
	#rename_object('BezierCurve','a_simple_curve')
	#move_object('simple_curve', (25,-7,12))

cyls=[
	[ (-17.55, -1.3, 8),          (-9.07, -11.38, 8),           'cyl_01'],
	[ (-17.271, -1.61, 8),        (-4.3454, 25.341, 8),         'cyl_02'],
	[ (-18.5, 13, 8),             (-18.5, -19.0, 8),          'cyl_03'],
	[ (-4.032, -1.3666, 8),       (9.7093, 3.0667, 8),          'cyl_04'],
	[ (2.1759, 8.9635, 8),        (2.5, -7.2983, 8),            'cyl_05'],
	[ (2.238, 8.9, 8),            (2.446, -7.3114, 8),          'cyl_08'],
	[ (5.4821, -5.089, 8),        (5.4388, 9.4334, 8),          'cyl_12'],
	[ (4.1324, -6.7657, 8),       (5.4821, -5.089, 8),          'cyl_13'],
	[ (4.1871, -6.7663, 8),       (2.5514, -7.6583, 8),         'cyl_14'],
	[ (-0.10749, 8.3824, 8),     (-9.07, -11.38, 8),           'cyl_10'],
  [ (-0.10749, 8.3824, 8),       (2.1759, 8.9635, 8),         'cyl_11'],
  [ (.73045, 8.7949, 8),       (0.7306, 8.8, 8),         'cyl_11'],
	[ (5.5514,9.7713, 8),        (10.385, 11.85, 8),       'cyl_09'],
	[ (11.009,12.006, 8),        (11.736,11.902, 8),       'cyl_15'],
	[ ( 12.256, 4.3141 , 8),           ( 9.7093, 3.0667 , 8),  'cyl_16'],
	[ ( 10.333, 3.1446 , 8),           (15.487, -3.6552  , 8),  'cyl_17'],
	[ ( 23.969, -1.0981 , 8),           ( 15.487, -3.6552 , 8),  'cyl_18'],
	[ (24.219,7.1968  , 8),           ( 23.231,7.4567 , 8),  'cyl_19'],
	[ (18.138, 6.2094  , 8),           (  23.231,7.4567, 8),  'cyl_20'],
	[ ( 16.46,12.66 , 8),              (17.134, 13.708, 8),  'cyl_21'],
	[ ( 17.134, 13.708 , 8),           ( 17.583, 14.307 , 8),  'cyl_22'],
	[ ( 25.671, 17.673 , 8),           ( 17.583, 14.307  , 8),  'cyl_23'],
	[ ( 24.623, -0.66338 , 8),           ( 25.626, 0.5063 , 8),  'cyl_24'],
	#[ (  , 8),           (  , 8),  'cyl_25'],
	#[ (  , 8),           (  , 8),  'cyl_26'],
	#[ (  , 8),           (  , 8),  'cyl_27'],
]

if False:
	delete_objects_by_name_wildcard("ring*")

	bpy.ops.mesh.primitive_torus_add(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0), major_segments=128, minor_segments=40, minor_radius=0.05)
	bpy.ops.transform.resize(value=(26.7, 26.7, 26.7), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1))
		, orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH'
		, proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False
		, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=False
		, use_snap_edit=False, use_snap_nonedit=False, use_snap_selectable=False)
	obj = bpy.context.active_object
	obj.name = "ring"

if False:
	delete_objects_by_name_wildcard("curve*")
	bpy.ops.mesh.primitive_torus_add(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0), major_segments=128, minor_segments=40, minor_radius=0.20)
	bpy.ops.transform.resize(value=(5.3,5.3,5.3), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1))
		, orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH'
		, proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False
		, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=False
		, use_snap_edit=False, use_snap_nonedit=False, use_snap_selectable=False)
	obj = bpy.context.active_object
	obj.name = "curve1"
	#move_object("curve1", (8.1347,8.1802, 8))

	bpy.ops.mesh.primitive_torus_add(align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0), major_segments=128, minor_segments=40, minor_radius=0.20)
	bpy.ops.transform.resize(value=(4.552, 4.552, 4.552), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1))
		, orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH'
		, proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False
		, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='CLOSEST', use_snap_self=False
		, use_snap_edit=False, use_snap_nonedit=False, use_snap_selectable=False)
	obj = bpy.context.active_object
	obj.name = "curve2"
	#move_object("curve2", (20.151,10.499, 8))

delete_objects_by_name_wildcard("cyl_*")

count = 1
for foo in cyls:
	#print(foo)
	cylinder_between(foo[2], foo[0],foo[1],     1.3, ROUNDED=True)
	count += 1

delete_objects_by_name_wildcard("Basic_Sphere*")

simple_curve()

bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))

