#----------------------------------------------------------
# File objects.py
#----------------------------------------------------------
import bpy
import mathutils
from mathutils import Vector
 
def run():
    # prepare a scene
    scn = bpy.context.scene
    scn.frame_start = 1
    scn.frame_end = 101
    
    # move to frame 17
    bpy.ops.anim.change_frame(frame = 17)
    
    
    # select the created object
    bpy.ops.object.select_name(name="'Cylinder.001'")
    
    # do something with the object. A rotation, in this case
    bpy.ops.transform.rotate(value=(-0.5*pi, ), axis=(-1, 0, 0))
    bpy.ops.transform.location.xyz = (-0.85, 0.10, 0.36)
    
    # create keyframe
    bpy.ops.anim.keyframe_insert_menu(type='Rotation')  

    bpy.data.objects['Cylinder.001'].location.xyz = (.5, 1, 1)
    return
 
if __name__ == "__main__":
    run()
bpy.data.objects['Cylinder.017'].location.xyz = (.5, 1, 1)


##################################################################################
# prepare a scene

# create an object
bpy.ops.object.add(type='MESH')
newObject = bpy.context.object
newObject.name = "MyTriangle"
newMesh = newObject.data
x, y, z = 0, 0, 0
width, depth, height = 1, 1, 0.5
newVerts = [(x,y,z), (x+width,y,z), (x+width,y+depth,z), (x,y+depth,z),
           (x,y,z+height), (x+width,y,z+height), (x+width,y+depth,z+height),
           (x,y+depth,z+height)]
newEdges = []       # creating vertices and faces is sufficient.
newFaces = [(0,1,2,3), (2,3,7,6), (4,5,6,7), (0,3,7,4), (1,2,6,5), (0,1,5,4)]
newMesh.from_pydata(newVerts, newEdges, newFaces)
newMesh.update()

# select the created object
bpy.ops.object.select_name(name="myTriangle")

bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}
  , TRANSFORM_OT_translate={"value":(0.1, 0.1, 0.1)
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
