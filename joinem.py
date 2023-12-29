
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

###############################################################################################
###############################################################################################
def build_extruded_plane(
								 vertex_tuples                      # list of vertexes tuples.  3 numbers (x,y,z) for each vertex.
							 , edge_list                          # list of point offsets for each segment
							 , extrude_tuple                      # 3 member tuple for extrusion
							 , in_object_name ):

	print ("Vertices and edges (straightforward)")
	vertex_point_index_for_segments = []
	vertex_list = []

	for foo in vertex_tuples:
		for bar in foo:
			vertex_list.append(float(bar))

	print (vertex_list)
	for i in range(len(vertex_list)):
		print (i)
		if i%3 == 0:
			vertex_point_index_for_segments.append(i/3)

	vertices = numpy.array(vertex_list, dtype=numpy.float32)
	num_vertices = vertices.shape[0] // 3
	print ("Polygons are defined in loops.")

	vertex_index = numpy.array(vertex_point_index_for_segments, dtype=numpy.int32)
	print ("For each polygon the start of its vertex indices in the vertex_index array")
	loop_start = numpy.array([0], dtype=numpy.int32)
	print ("Length of each polygon in number of vertices")
	print("greggo ...", len(vertex_list))
	loop_total = numpy.array([num_vertices], dtype=numpy.int32)
	edges = numpy.array(edge_list, dtype=numpy.int32)
	num_edges = edges.shape[0] // 2

	num_vertex_indices = vertex_index.shape[0]
	num_loops = loop_start.shape[0]

	print ("Create mesh object based on the arrays above")

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

	print ("Create Object whose Object Data is our new mesh")
	obj = bpy.data.objects.new('created object', mesh)

	print ("Add *Object* to the scene, not the mesh")
	scene = bpy.context.scene
	scene.collection.objects.link(obj)

	# Select the new object and make it active
	bpy.ops.object.select_all(action='DESELECT')
	obj.select_set(True)
	bpy.context.view_layer.objects.active = obj

	extrude_plane(extrude_tuple)

	obj = bpy.context.active_object
	obj.name = in_object_name
	print ("location", obj.location)
	print ("changing origin")
	bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')

#   join_objects_by_name(["addme","kars name" ])
shape_tuples = [
(-36, -27.5, 0),
(8.9,-8.9,0),
( 6.5,-12,0),
(45,.87,0),
(-1,-18,0),
(1.9,-14,0),
		]

edges = [
			1, 2,
			2, 3,
			3, 4,
			4, 5,
			5, 1,
		]

build_extruded_plane(
									 shape_tuples                    # list of vertexes tuples.  3 numbers (x,y,z) for each vertex.
								 , edges                            # list of point offsets for each segment
								 , (0,0,2)                     # 3 member tuple for extrusion
								 , "bolt" )

bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))

(-36, -27.5, 0),
(8.9,-8.9,0),
( 6.5,-12,0),
(45,.87,0),
(-1,-18,0),

