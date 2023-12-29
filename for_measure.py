
from greg_blender import *
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

C = bpy.context

output_blend =  pathlib.PurePath(__file__).stem

delete_all_objects()

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

verts = []
faces = []
edges = []

verts.append([0,0,0])  # index 0
verts.append([12.5,0,0])  # index 1
verts.append([29,30-12.5,0])  # index 2
verts.append([29,30,0])  # index 3
verts.append([0,30,0])  # index 4
verts.append([0,0,42])  # index 5
verts.append([12.5,0,42])  # index 6
verts.append([29,30-12.5,42])  # index 7
verts.append([29,30,42])  # index 8
verts.append([0,30,42])  # index 9

if False:
	add_text('t%d' %0, '%d' %0, [0,0,0], SCALE=2)
	add_text('t%d' %1, '%d' %1, [12.5,0,0], SCALE=2)
	add_text('t%d' %2, '%d' %2, [29,30-12.5,0], SCALE=2)
	add_text('t%d' %3, '%d' %3, [29,30,0], SCALE=2)
	add_text('t%d' %4, '%d' %4, [0,30,0], SCALE=2)
	add_text('t%d' %5, '%d' %5, [0,0,42], SCALE=2)
	add_text('t%d' %6, '%d' %6, [12.5,0,42], SCALE=2)
	add_text('t%d' %7, '%d' %7, [29,30-12.5,42], SCALE=2)

if True:

	faces.append([0,1,2,3,4])
	faces.append([5, 6, 7, 8, 9])
	faces.append([0,1,6,5])
	faces.append([2,3,8,7])
	faces.append([3,4,9,8])
	faces.append([0,4,9,5])

if True:
	for foo in range(len(verts)):
		add_text('t%d' %foo, '%d' %foo, verts[foo], SCALE=2)

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

	#bpy.ops.object.modifier_add(type='SOLIDIFY')
	#bpy.context.object.modifiers["Solidify"].thickness = 5/8
	#bpy.ops.object.modifier_apply(modifier="Solidify")

	#mod_skin = obj.modifiers.new('Skin', 'SKIN')

if True:
	print ("\n\n\n%s/%s.blend\n\n\n" %(cwd,output_blend))
	bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))
	#bpy.ops.export_mesh.stl(filepath="%s/%s.stl" %(cwd,output_blend))
	#bpy.ops.export_scene.obj(filepath="%s/%s.obj" %(cwd,output_blend))

#BMESH?

