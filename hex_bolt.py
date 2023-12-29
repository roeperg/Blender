#####################################################################################
#
#    PLACE HEX
#
#####################################################################################
# 23.3709135
# 41.667
import os
import bpy
import bmesh
from bpy.types import Operator
from bpy_extras.object_utils import AddObjectHelper, object_data_add
from mathutils import Vector

##########################################################################################
##########################################################################################
def clearscreen():
  #print
  absolutely_unused_variable = os.system("cls")

##########################################################################################
##########################################################################################
def modifiy_difference(target, opObj):
	'''subtract opObj from the target'''

	# Deselect All
	bpy.ops.object.select_all(action='DESELECT')

	# Select the new object.
	target.selected = True
	bpy.context.scene.objects.active = target

	# Add a modifier
	bpy.ops.object.modifier_add(type='BOOLEAN')

	mod = target.modifiers
	mod[0].name = "SubEmUp"
	mod[0].object = opObj
	mod[0].operation = 'DIFFERENCE'

	# Apply modifier
	bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod[0].name)

##########################################################################################
##########################################################################################
def modifiy_union(target, opObj):
	'''subtract opObj from the target'''

	# Deselect All
	bpy.ops.object.select_all(action='DESELECT')

	# Select the new object.
	target.selected = True
	bpy.context.scene.objects.active = target

	# Add a modifier
	bpy.ops.object.modifier_add(type='BOOLEAN')

	mod = target.modifiers
	mod[0].name = "SubEmUp"
	mod[0].object = opObj
	mod[0].operation = 'UNION'

	# Apply modifier
	bpy.ops.object.modifier_apply(apply_as='DATA', modifier=mod[0].name)
	bpy.ops.object.select_all(action='DESELECT')

#####################################################################################
#####################################################################################
def bolt_recess(bolt_head,bolt_height,length,width,offset, name='Greg'):

    corner_width = bolt_head * 1.154285714

    #scale for inches
    bolt_head = bolt_head*25
    corner_width = corner_width*25
    bolt_height = bolt_height*25
    offset = offset*25
    length = length*25
    width  = width*25

    # add 5%
    #bolt_head = bolt_head*1.05
    #corner_width = corner_width*1.05

    verts = [
    # bottom nut vertices
    Vector((-bolt_head/2,     corner_width/4 , offset )),        #    0
    Vector((     0,     corner_width/2 , offset )),        #    1
    Vector(( bolt_head/2,     corner_width/4 , offset )),        #    2
    Vector(( bolt_head/2, -corner_width/4 , offset )),        #    3
    Vector((     0, -corner_width/2 , offset )),        #    4
    Vector((-bolt_head/2, -corner_width/4 , offset )),        #    5

    # top nut vertices
    Vector((-bolt_head/2,     corner_width/4 , offset+bolt_height )),        #    6
    Vector((     0,     corner_width/2 , offset+bolt_height )),        #    7
    Vector(( bolt_head/2,     corner_width/4 , offset+bolt_height )),        #    8
    Vector(( bolt_head/2, -corner_width/4 , offset+bolt_height )),        #    9
    Vector((     0, -corner_width/2 , offset+bolt_height )),        #    10
    Vector((-bolt_head/2, -corner_width/4 , offset+bolt_height )),        # 11

    # outer bottom vertices
    Vector((-length/2, width/2 , offset )),                # 12
    Vector(( length/2, width/2 , offset )),                # 13
    Vector(( length/2,-width/2 , offset )),                # 14
    Vector((-length/2,-width/2 , offset )),                # 15

    # top bottom vertices
    Vector((-length/2, width/2 , offset+bolt_height )),                # 16
    Vector(( length/2, width/2 , offset+bolt_height )),                # 17
    Vector(( length/2,-width/2 , offset+bolt_height )),                # 18
    Vector((-length/2,-width/2 , offset+bolt_height )),                # 19

    ]

    faces = [
        # internal
        [0,6,11,5],
        [0,6,7,1],
        [7,1,2,8],
        [2,8,9,3],
        [9,3,4,10],
        [4,10,11,5],
        [11,5,0,6],

        # external
        [12,13,17,16],
        [13,14,18,17],
        [18,19,15,14],
        [15,12,16,19],

        # top
        [12,1,0,5,4,15],
        [13,2,12],
        [13,14,3,2],
        [15,3,14],

        # bottom
        [16,7,6,11,10,19],
        [17,8,16],
        [17,18,9,8],
        [19,9,18],
        ]

    edges = []

    mesh = bpy.data.meshes.new(name=name)

    mesh = bpy.data.meshes.new(name)    # add a new mesh
    mesh.from_pydata(verts, edges, faces)
    obj = object_data_add(bpy.context, mesh)

    print (mesh.name)

    return mesh.name

