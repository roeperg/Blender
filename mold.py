
from greg_blender import *
import bpy
import random
import pathlib
import os
import math
cwd = os. getcwd()

C = bpy.context

output_blend =  pathlib.PurePath(__file__).stem

###############################################################################################
###############################################################################################
def newMaterial(id):
	mat = bpy.data.materials.get(id)
	if mat is None:
		mat = bpy.data.materials.new(name=id)
	mat.use_nodes = True
	if mat.node_tree:
		mat.node_tree.links.clear()
		mat.node_tree.nodes.clear()
	return mat

###############################################################################################
###############################################################################################
def newShader(id, type, r, g, b):

	mat = newMaterial(id)

	nodes = mat.node_tree.nodes
	links = mat.node_tree.links
	output = nodes.new(type='ShaderNodeOutputMaterial')

	if type == "diffuse":
		shader = nodes.new(type='ShaderNodeBsdfDiffuse')
		nodes["Diffuse BSDF"].inputs[0].default_value = (r, g, b, 1)

	elif type == "emission":
		shader = nodes.new(type='ShaderNodeEmission')
		nodes["Emission"].inputs[0].default_value = (r, g, b, 1)
		nodes["Emission"].inputs[1].default_value = 1

	elif type == "glossy":
		shader = nodes.new(type='ShaderNodeBsdfGlossy')
		nodes["Glossy BSDF"].inputs[0].default_value = (r, g, b, 1)
		nodes["Glossy BSDF"].inputs[1].default_value = 0

	links.new(shader.outputs[0], output.inputs[0])

	return mat

###############################################################################################
###############################################################################################
def get_y_from_x(radius, x):
	l2 = radius*radius
	x2 = x * x
	return (x,math.sqrt(l2-x2))

###############################################################################################
###############################################################################################
def add_text(in_name, in_text, in_location, FONT="CENTURY", bevel=0.002, SCALE=(5,5,5)):

	in_text = in_text.strip()
	print("GREGGO")
	fnt = bpy.data.fonts.load(f'c:/Windows/Fonts/{FONT}.ttf')

	bpy.ops.object.text_add(location=in_location)
	ob=bpy.context.object
	sd=	bpy.context
	ops = bpy.ops.object

	ob.data.body = str(in_text)
	ob.data.space_character = 1.0
	ob.data.align_x = 'CENTER'
	ob.data.align_y = 'CENTER'
	ob.data.font = fnt

	ob.name = in_name

	print(ob.dimensions.x)
	print(ob.dimensions.y)
	print(ob.dimensions.z)

	ob.data.extrude = .25
	ob.data.bevel_depth = bevel
	if True:
		ops.convert(target='MESH')
		ops.modifier_add(type='DECIMATE')
		sd.object.modifiers["Decimate"].decimate_type = 'DISSOLVE'
		ops.modifier_apply(modifier="Decimate")
		rotate_object(ob.name, (0,180,0))
	scale_object(ob.name, SCALE)

###############################################################################################
###############################################################################################
def text_cut(inbase, inname,intext,inlocation,bevel=.04, SCALE=(5,5,5)):
	add_text(inname,intext,inlocation,bevel,SCALE)
	boolean_difference(inbase, inname, SOLVER='FAST')
	remove_object(inname)

###############################################################################################
###############################################################################################
def processit(thisfont):
	delete_all_objects()
	#join_list = ["Austin"]  # ["upper_curve", "lower_curve"]

	if True:
		print(f"\n\n\n>>>>>>>>>>>>>>>>>>	 Trying {thisfont}\n\n\n")
		add_text("Alpha", "Sara", ( 0,0,0), SCALE=(45,45,60), FONT=thisfont)
		build_cube("form", ( 0,0,2), (85,45,8))
		mat = newShader("Shader1", "diffuse", 1, 0.2141388, 0.2204449)
		build_cube("base", ( 0,0,-1.5), (85,45,3))
		ob=bpy.context.object
		ob.data.materials.append(mat)

		boolean_difference("form", "Alpha")
		remove_object("Alpha")
	#join_objects_by_name(join_list)
	for area in bpy.context.screen.areas:
			if area.type == 'VIEW_3D':
				space = area.spaces.active
				if space.type == 'VIEW_3D':
					space.shading.type = 'MATERIAL'

processit("BAUHS93")
bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))
bpy.ops.export_mesh.stl(filepath="%s/%s.stl" %(cwd,output_blend))

#  .ttf
#	fnt = bpy.data.fonts.load('c:/Windows/Fonts/Raybent Mango.ttf')
#	fnt = bpy.data.fonts.load('c:/Windows/Fonts/comici.ttf')

"""
 1  ARIALNB
 6 is really cute
32 BROADW
50 Curly
"""

