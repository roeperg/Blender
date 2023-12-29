
from math import *
# from mathutils import Vector
import bmesh
import bpy
import mathutils
import numpy
import os
import random
import sys
import math
import fnmatch

X,Y,Z,ALL = range(4)
C = bpy.context

"""
import bpy

view_layer = bpy.context.view_layer

# Create new light datablock.
light_data = bpy.data.lights.new(name="New Light", type='POINT')

# Create new object with our light datablock.
light_object = bpy.data.objects.new(name="New Light", object_data=light_data)

# Link light object to the active collection of current view layer,
# so that it'll appear in the current scene.
view_layer.active_layer_collection.collection.objects.link(light_object)

# Place light to a specified location.
light_object.location = (5.0, 5.0, 5.0)

# And finally select it and make it active.
light_object.select_set(True)
view_layer.objects.active = light_object
"""


###############################################################################################
###############################################################################################
def clearscreen():
	absolutely_unused_variable = os.system("cls")

###############################################################################################
###############################################################################################
def delete_all_objects():
	bpy.ops.object.select_all(action='SELECT')
	bpy.ops.object.delete()

###############################################################################################
###############################################################################################
def deselect_all():
	bpy.ops.object.select_all(action='SELECT')
	bpy.ops.object.delete()

###############################################################################################
###############################################################################################
def SAE2Metric(inVal):
	return inVal * 25.4

###############################################################################################
###############################################################################################
def set_3d_cursor(LOCATION=(0,0,0)):
	saved_location = C.scene.cursor.location.copy()
	C.scene.cursor.location = LOCATION
	print(saved_location)
	return saved_location
	
###############################################################################################
###############################################################################################
def Deg2Rad(inX,inY,inZ):
		return (pi*inX/180,pi*inY/180,pi*inZ/180)

###############################################################################################
###############################################################################################
def verts_labels(in_text):
	# text is tab delimited
	# vert number, x, y z
	in_text = in_text.replace("\t"," ").strip()
	barray = in_text.split("\n")
	headers = barray.pop(0)
	doneski = {}
	for foo in barray:
		foo = foo.strip()
		if len(foo) < 8:
			break
		(pnt, x, y , z, facename) = foo.split(",")

		keystring = "%03d%03d%03d" %(float(x), float(y), float(z))

		if keystring not in doneski.keys():
			doneski[keystring] = 1
			bpy.ops.object.text_add(location=(float(x), float(y), float(z)))
			ob=bpy.context.object
			ob.data.body = pnt
			ob.name = "text%s" %pnt
			ob.data.extrude = 0.1
			ob.data.bevel_depth = 0.02
			scale_object(ob.name, (2,2,2))

###############################################################################################
###############################################################################################
def verts_faces(inverts, infaces, in_text):
	# text is tab delimited
	# vert number, x, y z
	saveface = ""
	verts = []
	faces = []
	points = ""
	in_text = in_text.replace("\t"," ").strip()
	barray = in_text.split("\n")
	headers = barray.pop(0)

	current_v = 0
	for foo in barray:
		foo = foo.strip()
		if len(foo) < 8:
			break
		sarray = foo.split(",")

		(pnt, x, y , z, facename) = foo.split(",")
		#(v, z, y, x) = foo.split(",")
		#(v, y, x, z) = foo.split(",")

		if saveface != facename:
			saveface = facename
			if len(verts):
				for foo in verts:
					inverts.append(foo)
				infaces.append(tuple(faces))
				verts = []
				faces = []
			points += "\n%s    " %facename

		verts.append((float(x), float(y), float(z)))
		faces.append(int(current_v))
		current_v += 1
		points += "%s-" %pnt

	points += "\n"
	points = points.replace("-\n","\n")
	for foo in verts:
		inverts.append(foo)
	infaces.append(tuple(faces))
	return (inverts, infaces)

###############################################################################################
###############################################################################################
def base_points(in_file):

	with open(in_file, 'rt') as content_file:
		f1 = content_file.read()
	verts_labels(f1)

###############################################################################################
###############################################################################################
def base_framework(in_object_name, in_filename):

	with open(in_filename, 'r') as content_file:
		f1 = content_file.read()

	rect_verts = []
	rect_faces = []

	(temp_rect, temp_face) = verts_faces(rect_verts,rect_faces, f1)

	mesh_data = bpy.data.meshes.new("cube_mesh_data")
	mesh_data.from_pydata(rect_verts, [], rect_faces)
	mesh_data.update()

	obj = bpy.data.objects.new(in_object_name, mesh_data)

	scene = bpy.context.scene
	scene.collection.objects.link(obj)
	join_list.append(in_object_name)

