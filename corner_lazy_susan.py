
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
#shelf_thickness = (2.54*5)/16
shelf_thickness = 5/16
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

verts.append(([0,0,0]))                  # index 0
verts.append(([24,0,0]))                 # index 1
verts.append(([33.16, -9.16,0]))         # index 2
verts.append(([33.16,-33.16,0]))         # index 3
verts.append(([12,-33.16, 0]))           # index 4
verts.append(([12,-21.16, 0]))           # index 5
verts.append(([0,-21.16, 0]))            # index 6

rng = len(verts)
for foo in range(rng):
	verts.append((sum_lists(verts[foo],[0,0,34.75])))

if False:
	for foo in range(len(verts)):
		add_text('t%d' %foo, str(foo), verts[foo], SCALE=2)

if True:
	print("\n\n\n")
	print("Starts :", verts[0], verts[7])
	print("\n\n\n")
	build_side("bottom", verts, [0,1,2,3,4,5,6], -shelf_thickness)
	move_object("bottom", (0,0,3.5))
	build_side("corner_lazy_susan", verts, [7,8,9,10,11,12,13], shelf_thickness)
	build_side("side1", verts, [0,1,8,7], shelf_thickness)
	build_side("side2", verts, [1,2,9,8], shelf_thickness)
	build_side("side3", verts, [2,3,10, 9], shelf_thickness)
	build_side("side4", verts, [3,4,11,10], shelf_thickness)
	build_side("side5", verts, [0,6,13,7], shelf_thickness)

	#door_size = [11.25, 5/8, 41.75]
	#door_pos = [0,0,0]

	#build_cube("door_1", ([0,0,0]), (door_size))
	#set_material('door_1', base_cabinet_material)
	#build_drawer_handle("handle_1")
	#rotate_object("handle_1", (0, 90, 180))
	#move_object("handle_1", ([5,0,0]))
	#join_objects_by_name(["handle_1", "door_1"])
	#set_door_origin("door_1", "left")
	#rotate_object("door_1", (0,0,-45))
	#move_object("door_1", ([12.5,-.333,21]))
  #
	#build_cube("door_2", ([0,0,0]), (door_size))
	#set_material('door_2', base_cabinet_material)
	#build_drawer_handle("handle_2")
	#rotate_object("handle_2", (0, 90, 180))
	#move_object("handle_2", ([-5,0,0]))
	#join_objects_by_name(["handle_2", "door_2"])
	#set_door_origin("door_2", "right")
	#rotate_object("door_2", (0,0,45))
  #
	#move_object("door_2", ([29,16.666,21]))

	join_objects_by_name(["bottom","side1","side2","side3","side4", "side5", "corner_lazy_susan"])

	base_cabinet_material = define_material_hsv ("base_cabinet_material",  1.0, 1.0, 1.0,1.0)
	set_material('corner_lazy_susan', base_cabinet_material)

if True:
	build_cylinder("ls_shaft",(0,0,0), (1,1,34))
	build_cylinder("ls_shelf1", (0,0,0), (20,20,1))
	build_cylinder("ls_shelf2", (0,0,0), (20,20,1))
	move_object("ls_shaft",(20,-13,17))
	move_object("ls_shelf1",(20,-13,15))
	move_object("ls_shelf2",(20,-13,25))
	join_objects_by_name(["ls_shelf1","ls_shelf2","ls_shaft"])

	ls_material = define_material_hsv ("ls_material",  .02, 0.3, 0.5,1.0)
	set_material('ls_shaft', ls_material)

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
	#scale_object("corner_lazy_susan", (2.54,2.54,2.54))
	join_objects_by_name(["ls_shaft", "corner_lazy_susan"])
	print ("\n\n\n%s/%s.blend\n\n\n" %(cwd,output_blend))
	bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))
	#bpy.ops.export_mesh.stl(filepath="%s/%s.stl" %(cwd,output_blend))
	bpy.ops.export_scene.obj(filepath="%s/%s.obj" %(cwd,output_blend))

#BMESH?

