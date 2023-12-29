
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
def add_text(in_name, in_text, in_location, bevel=0.002):

  in_text = in_text.strip()
  bpy.ops.object.text_add(location=in_location)
  ob=bpy.context.object
  ob.data.body = str(in_text)
  ob.data.space_character = 1.4

  ob.name = in_name
  ob.data.extrude = .1
  ob.data.bevel_depth = bevel
  bpy.ops.object.convert(target='MESH')

  scale_object(ob.name, (5,5,5))

###############################################################################################
###############################################################################################

if True:
	verts = []    # x,y,z
	edges = []    # p1,p2
	faces = []    # p1 - pN

	verts.append([    # index 0
		0.0,   # x
		0.0,   # y
		0.0,   # z
	])
	verts.append([30.0,0.0,0.0,]) # index 1
	verts.append([0.0,29.0,0.0,]) # index 2
	verts.append([0,0,96])    # index 3
	verts.append([30,0,96])    # index 4
	verts.append([0,29,96])    # index 5

	#for foo in range(len(verts)):
	#	add_text("t%d" %foo, "%d" %foo, verts[foo])

	#edges.append([0, 1])
	#edges.append([1, 2])
	#edges.append([0, 2])
	#edges.append([3, 4])
	#edges.append([4, 5])

	print(edges)

	faces.append([0,1,2])
	faces.append([3, 4, 5])
	faces.append([1,2,5,4])
	faces.append([0,2,5,3])
	faces.append([0,3,4,1])

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

	#mod_skin = obj.modifiers.new('Skin', 'SKIN')

if True:
	print ("\n\n\n%s/%s.blend\n\n\n" %(cwd,output_blend))
	bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))
	#bpy.ops.export_mesh.stl(filepath="%s/%s.stl" %(cwd,output_blend))
	#bpy.ops.export_scene.obj(filepath="%s/%s.obj" %(cwd,output_blend))

#BMESH?