###############################################################################################
###############################################################################################
def join_objects_by_name(in_list):

	scene = bpy.context.scene
	bpy.ops.object.select_all(action="DESELECT")

	for ob in in_list:
		obj = bpy.data.objects[ob]
		obj.select_set(True)
		bpy.context.view_layer.objects.active = obj

	bpy.ops.object.join()

##############################################################################################
###############################################################################################
def extrude_plane(extrusion_tuple):
	bpy.ops.object.editmode_toggle()
	bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False
																			, "mirror":False}
																			, TRANSFORM_OT_translate={"value":extrusion_tuple
																			, "orient_type":'LOCAL'
																			, "orient_matrix":((1, 0, 0), (0 , 1, 0), (0, 0, 1))
																			, "orient_matrix_type":'LOCAL'
																			, "constraint_axis":(False, False, False)  # z was true originally
																			, "mirror":False
																			, "use_proportional_edit":False
																			, "proportional_edit_falloff":'SMOOTH'
																			, "proportional_size":1
																			, "use_proportional_connected":False
																			, "use_proportional_projected":False
																			, "snap":False
																			, "snap_target":'CLOSEST'
																			, "snap_point":(0, 0, 0)
																			, "snap_align":False
																			, "snap_normal":(0, 0, 0)
																			, "gpencil_strokes":False
																			, "cursor_transform":False
																			, "texture_space":False
																			, "remove_on_cancel":False
																			, "release_confirm":False
																			, "use_accurate":False})
	bpy.ops.object.editmode_toggle()

	return

###############################################################################################
###############################################################################################
def set_object_center(in_object_name, TYPE='ORIGIN_CENTER_OF_VOLUME'):
	# active object
	print("Centering ", in_object_name)

	objectToSelect = bpy.data.objects[in_object_name]
	objectToSelect.select_set(True)
	bpy.ops.object.origin_set(type=TYPE, center='MEDIAN')
	
###############################################################################################
###############################################################################################
def get_object_dimensions(in_object_name):
	#example   [10.890256881713867, 10.890256881713867, 4.956655979156494]
	bpy.ops.object.select_all(action="DESELECT")
	obj = bpy.data.objects[in_object_name]
	return list(obj.dimensions	)

###############################################################################################
###############################################################################################
def get_object_bound_box(in_object_name):
	bpy.ops.object.select_all(action="DESELECT")
	obj = bpy.data.objects[in_object_name]
	return list(obj.bound_box	)

###############################################################################################
###############################################################################################
def get_object_delta_scale(in_object_name):
	bpy.ops.object.select_all(action="DESELECT")
	obj = bpy.data.objects[in_object_name]
	return list(obj.delta_scale	)

###############################################################################################
###############################################################################################
def get_object_location(in_object_name):
        bpy.ops.object.select_all(action="DESELECT")
        obj = bpy.data.objects[in_object_name]
        return list(obj.location        )



###############################################################################################
###############################################################################################
def get_object_scale(in_object_name):
        bpy.ops.object.select_all(action="DESELECT")
        obj = bpy.data.objects[in_object_name]
        return list(obj.scale   )



###############################################################################################
###############################################################################################
def get_object_rotation_euler(in_object_name):
        bpy.ops.object.select_all(action="DESELECT")
        obj = bpy.data.objects[in_object_name]
        return list(obj.rotation_euler  )



###############################################################################################
###############################################################################################
def get_object_rotation_quaternion(in_object_name):
        bpy.ops.object.select_all(action="DESELECT")
        obj = bpy.data.objects[in_object_name]
        return list(obj.rotation_quaternion     )



###############################################################################################
###############################################################################################
def get_object_show_name(in_object_name):
        bpy.ops.object.select_all(action="DESELECT")
        obj = bpy.data.objects[in_object_name]
        return list(obj.show_name       )



###############################################################################################
###############################################################################################
def get_object_type(in_object_name):
        bpy.ops.object.select_all(action="DESELECT")
        obj = bpy.data.objects[in_object_name]
        return obj.type   



###############################################################################################
###############################################################################################
def get_object_children(in_object_name):
        bpy.ops.object.select_all(action="DESELECT")
        obj = bpy.data.objects[in_object_name]
        return list(obj.children        )

###############################################################################################
###############################################################################################