#####################################################################################
#####################################################################################
def base_planes(shaft_size, bolt_height,length,width,offset, name='Greg'):

    #scale for inches
    shaft_size = shaft_size*12.5
    shaft_length = bolt_height*100
    bolt_height = bolt_height*25
    length = length*25
    width  = width*25
    offset = offset*25

    verts = [

    # outer bottom vertices
    Vector((-length/2, width/2 , offset )),            # 0
    Vector(( length/2, width/2 , offset )),            # 1
    Vector(( length/2,-width/2 , offset )),            # 2
    Vector((-length/2,-width/2 , offset )),            # 3

    # top bottom vertices
    Vector((-length/2, width/2 , offset+bolt_height )),            # 4
    Vector(( length/2, width/2 , offset+bolt_height )),            # 5
    Vector(( length/2,-width/2 , offset+bolt_height )),            # 6
    Vector((-length/2,-width/2 , offset+bolt_height )),            # 7

    ]

    faces = [
        [0,1,2,3],
        [4,5,6,7],

        [0,1,5,4],
        [0,3,7,4],
        [1,2,6,5],
        [2,3,7,6],
    ]
    edges = []

    mycyl = bpy.ops.mesh.primitive_cylinder_add(radius=shaft_size, depth=shaft_length
                            , enter_editmode=False, location=(0,0,0)
                            )
    cylobj = bpy.context.object

    mesh = bpy.data.meshes.new(name)    # add a new mesh
    mesh.from_pydata(verts, edges, faces)
    obj = object_data_add(bpy.context, mesh)

    bpy.ops.object.select_all(action='DESELECT')

    if True:
        modifiy_difference(bpy.data.objects[mesh.name], bpy.data.objects[cylobj.name])
        print("cylobj",cylobj.name)
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[cylobj.name].select = True
        bpy.ops.object.delete()
    print (mesh.name)
    return mesh.name

#####################################################################################
#####################################################################################
def hex_bolt(bolt_head,bolt_height,shaft_size, shaft_length, offset, name='Greg'):
    #scale for inches
    corner_width = bolt_head * 1.154285714
    shaft_size = shaft_size*12.5
    shaft_length = shaft_length*12.5

    # scale for blender
    bolt_head = bolt_head*25
    corner_width = corner_width*25
    bolt_height = bolt_height*25
    offset = offset*25

    verts = [
    # bottom nut vertices
    Vector((-bolt_head/2,     corner_width/4 , offset )),        #    0
    Vector((     0,     corner_width/2 , offset )),        #    1
    Vector(( bolt_head/2,     corner_width/4 , offset )),        #    2
    Vector(( bolt_head/2, -corner_width/4 , offset )),    #    3
    Vector((     0, -corner_width/2 , offset )),        #    4
    Vector((-bolt_head/2, -corner_width/4 , offset )),    #    5

    # top nut vertices
    Vector((-bolt_head/2,     corner_width/4 , offset+bolt_height )),        #    6
    Vector((     0,     corner_width/2 , offset+bolt_height )),        #    7
    Vector(( bolt_head/2,     corner_width/4 , offset+bolt_height )),        #    8
    Vector(( bolt_head/2, -corner_width/4 , offset+bolt_height )),    #    9
    Vector((     0, -corner_width/2 , offset+bolt_height )),        #    10
    Vector((-bolt_head/2, -corner_width/4 , offset+bolt_height )),    # 11
    ]

    faces = [
        # internal
        [0,6,11,5],
        [0,6,7,1],
        [7,1,2,8],
        [2,8,9,3],
        [9,3,4,10],
        [4,10,11,5],
        [11,5,0,6],

        # top
        [0,1,2,3,4,5],

        # bottom
        [6,7,8,9,10,11],
        ]

    edges = []

    mycyl = bpy.ops.mesh.primitive_cylinder_add(radius=shaft_size, depth=shaft_length+bolt_height, view_align=False
                            , enter_editmode=False, location=(0,0,shaft_length/2+bolt_height)
                            , layers=(True, False, False, False, False, False, False, False, False
                            , False, False, False, False, False, False, False, False, False, False, False))
    cylobj = bpy.context.object

    mesh = bpy.data.meshes.new(name)    # add a new mesh
    mesh.from_pydata(verts, edges, faces)
    obj = object_data_add(bpy.context, mesh)

    modifiy_union(bpy.data.objects[mesh.name], bpy.data.objects[cylobj.name])

    bpy.ops.object.select_all(action='DESELECT')

    bpy.data.objects[cylobj.name].select = True

    bpy.ops.object.delete()

clearscreen()
print ("Beginning")

basename = "1/2"
bolt_head = 1/2
bolt_height = 0.16
shaft_diameter = 5/16
shaft_length = 1.5
recess_outer_length = 1
recess_outer_width = 1

if True:
    r_name = bolt_recess(bolt_head, bolt_height, recess_outer_length, recess_outer_width, bolt_height, name="%s inch" %basename)
    b_name = base_planes(shaft_diameter, bolt_height, recess_outer_length, recess_outer_width, 0, name="%s inch base" %basename)

    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.join()
    bpy.ops.object.select_all(action='DESELECT')

if False:
    hex_bolt ( bolt_head, bolt_height, shaft_diameter, shaft_length, 0, name="%s inch bolt" %basename)

