
from greg_blender import *
import bpy
import random
import pathlib
import os
import math
import types
from mathutils import Vector

cwd = os. getcwd()
from inspect import getmembers, isfunction
from mathutils import Vector

"""
obj = bpy.context.object
object_details = bounds(obj)

a = object_details.z.max
b = object_details.z.min
c = object_details.z.distance

print(a, b, c)
"""

cooktop_material = define_material_hsv ("cooktop_material",  0.00399625, 0.00467182, 0.00393842, 1, METALLIC=0.50)
burner_material = define_material_hsv ("burner_material",    .86, .300, .220, 1.0)

C = bpy.context

output_blend =  pathlib.PurePath(__file__).stem

CONVERT=False

###############################################################################################
###############################################################################################
def to_sh3d_dim(invalue):
    # function to convert inches to millimeter equivalent of Blender/Sweet Home 3D
    output = []
    if CONVERT:
        for foo in invalue:
            output.append(foo*2.54)
        return output
    return invalue

###############################################################################################
###############################################################################################
def add_text(in_name, in_text, in_location, bevel=0.002, SCALE=(5,5,5)):

    in_text = in_text.strip()
    bpy.data.fonts.load(r"C:\Windows\Fonts\PLAYBILL.TTF")
    # bpy.ops.font.open(filepath=r"C:\Windows\Fonts\ITCKRIST.TTF")
    bpy.ops.object.text_add(location=in_location)
    ob=bpy.context.object
    sd=    bpy.context

    ob.data.body = str(in_text)
    ob.data.space_character = 1.4

    ob.name = in_name
    ob.data.extrude = .25
    ob.data.bevel_depth = bevel
    bpy.ops.object.convert(target='MESH')

    scale_object(ob.name, SCALE)

###############################################################################################
###############################################################################################
def set_3d_cursor(LOCATION=(0,0,0)):
    saved_location = C.scene.cursor.location.copy()
    C.scene.cursor.location = LOCATION
    print(saved_location)
    return saved_location

###############################################################################################
###############################################################################################
def build_cooktop(in_name):
    # print("build_cooktop ", in_name)
    # print(to_sh3d_dim((38,23,1)))
    build_cube(in_name, to_sh3d_dim((0,0,0)) , to_sh3d_dim((38,23,1)))
    set_material(in_name, cooktop_material)
    build_cylinder("main_burner", to_sh3d_dim((0,5,.25)), to_sh3d_dim((10,10,.75)), VERTICES=256)
    build_cylinder("small_burner_1", to_sh3d_dim((10,-4,.25)), to_sh3d_dim((5,5,.75)), VERTICES=256)
    set_material("main_burner", burner_material)
    set_material("small_burner_1", burner_material)

###############################################################################################
###############################################################################################

# delete_all_objects()

build_cooktop("my_cooktop")

move_object("Camera", (20.3809, -24.2674, 7.57636 ))
remove_object("Cube")

print ("\n\n\n%s/%s.blend\n\n\n" %(cwd,output_blend))
bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd,output_blend))
# bpy.ops.export_mesh.stl(filepath="%s/%s.stl" %(cwd,output_blend))
bpy.ops.export_scene.obj(filepath="%s/%s.obj" %(cwd,output_blend))
# remove_object("cutout")

bpy.context.object.active_material.metallic = 0.5
bpy.context.object.active_material.diffuse_color = (0.00399625, 0.00467182, 0.00393842, 1)