###############################################################################################
###############################################################################################
def move_object(in_object_name, in_location):

	bpy.ops.object.select_all(action="DESELECT")
	obj = bpy.data.objects[in_object_name]
	obj.location = in_location

###############################################################################################
###############################################################################################
def move_object_relative(in_object_name, in_offset):

	bpy.ops.object.select_all(action="DESELECT")
	location = get_object_location(in_object_name)
	obj = bpy.data.objects[in_object_name]
	new_location = [0.0,0.0,0.0]
	for i in range(len(in_offset)):
		new_location[i] = location[i] + in_offset[i]
	obj.location = new_location
###############################################################################################
###############################################################################################
def copy_object (in_object_name, in_new_name, data=True, actions=True, collection=None):
	bpy.ops.object.select_all(action="DESELECT")
	obj = bpy.data.objects[in_object_name]
	print(">>>>>>>>>>>>>>", bpy.context.view_layer.objects.active)

	obj_copy = obj.copy()
	if data:
		obj_copy.data = obj_copy.data.copy()
	if actions and obj_copy.animation_data:
		obj_copy.animation_data.action = obj_copy.animation_data.action.copy()
	#if collection:
	#	collection.objects.link(obj_copy)
	obj_copy.name = in_new_name
	print("Copied %s to %s" %(in_object_name, in_new_name))
	for obj in bpy.data.objects:
		print(">>", obj.name)
	
###############################################################################################
###############################################################################################
def cutout_same_shape(in_object_name, in_scale, AXIS=Z):
	
	C = bpy.context
	src_obj = bpy.data.objects[in_object_name]
	print(src_obj)
	new_obj = src_obj.copy()
	new_obj.data = src_obj.data.copy()
	new_obj.animation_data_clear()
	C.collection.objects.link(new_obj)

	print("SCALE ", new_obj.scale)
	new_scale = new_obj.scale * in_scale
	if AXIS != ALL:
		new_scale[AXIS] = src_obj.scale[AXIS] * 1.5
		print("NEW SCALE ", new_scale)
	new_obj.scale = new_scale

	new_obj.select_set(False)

	boolean_difference(in_object_name, new_obj.name)
	remove_object(new_obj.name)

	#remove_object(temp_name)

###############################################################################################
###############################################################################################
def curve_to_mesh(in_object_name):

	bpy.ops.object.select_all(action="DESELECT")
	obj = bpy.data.objects[in_object_name]
	obj.convert(target='MESH', keep_original=True)
	
	
###############################################################################################
###############################################################################################
def scale_object(in_object_name, in_scale):

	bpy.ops.object.select_all(action="DESELECT")
	obj = bpy.data.objects[in_object_name]
	obj.scale = in_scale

###############################################################################################
###############################################################################################
def rotate_object(in_object_name, in_rotation):
	bpy.ops.object.select_all(action="DESELECT")
	obj = bpy.data.objects[in_object_name]
	obj.rotation_euler = Deg2Rad(in_rotation[0],in_rotation[1],in_rotation[2])

###############################################################################################
###############################################################################################
def remove_object(inBase):

	bpy.ops.object.select_all(action="DESELECT")
	objectToSelect = bpy.data.objects[inBase]
	objectToSelect.select_set(True)
	bpy.context.view_layer.objects.active = objectToSelect
	bpy.ops.object.delete(use_global=False, confirm=False)

###############################################################################################
###############################################################################################
def boolean_difference(inBase, inCutout, SOLVER='EXACT'):

	bpy.ops.object.select_all(action="DESELECT")
	objectToSelect = bpy.data.objects[inBase]
	objectToSelect.select_set(True)
	bpy.context.view_layer.objects.active = objectToSelect

	#bpy.context.space_data.context = 'MODIFIER'
	bpy.ops.object.modifier_add(type='BOOLEAN')
	bpy.context.object.modifiers["Boolean"].solver = SOLVER
	bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[inCutout]
	bpy.context.object.modifiers["Boolean"].operation = 'DIFFERENCE'
	bpy.ops.object.modifier_apply(modifier="Boolean", report=True)

###############################################################################################
###############################################################################################
def cutout_sphere(inBase, cutout_pos, cutout_size, SEGMENTS=32, RINGS=16, ROTATION=(0,0,0) , SOLVER='EXACT'):
	build_sphere("temp_shape_for_cutting_out_sphere", cutout_pos, cutout_size, SMOOTH=False, SEGMENTS=32, RINGS=16)
	boolean_difference(inBase, "temp_shape_for_cutting_out_sphere", SOLVER=SOLVER)
	remove_object("temp_shape_for_cutting_out_sphere")

