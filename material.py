import bpy
from greg_blender import *
import random
import pathlib
import os
import math

cwd = os. getcwd()

C = bpy.context

output_blend =  pathlib.PurePath(__file__).stem

colorcount = 0
colors = []
for h in [0,.1,.2,.3,.4,.5,.6,.7,.8,.9.1]:
	for s in [0,.1,.2,.3,.4,.5,.6,.7,.8,.9.1]:
		for v in [0,.1,.2,.3,.4,.5,.6,.7,.8,.9.1]:
			ob = "cube%d" %colorcount
			colors.append(define_material_hsv ("color%d" %colorcount, h,s,v,1.0)
			build_cube(ob,(colorcount,0,0),(1,1,1))
			set_material(ob, colors[colorcount])

			colorcount += 1
matr = define_material_hsv ("matr", .7,.05,.05,1.0)
greggo = define_material_hsv ("greggo", .4,.9,.2,1.0)
sara = define_material_hsv ("sara", .1,.9,.4,.5)

template_object = bpy.data.objects.get('Cube')
#template_object.material_slots[0].link = 'OBJECT'

template_object.active_material = greggo

build_cube("cabinet",        (5,5,0),(2,2,2))
build_cylinder("cutout", ( 0, -3, 0), (2, 2, 4), VERTICES=128)

set_material('cutout', sara)
set_material('cabinet', greggo)

print ("\n\n\n%s/%s.blend\n\n\n" %(cwd,output_blend))
bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))

