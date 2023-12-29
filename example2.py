#----------------------------------------------------------
# File objects.py
#----------------------------------------------------------
import bpy
import mathutils
from mathutils import Vector
import fnmatch

#----------------------------------------------------------
def Move2Zero():

    obj_objects = [obj for obj in scn.objects if fnmatch.fnmatchcase(obj.name, "*Bulb*")]

    row=1
    col=1

    for obj in obj_objects:
        print (obj.name)
        obj.animation_data_clear()
        bpy.context.scene.frame_current = 1
        obj.location = (row*-.1, col*-.11, 0.05)
        obj.rotation_euler = (-90, 45, 0)
        obj.keyframe_insert(data_path="location", frame=1.00)
        bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')

        #bpy.context.scene.frame_current = 10
        obj.location = (row*-.1, col*-.11, 0.20)
        obj.rotation_euler = (-90, 45, 0)
        obj.keyframe_insert(data_path="location", frame=10.00)
        bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')

        obj.location = (row*-.2, col*-.51, 0.40)
        obj.rotation_euler = (0, 0, 0)
        obj.keyframe_insert(data_path="location", frame=40.00)
        bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')

        #bpy.ops.anim.keyframe_insert_menu(type='BUILTIN_KSI_LocRot')
        col += 1
        if col >= 6:
            col = 1
            row += 1

#----------------------------------------------------------
def CopyBulb(inName, inLocation, inFrame):

    bpy.ops.object.select_all(action="DESELECT")
    bpy.ops.object.select_pattern(pattern=inName)
    bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}
      , TRANSFORM_OT_translate={"value":(0, 0, 0)
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

# prepare a scene
scn = bpy.context.scene
scn.frame_start = 1
scn.frame_end = 201

# create the material
mat = bpy.data.materials.new('MaterialName')
mat.diffuse_color = (0.1, 0.0, 0.7)
mat.diffuse_shader = 'LAMBERT'
mat.diffuse_intensity = 1.0

# get all selected objects
# obj_objects = bpy.context.selected_objects[:]
# iterate through seleted objects

#for obj in obj_objects:
#    # print the name of the current obj
#    print (obj.name)

Move2Zero()
print ("Zeroed")
bpy.ops.wm.save_as_mainfile(filepath="example.blend" %(cwd, output_blend))

"""
CopyBulb("Bulb_Blue"   , (1.2, 1.2, 0))
CopyBulb("Bulb_Blue"   , (1.2, 1.3, 0))
CopyBulb("Bulb_Blue"   , (1.2, 1.1, 0))
CopyBulb("Bulb_Blue"   , (1.2, 1.4, 0))
CopyBulb("Bulb_Blue"   , (1.2, 1.5, 0))
CopyBulb("Bulb_Red"    , (1.4, 1.1, 0))
CopyBulb("Bulb_Red"    , (1.4, 1.2, 0))
CopyBulb("Bulb_Red"    , (1.4, 1.3, 0))
CopyBulb("Bulb_Red"    , (1.4, 1.1, 0))
CopyBulb("Bulb_Red"    , (1.4, 1.4, 0))
CopyBulb("Bulb_Red"    , (1.4, 1.5, 0))

bpy.context.scene.frame_current = 10
bpy.ops.transform.translate(value=(0, 0, 2.05668), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
bpy.ops.transform.translate(value=(0, 0.487778, 0), constraint_axis=(False, True, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
bpy.ops.transform.translate(value=(0.640833, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True)
bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
"""