###############################################################################################
###############################################################################################
def cutout_cylinder(inBase, cutout_pos, cutout_size, VERTICES=128, ROTATION=(0,0,0) , SOLVER='EXACT'):
	build_cylinder("temp_shape_for_cutting_out_cylinder", cutout_pos, cutout_size, VERTICES=VERTICES, ROTATION=ROTATION)
	boolean_difference(inBase, "temp_shape_for_cutting_out_cylinder", SOLVER=SOLVER)
	remove_object("temp_shape_for_cutting_out_cylinder")

###############################################################################################
###############################################################################################
def cutout_cube(inBase, cutout_pos, cutout_size, ROTATION=(0,0,0) , SOLVER='EXACT'):
	build_cube("temp_shape_for_cutting_out_cube", cutout_pos, cutout_size, ROTATION=ROTATION)
	boolean_difference(inBase, "temp_shape_for_cutting_out_cube", SOLVER=SOLVER)
	remove_object("temp_shape_for_cutting_out_cube")

###############################################################################################
###############################################################################################
def build_extruded_plane(
								 vertex_csv                         # list of vertexes.  3 numbers (x,y,z) for each vertex.
							 , edge_list                          # list of point offsets for each segment
							 , extrude_tuple                      # 3 member tuple for extrusion
							 , in_object_name
							 , CENTER_ORIGIN=False
								):

	vertex_point_index_for_segments = []
	vertex_list = []

	with open(vertex_csv, 'r') as content_file:
		f1 = content_file.read()

	for foo in f1.split("\n"):
		for bar in foo.split(","):
			try:
				vertex_list.append(float(bar))
			except Exception:
				pass

	for i in range(len(vertex_list)):
		if i%3 == 0:
			vertex_point_index_for_segments.append(i/3)

	vertices = numpy.array(vertex_list, dtype=numpy.float32)
	num_vertices = vertices.shape[0] // 3

	vertex_index = numpy.array(vertex_point_index_for_segments, dtype=numpy.int32)
	loop_start = numpy.array([0], dtype=numpy.int32)
	loop_total = numpy.array([num_vertices], dtype=numpy.int32)
	edges = numpy.array(edge_list, dtype=numpy.int32)
	num_edges = edges.shape[0] // 2

	num_vertex_indices = vertex_index.shape[0]
	num_loops = loop_start.shape[0]

	mesh = bpy.data.meshes.new(name='created mesh')

	mesh.vertices.add(num_vertices)
	mesh.vertices.foreach_set("co", vertex_list)

	mesh.edges.add(num_edges)
	mesh.edges.foreach_set("vertices", edges)

	mesh.loops.add(num_vertex_indices)
	mesh.loops.foreach_set("vertex_index", vertex_index)

	mesh.polygons.add(num_loops)
	mesh.polygons.foreach_set("loop_start", loop_start)
	mesh.polygons.foreach_set("loop_total", loop_total)

	mesh.update()
	mesh.validate()

	obj = bpy.data.objects.new('created object', mesh)

	scene = bpy.context.scene
	scene.collection.objects.link(obj)

	# Select the new object and make it active
	bpy.ops.object.select_all(action='DESELECT')
	obj.select_set(True)
	bpy.context.view_layer.objects.active = obj

	extrude_plane(extrude_tuple)

	obj = bpy.context.active_object
	obj.name = in_object_name

	if CENTER_ORIGIN:
		bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')



###############################################################################################
###############################################################################################
def build_torus(in_object_name, pos, scale, major_rad=1, minor_rad=.25, major_segments=128, minor_segments=48, ROTATION=(0,0,0)):

	bpy.ops.object.select_all(action="DESELECT")
	bpy.ops.mesh.primitive_torus_add(location=pos, rotation=ROTATION
																 , major_radius=major_rad, minor_radius=minor_rad
																 , major_segments=major_segments, minor_segments=minor_segments
																 , abso_major_rad=major_rad*1.25, abso_minor_rad=minor_rad*3)
	bpy.ops.transform.resize(value=scale, orient_type='GLOBAL'
	, orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1))
	, orient_matrix_type='GLOBAL', constraint_axis=(False, False, True)
	, mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH'
	, proportional_size=1, use_proportional_connected=False
	, use_proportional_projected=False)

	obj = bpy.context.active_object
	obj.name = in_object_name

###############################################################################################
###############################################################################################
def build_rounded_cube(in_object_name, pos, scale):
	build_frame("temp_frame", pos, scale)
	build_cube(in_object_name, pos, scale)
	join_objects_by_name(["temp_frame",in_object_name ])
	
