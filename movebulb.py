#----------------------------------------------------------
# File objects.py
#----------------------------------------------------------
import bpy
import mathutils
from mathutils import Vector
import fnmatch
import os
import math
##########################################################################################
##########################################################################################

locations = [ (-3.85, 0.10, 1.76) , (-3.89, 0.09, 1.76) , (-3.93, 0.06, 1.76) , (-3.95, 0.02, 1.76)
    , (-3.95, -0.02, 1.76) , (-3.93, -0.06, 1.76) , (-3.89, -0.09, 1.76) , (-3.85, -0.10, 1.76)
    , (-3.81, -0.09, 1.76) , (-3.77, -0.06, 1.76) , (-3.75, -0.02, 1.76) , (-3.75, 0.02, 1.76)
    , (-3.77, 0.06, 1.76) , (-3.81, 0.09, 1.76) , (-3.85, 0.20, 1.41) , (-3.97, 0.16, 1.41)
    , (-4.04, 0.06, 1.41) , (-4.04, -0.06, 1.41) , (-3.97, -0.16, 1.41) , (-3.85, -0.20, 1.41)
    , (-3.73, -0.16, 1.41) , (-3.66, -0.06, 1.41) , (-3.66, 0.06, 1.41) , (-3.73, 0.16, 1.41)
    , (-3.85, 0.30, 1.06) , (-4.06, 0.21, 1.06) , (-4.15, -0.00, 1.06) , (-4.06, -0.21, 1.06)
    , (-3.85, -0.30, 1.06) , (-3.64, -0.21, 1.06) , (-3.55, 0.00, 1.06) , (-3.64, 0.21, 1.06)
    , (-3.85, 0.40, 0.71) , (-4.23, 0.12, 0.71) , (-4.09, -0.32, 0.71) , (-3.61, -0.32, 0.71)
    , (-3.47, 0.12, 0.71) , (-3.85, 0.50, 0.36) , (-4.28, -0.25, 0.36) , (-3.42, -0.25, 0.36)
  ]


#----------------------------------------------------------
def clearscreen():
  #print
  absolutely_unused_variable = os.system("cls")



#----------------------------------------------------------
def loadImage(inName, imgName):

    bpy.ops.object.select_all(action="DESELECT")
    bpy.ops.object.select_pattern(pattern=inName)

    img = bpy.data.add_image(imgName)
    tex = bpy.data.textures.new('TexName')
    tex.type = 'IMAGE' 
    print("Recast", tex, tex.type)
    tex = tex.recast_type()
    print("Done", tex, tex.type)
    tex.image = img
    mat = bpy.data.materials.new('MatName')
    mat.add_texture(texture = tex, texture_coordinates = 'ORCO', map_to = 'COLOR') 
    ob = bpy.context.object
    bpy.ops.object.material_slot_remove()
    me = ob.data
    me.add_material(mat)
    return

#----------------------------------------------------------
def Deg2Rad(inX,inY,inZ):
    return (math.pi*inX/180,math.pi*inY/180,math.pi*inZ/180)
#----------------------------------------------------------
def MoveCamera():

    obj_objects = [obj for obj in scn.objects if fnmatch.fnmatchcase(obj.name, "Camera")]

    row=1
    col=1
    print (Deg2Rad(90,79,0))
    for obj in obj_objects:
        obj.animation_data_clear()
        SetObjFrame(obj, (-.64,-.33,5), Deg2Rad(0,0,0), (1,1,1), 1)
        SetObjFrame(obj, (3.5,4.35,3.5), Deg2Rad(83,0,108), (1,1,1), 30)
        SetObjFrame(obj, (6,1,5), Deg2Rad(69,2,97), (1,1,1), 80)
        SetObjFrame(obj, (-1.11,-.75,0.95), Deg2Rad(88,.2,77), (1,1,1), 150)

#----------------------------------------------------------
def SetObjFrame(inObj, inLoc, inRot, inScale, inFrame):
        inObj.scale = inScale
        inObj.location = inLoc
        inObj.rotation_euler = inRot
        inObj.keyframe_insert(data_path="location", frame=inFrame)
        inObj.keyframe_insert(data_path="rotation_euler", frame=inFrame)
        inObj.keyframe_insert(data_path="scale", frame=inFrame)

#----------------------------------------------------------
def Move2Zero():

    obj_objects = [obj for obj in scn.objects if fnmatch.fnmatchcase(obj.name, "*Bulb*")]
    print ("The number of bulbs = %d" %len(obj_objects))
    row=1
    col=1
    counter=0
    for obj in obj_objects:
        # print the name of the current obj
        obj.animation_data_clear()
        
        SetObjFrame(obj, (row*-.1, col*-.11, 0.05), Deg2Rad(-90,45,0), (.008,.008,.008), 1)
        SetObjFrame(obj, (row*-.1, col*-.11, 0.05), Deg2Rad(-90,45,0), (.008,.008,.008), 30)
        SetObjFrame(obj, locations[counter], Deg2Rad(0,0,245), (.008,.008,.008), 100)
        counter += 1
        col += 1
        if col >= 6:
            col = 1
            row += 1

#----------------------------------------------------------
def CopyBulb(inName, inLocation, inFrame):
     
    bpy.ops.object.select_all(action="DESELECT")
    bpy.ops.object.select_pattern(pattern=inName)
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}
      , TRANSFORM_OT_translate={"value":(0,0,0)
      , "constraint_axis":(False, False, False)
      , "constraint_orientation":'GLOBAL'
      , "mirror":False
      , "proportional":'DISABLED'
      , "proportional_edit_falloff":'SMOOTH'
      , "proportional_size":1
      , "snap":False
      , "snap_target":'CLOSEST'
      , "snap_point":(0, 0, 0)
      , "snap_align":False
      , "snap_normal":(0, 0, 0)
      , "gpencil_strokes":False
      , "texture_space":False
      , "remove_on_cancel":False
      , "release_confirm":False})

    bpy.context.scene.frame_set(frame=0)
    bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocRot')

    bpy.ops.transform.translate(value=inLocation
        , constraint_axis=(False, False, False)
        , constraint_orientation='GLOBAL'
        , mirror=False
        , proportional='DISABLED'
        , proportional_edit_falloff='SMOOTH'
        , proportional_size=1
        , release_confirm=True)

    bpy.context.scene.frame_set(frame=inFrame)
    bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocRot')
    bpy.ops.object.select_all(action="DESELECT")

#----------------------------------------------------------
clearscreen()
# prepare a scene
scn = bpy.context.scene
scn.frame_start = 1
scn.frame_end = 201


# create the material
mat = bpy.data.materials.new('MaterialName')
mat.diffuse_color = (0.1,0.0,0.7)
mat.diffuse_shader = 'LAMBERT'
mat.diffuse_intensity = 1.0

Move2Zero()
MoveCamera()
print ("Moved")

loadImage(inName, imgName)

loadImage('Bulb001','/blender/colors.png')
