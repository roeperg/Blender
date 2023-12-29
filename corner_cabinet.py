
from greg_cabinet_stuff import *
from math import *
from mathutils import Vector
import bpy
import math
import mathutils
import numpy
import os
import pathlib
import random
import sys
import types

cwd = os. getcwd()

verts = []
faces = []
edges = []
shelf_thickness = (2.54*5)/16
C = bpy.context

output_blend =  pathlib.PurePath(__file__).stem

delete_all_objects()

###############################################################################################
###############################################################################################
def add_text(in_name, in_text, in_location, bevel=0.002, SCALE=5):

  in_text = in_text.strip()
  bpy.ops.object.text_add(location=in_location)
  ob=bpy.context.object
  ob.data.body = str(in_text)
  ob.data.space_character = 1.4

  ob.name = in_name
  ob.data.extrude = .1
  ob.data.bevel_depth = bevel
  bpy.ops.object.convert(target='MESH')

  scale_object(ob.name, (SCALE,SCALE,SCALE))

###############################################################################################
###############################################################################################
def build_side(in_name, vertices, face, offset):
	print(in_name)
	print(vertices)
	print(face)
	print(tuple(map(len, [face])))
	mesh = bpy.data.meshes.new(in_name)
	obj = bpy.data.objects.new(in_name, mesh)
	print("collection length = ", len(bpy.data.collections))
	col = bpy.data.collections[0]
	col.objects.link(obj)
	bpy.context.view_layer.objects.active = obj
	print(face)
	mesh.from_pydata(vertices, edges, [face])

	bpy.ops.object.modifier_add(type='SOLIDIFY')
	bpy.context.object.modifiers["Solidify"].thickness = offset
	bpy.ops.object.modifier_apply(modifier="Solidify")

###############################################################################################
###############################################################################################
def parallel(vertice, offsets):
	print("Input vert", vertice)
	outvert = []
	for foo in range(len(vertice)):
		outvert.append(vertice[foo] + offsets[foo])
	print("Output vert", outvert)
	return outvert

###############################################################################################
###############################################################################################

verts.append(to_sh3d_dim([0,0,0]))  # index 0
verts.append(to_sh3d_dim([12.5,0,0]))  # index 1
verts.append(to_sh3d_dim([29,17.5,0]))  # index 2
verts.append(to_sh3d_dim([29,30,0]))  # index 3
verts.append(to_sh3d_dim([0,30,0]))  # index 4
verts.append(to_sh3d_dim([0,0,42]))  # index 5
verts.append(to_sh3d_dim([12.5,0,42]))  # index 6
verts.append(to_sh3d_dim([29,17.5,42]))  # index 7
verts.append(to_sh3d_dim([29,30,42]))  # index 8
verts.append(to_sh3d_dim([0,30,42]))  # index 9

if False:
	add_text('t%d' %0, '%d' %0,to_sh3d_dim( [0,0,0]), SCALE=2)
	add_text('t%d' %1, '%d' %1,to_sh3d_dim( [12.5,0,0]), SCALE=2)
	add_text('t%d' %2, '%d' %2,to_sh3d_dim( [29,17.5,0]), SCALE=2)
	add_text('t%d' %3, '%d' %3,to_sh3d_dim( [29,30,0]), SCALE=2)
	add_text('t%d' %4, '%d' %4,to_sh3d_dim( [0,30,0]), SCALE=2)
	add_text('t%d' %5, '%d' %5,to_sh3d_dim( [0,0,42]), SCALE=2)
	add_text('t%d' %6, '%d' %6,to_sh3d_dim( [12.5,0,42]), SCALE=2)
	add_text('t%d' %7, '%d' %7,to_sh3d_dim( [29,17.5,42]), SCALE=2)
	add_text('t%d' %8, '%d' %8,to_sh3d_dim( [29,30,42]), SCALE=2)
	add_text('t%d' %9, '%d' %9,to_sh3d_dim( [0,30,42]), SCALE=2)

if False:

	faces.append([0,1,2,3,4])
	faces.append([5, 6, 7, 8, 9])
	faces.append([0,1,6,5])
	faces.append([2,3,8,7])
	faces.append([3,4,9,8])
	faces.append([0,4,9,5])

if True:
	build_side("bottom", verts, [0,1,2,3,4], -shelf_thickness)
	build_side("corner_cabinet", verts, [5, 6, 7, 8, 9], shelf_thickness)
	build_side("side1", verts, [0,1,6,5], shelf_thickness)
	build_side("side2", verts, [2,3,8,7], shelf_thickness)
	build_side("side3", verts, [3,4,9,8], shelf_thickness)
	build_side("side4", verts, [0,4,9,5], -shelf_thickness)

	door_size = [11.25, 5/8, 41.75]
	door_pos = [0,0,0]

	build_cube("door_1", to_sh3d_dim([0,0,0]), to_sh3d_dim(door_size))
	set_material('door_1', base_cabinet_material)
	build_drawer_handle("handle_1")
	rotate_object("handle_1", (0, 90, 180))
	move_object("handle_1", to_sh3d_dim([5,0,0]))
	join_objects_by_name(["handle_1", "door_1"])
	set_door_origin("door_1", "left")
	rotate_object("door_1", (0,0,-45))
	move_object("door_1", to_sh3d_dim([12.5,-.333,21]))

	build_cube("door_2", to_sh3d_dim([0,0,0]), to_sh3d_dim(door_size))
	set_material('door_2', base_cabinet_material)
	build_drawer_handle("handle_2")
	rotate_object("handle_2", (0, 90, 180))
	move_object("handle_2", to_sh3d_dim([-5,0,0]))
	join_objects_by_name(["handle_2", "door_2"])
	set_door_origin("door_2", "right")
	rotate_object("door_2", (0,0,45))

	move_object("door_2", to_sh3d_dim([29,16.666,21]))

	#join_objects_by_name(["bottom","side1","side2","side3","side4","door_1", "corner_cabinet"])

if False:
	for foo in range(len(verts)):
		add_text('t%d' %foo, '%d' %foo, verts[foo], SCALE=2)

if False:
	name = "greggo"
	mesh = bpy.data.meshes.new(name)
	obj = bpy.data.objects.new(name, mesh)
	print("collection length = ", len(bpy.data.collections))
	col = bpy.data.collections[0]
	print(col)
	col.objects.link(obj)
	bpy.context.view_layer.objects.active = obj
	mesh.from_pydata(verts, edges, faces)
	print(mesh)

	bpy.ops.object.modifier_add(type='SOLIDIFY')
	bpy.context.object.modifiers["Solidify"].thickness = shelf_thickness
	bpy.ops.object.modifier_apply(modifier="Solidify")

	#mod_skin = obj.modifiers.new('Skin', 'SKIN')

if True:
	print ("\n\n\n%s/%s.blend\n\n\n" %(cwd,output_blend))
	bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))
	#bpy.ops.export_mesh.stl(filepath="%s/%s.stl" %(cwd,output_blend))
	bpy.ops.export_scene.obj(filepath="%s/%s.obj" %(cwd,output_blend))

#BMESH?