###############################################################################################
###############################################################################################
def build_cube(in_object_name, pos, scale, ROTATION=(0,0,0)):

	bpy.ops.object.select_all(action="DESELECT")
	bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=pos)
	bpy.ops.transform.resize(value=scale, orient_type='GLOBAL'
	, orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1))
	, orient_matrix_type='GLOBAL', constraint_axis=(False, False, True)
	, mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH'
	, proportional_size=1, use_proportional_connected=False
	, use_proportional_projected=False)
	obj = bpy.context.active_object
	obj.name = in_object_name
	rotate_object(obj.name, ROTATION)

###############################################################################################
###############################################################################################
def build_circle(in_object_name, pos, radius, ROTATION=(0,0,0), SMOOTH=False, VERTICES=32):

	bpy.ops.object.select_all(action="DESELECT")
	
	bpy.ops.mesh.primitive_circle_add(enter_editmode=False, location=pos)
	obj = bpy.context.active_object
	obj.radius = radius
	obj.name = in_object_name
	rotate_object(obj.name, ROTATION)




###############################################################################################
###############################################################################################
def build_frame(in_object_name, pos, scale):
	
	radius = 10000
	radious_offset = 0
 
	# length, rotate, move
	cylinders0 = [[(0,0,0),(0,scale[1],0)],
					[(0,scale[1],0),(0,scale[1],scale[2])],
					[(0,scale[1],scale[2]),(0,0,scale[2])],
					[(0,0,scale[2]),(0,0,0)],
					]

	cylinders1 = [[(0,0,0),(scale[0],0,0)],
					[(scale[0],0,0),(scale[0],0,scale[2])],
					[(scale[0],0,scale[2]),(0,0,scale[2])],
					[(0,0,scale[2]),(0,0,0)],
					]

	cylinders2 = [[(0,0,0),(scale[0],0,0)],
					[(scale[0],0,0),(scale[0],scale[1],0)],
					[(scale[0],scale[1],0),(0,scale[1],0)],
					[(0,scale[1],0),(0,0,0)],
					]

	points0 = [(0,0,0),(0,scale[1],0),(0,scale[1],scale[2]),(0,0,scale[2])]
	points1 = [(0,0,0),(scale[0],0,0),(scale[0],0,scale[2]),(0,0,scale[2])]
	points2 = [(0,0,0),(scale[0],0,0),(scale[0],scale[1],0),(0,scale[1],0)]
	

	if scale[0] < radius:
		radius = scale[0]
		radius_offset = 0 
		points = points0 
		
	if scale[1] < radius:
		radius = scale[1]
		radius_offset = 1  
		points = points1

	if scale[2] < radius:
		radius = scale[2]
		radius_offset = 2  
		points = points2 

	bpy.ops.object.select_all(action="DESELECT")
	build_sphere("r1", points[0]  , (radius,radius,radius), SMOOTH=True)
	build_sphere("r2", points[1]  , (radius,radius,radius), SMOOTH=True)
	build_sphere("r3", points[2]  , (radius,radius,radius), SMOOTH=True)
	build_sphere(in_object_name, points[3 ] , (radius,radius,radius), SMOOTH=False)
	if scale[0] == radius:
		#Build y and z cylinders
		build_cylinder("c1", (0,0,0), (radius,radius,scale[1]), ROTATION=(90,0,0), SMOOTH=True )
		move_object("c1", (0,scale[1]/2,0))
		build_cylinder("c2", (0,0,0), (radius,radius,scale[1]), ROTATION=(90,0,0), SMOOTH=True )
		move_object("c2", (0,scale[1]/2,scale[2]))
		build_cylinder("c3", (0,0,0), (radius,radius,scale[2]), ROTATION=(0,0,90), SMOOTH=True )
		move_object("c3", (0,0,scale[2]/2))
		build_cylinder("c4", (0,0,0), (radius,radius,scale[2]), ROTATION=(0,0,90), SMOOTH=True )
		move_object("c4", (0,scale[1],scale[2]/2))
	elif scale[1] == radius:
		build_cylinder("c1", (0,0,0), (radius,radius,scale[0]), ROTATION=(0,90,0), SMOOTH=True )
		move_object("c1", (scale[0]/2,0,0))
		build_cylinder("c2", (0,0,0), (radius,radius,scale[0]), ROTATION=(0,90,0), SMOOTH=True )
		move_object("c2", (scale[0]/2,0,scale[2]))
		build_cylinder("c3", (0,0,0), (radius,radius,scale[2]), ROTATION=(0,0,0), SMOOTH=True )
		move_object("c3", (0,0,scale[2]/2))
		build_cylinder("c4", (0,0,0), (radius,radius,scale[2]), ROTATION=(0,0,0), SMOOTH=True )
		move_object("c4", (scale[0],0,scale[2]/2))
	elif scale[2] == radius:
		build_cylinder("c1", (0,0,0), (radius,radius,scale[0]), ROTATION=(0,90,0), SMOOTH=True )
		move_object("c1", (scale[0]/2,0,0))
		build_cylinder("c2", (0,0,0), (radius,radius,scale[0]), ROTATION=(0,90,0), SMOOTH=True )
		move_object("c2", (scale[0]/2,scale[1],0))
		build_cylinder("c3", (0,0,0), (radius,radius,scale[1]), ROTATION=(90,0,0), SMOOTH=True )
		move_object("c3", (0,scale[1]/2,0))
		build_cylinder("c4", (0,0,0), (radius,radius,scale[1]), ROTATION=(90,0,0), SMOOTH=True )
		move_object("c4", (scale[0],scale[1]/2,0))
	
	if True:
		join_objects_by_name(["c1","c2","c3","c4","r1","r2","r3",in_object_name ])
		bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS', center='MEDIAN')
		move_object (in_object_name,pos)

###############################################################################################
###############################################################################################
def build_sphere(in_object_name, pos, scale, SEGMENTS=32, RINGS=16, SMOOTH=False):
	# Create an empty mesh and the object.
	mesh = bpy.data.meshes.new('Basic_Sphere')
	basic_sphere = bpy.data.objects.new("Basic_Sphere", mesh)

	# Add the object into the scene.
	bpy.context.collection.objects.link(basic_sphere)

	# Select the newly created object
	bpy.context.view_layer.objects.active = basic_sphere
	basic_sphere.select_set(True)

	# Construct the bmesh sphere and assign it to the blender mesh.
	#GREGGObm = bmesh.new()
	bpy.ops.mesh.primitive_uv_sphere_add(segments=SEGMENTS, ring_count=RINGS, radius=0.5, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

	#GREGGObmesh.ops.create_uvsphere(bm, u_segments=SEGMENTS, v_segments=32, radius=.5)
	#GREGGObm.to_mesh(mesh)
	#GREGGObm.free()

	bpy.ops.transform.resize(value=scale, orient_type='GLOBAL'
			, orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1))
			, orient_matrix_type='GLOBAL', constraint_axis=(False, False, True)
			, mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH'
			, proportional_size=1, use_proportional_connected=False
	, use_proportional_projected=False)

	if SMOOTH == True:
		bpy.ops.object.modifier_add(type='SUBSURF')
		bpy.ops.object.shade_smooth()

	obj = bpy.context.active_object
	obj.name = in_object_name
	move_object(in_object_name, pos)
	
###############################################################################################
###############################################################################################
def build_cylinder(in_object_name, pos, scale, ROTATION=(0,0,0), SMOOTH=False, VERTICES=32):

	bpy.ops.object.select_all(action="DESELECT")
	bpy.ops.mesh.primitive_cylinder_add(radius=.5, vertices=VERTICES, depth=1, enter_editmode=False, location=(0, 0, 0))
	bpy.ops.transform.resize(value=scale, orient_type='GLOBAL'
			, orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1))
			, orient_matrix_type='GLOBAL', constraint_axis=(False, False, True)
			, mirror=True, use_proportional_edit=False   #, proportional_edit_falloff='SMOOTH'
			, proportional_size=2, use_proportional_connected=False
	, use_proportional_projected=False
	)
	if SMOOTH:
		bpy.ops.object.modifier_add(type='SUBSURF')
		bpy.ops.object.shade_smooth()
	obj = bpy.context.active_object
	obj.name = in_object_name
	rotate_object(obj.name, ROTATION)
	move_object(obj.name, pos)

###############################################################################################
###############################################################################################
def build_cylinder_diameter(in_object_name, pos, scale, ROTATION=(0,0,0), SMOOTH=False, VERTICES=32):

	bpy.ops.object.select_all(action="DESELECT")
	bpy.ops.mesh.primitive_cylinder_add(radius=1.0, vertices=VERTICES, depth=1, enter_editmode=False, location=(0, 0, 0))
	bpy.ops.transform.resize(value=scale, orient_type='GLOBAL'
			, orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1))
			, orient_matrix_type='GLOBAL', constraint_axis=(False, False, True)
			, mirror=True, use_proportional_edit=False   #, proportional_edit_falloff='SMOOTH'
			, proportional_size=2, use_proportional_connected=False
	, use_proportional_projected=False
	)
	if SMOOTH:
		bpy.ops.object.modifier_add(type='SUBSURF')
		bpy.ops.object.shade_smooth()
	obj = bpy.context.active_object
	obj.name = in_object_name
	rotate_object(obj.name, ROTATION)
	move_object(obj.name, pos)

###############################################################################################
###############################################################################################
def to_wall(x1,y1,z1,x2,y2,z2, offset):
	tmp_verts = [
			( x1,  y1,  z1),
			( x1,  y2,  z1),
			( x1,  y2, z2),
			( x1,  y1 ,z2),

			( x2,  y1,  z1),
			( x2,  y2,  z1),
			( x2,  y2, z2),
			( x2,  y1 ,z2),
	]

	tmp_faces = [
			(0+offset, 1+offset, 2+offset, 3+offset),
			(4+offset, 7+offset, 6+offset, 5+offset),
			(0+offset, 4+offset, 5+offset, 1+offset),
			(1+offset, 5+offset, 6+offset, 2+offset),
			(2+offset, 6+offset, 7+offset, 3+offset),
			(4+offset, 0+offset, 3+offset, 7+offset)
	]

	return (tmp_verts, tmp_faces)


###############################################################################################
###############################################################################################
def build_get_object_data(inFlavor):

	print ("""
###############################################################################################
###############################################################################################
def get_object___FLAVOR__(in_object_name):
	bpy.ops.object.select_all(action="DESELECT")
	obj = bpy.data.objects[in_object_name]
	return list(obj.__FLAVOR__	)

""".replace("__FLAVOR__", inFlavor))



###############################################################################################
###############################################################################################
def define_material_hsv (matname, h,s,v,a, METALLIC=0.0):
	new_material = bpy.data.materials.new(matname)
	new_material.diffuse_color =  (h,s,v,a)
	new_material.metallic = METALLIC
	print(">>>>>>>>>>>>>>>>       ", METALLIC)
	return new_material

###############################################################################################
###############################################################################################
def set_material(inobject, inmaterial):
	current_object = bpy.data.objects.get(inobject)
	current_object.active_material = inmaterial




###############################################################################################
###############################################################################################
def test_my_stuff():

	bpy.ops.object.select_all(action="DESELECT")
	bpy.ops.mesh.primitive_cube_add(size=15, enter_editmode=False, location=(0,0,0,))
	bpy.ops.object.modifier_add(type='SUBSURF')
	bpy.context.object.modifiers["Subdivision"].levels = 3
	bpy.ops.object.editmode_toggle()
	bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":15, "smoothness":0, "falloff":'INVERSE_SQUARE', "object_index":0
		, "edge_index":7, "mesh_select_mode_init":(True, False, False)}
		#, TRANSFORM_OT_edge_slide={"value":-0, "single_side":False, "use_even":False
		#, "flipped":False, "use_clamp":True, "mirror":True, "snap":False, "snap_target":'CLOSEST'
		#, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0)
		#, "correct_uv":True, "release_confirm":True, "use_accurate":False
		#  }
			)
	#bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, "smoothness":0, "falloff":'INVERSE_SQUARE', "object_index":0, "edge_index":14, "mesh_select_mode_init":(True, False, False)}, TRANSFORM_OT_edge_slide={"value":0, "single_side":False, "use_even":False, "flipped":False, "use_clamp":True, "mirror":True, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "correct_uv":True, "release_confirm":True, "use_accurate":False})
	#bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, "smoothness":0, "falloff":'INVERSE_SQUARE', "object_index":0, "edge_index":22, "mesh_select_mode_init":(True, False, False)}, TRANSFORM_OT_edge_slide={"value":0, "single_side":False, "use_even":False, "flipped":False, "use_clamp":True, "mirror":True, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "correct_uv":True, "release_confirm":True, "use_accurate":False})
	#bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, "smoothness":0, "falloff":'INVERSE_SQUARE', "object_index":0, "edge_index":22, "mesh_select_mode_init":(True, False, False)}, TRANSFORM_OT_edge_slide={"value":0, "single_side":False, "use_even":False, "flipped":False, "use_clamp":True, "mirror":True, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "correct_uv":True, "release_confirm":True, "use_accurate":False})
	#bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, "smoothness":0, "falloff":'INVERSE_SQUARE', "object_index":0, "edge_index":40, "mesh_select_mode_init":(True, False, False)}, TRANSFORM_OT_edge_slide={"value":0, "single_side":False, "use_even":False, "flipped":False, "use_clamp":True, "mirror":True, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "correct_uv":True, "release_confirm":True, "use_accurate":False})
	#bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, "smoothness":0, "falloff":'INVERSE_SQUARE', "object_index":0, "edge_index":62, "mesh_select_mode_init":(True, False, False)}, TRANSFORM_OT_edge_slide={"value":-0, "single_side":False, "use_even":False, "flipped":False, "use_clamp":True, "mirror":True, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "correct_uv":True, "release_confirm":True, "use_accurate":False})
	#bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, "smoothness":0, "falloff":'INVERSE_SQUARE', "object_index":0, "edge_index":76, "mesh_select_mode_init":(True, False, False)}, TRANSFORM_OT_edge_slide={"value":0, "single_side":False, "use_even":False, "flipped":False, "use_clamp":True, "mirror":True, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "correct_uv":True, "release_confirm":True, "use_accurate":False})
	#bpy.ops.mesh.loopcut_slide(MESH_OT_loopcut={"number_cuts":1, "smoothness":0, "falloff":'INVERSE_SQUARE', "object_index":0, "edge_index":94, "mesh_select_mode_init":(True, False, False)}, TRANSFORM_OT_edge_slide={"value":-0, "single_side":False, "use_even":False, "flipped":False, "use_clamp":True, "mirror":True, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "correct_uv":True, "release_confirm":True, "use_accurate":False})
	#bpy.ops.object.editmode_toggle()
	#bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subdivision")


###############################################################################################
###############################################################################################
def makePrimitiveCircle(objName, v, r, f, loc, rot):
    bpy.ops.mesh.primitive_circle_add(
        vertices=v, 
        radius=r, 
        fill_type=f, 
        #view_align=False, 
        enter_editmode=False, 
        location=loc, 
        rotation=rot)
    obj = bpy.context.active_object
    obj.name = objName
    obj.show_name = True
    me = obj.data
    me.name = objName + 'Mesh'
    return obj


###############################################################################################
###############################################################################################
def delete_objects_by_name_wildcard(inname):
	for obj in bpy.context.scene.objects:
		if fnmatch.fnmatch(obj.name, inname):
			obj.select_set(True)
		else:
			obj.select_set(False)
	bpy.ops.object.delete()
		

###############################################################################################
###############################################################################################
def cylinder_between(inname, point1, point2, r, ROUNDED=False):     #  adapted from Martin McBride

	dx = point2[0] - point1[0]
	dy = point2[1] - point1[1]
	dz = point2[2] - point1[2]

	dist = math.sqrt(dx**2 + dy**2 + dz**2)

	#if ROUNDED:
	#	dist -= r  #(2*r)

	bpy.ops.mesh.primitive_cylinder_add(
			radius = r,
			depth = dist,
			location = (0,0,0)
	)

	phi = math.atan2(dy, dx)
	theta = math.acos(dz/dist)

	bpy.context.active_object.name = inname
	
	if ROUNDED:
		# convert to diameter
		d = r * 2
		build_sphere("endcap1", (0, 0, dist/2) , (d,d,d), SEGMENTS=32, RINGS=16, SMOOTH=False)
		build_sphere("endcap2", (0, 0, -dist/2) , (d,d,d), SEGMENTS=32, RINGS=16, SMOOTH=False)
		
		join_objects_by_name(["endcap1","endcap2", inname])

	bpy.context.object.rotation_euler[1] = theta
	bpy.context.object.rotation_euler[2] = phi
	move_object(inname, (dx/2 + point1[0], dy/2 + point1[1], dz/2 + point1[2]))

###############################################################################################
###############################################################################################
def rename_object (in_object_name, in_new_name):
	bpy.ops.object.select_all(action="DESELECT")
	obj = bpy.data.objects[in_object_name]
	obj.name = in_new_name

###############################################################################################
###############################################################################################
def sum_lists(lista,listb):
	listc = []
	if len(listb) > len(lista):
		for mm in listb:
			listc.append(mm)
		for x in range(len(lista)):
			listc[x] += lista[x]
	else:
		for mm in lista:
			listc.append(mm)
		for x in range(len(listb)):
			listc[x] += listb[x]
	print("sum_lists ", lista, listb, listc)
	return listc

