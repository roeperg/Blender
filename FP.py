from math import *
from mathutils import Vector
import bmesh
import bpy
import mathutils
import numpy
import os
import random
import sys

###############################################################################################
###############################################################################################
def clearscreen():
  #print
  absolutely_unused_variable = os.system("cls")


###############################################################################################
###############################################################################################
def Deg2Rad(inX,inY,inZ):
    return (pi*inX/180,pi*inY/180,pi*inZ/180)

###############################################################################################
###############################################################################################
def extrude_plane(extrusion_tuple):
  bpy.ops.object.editmode_toggle()
  bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False
                                      , "mirror":False}
                                      , TRANSFORM_OT_translate={"value":extrusion_tuple
                                      , "orient_type":'LOCAL'
                                      , "orient_matrix":((1, 0, 0), (0 , 1, 0), (0, 0, 1))
                                      , "orient_matrix_type":'LOCAL'
                                      , "constraint_axis":(False, False, True)
                                      , "mirror":False
                                      , "use_proportional_edit":False
                                      , "proportional_edit_falloff":'SMOOTH'
                                      , "proportional_size":1
                                      , "use_proportional_connected":False
                                      , "use_proportional_projected":False
                                      , "snap":False
                                      , "snap_target":'CLOSEST'
                                      , "snap_point":(0, 0, 0)
                                      , "snap_align":False
                                      , "snap_normal":(0, 0, 0)
                                      , "gpencil_strokes":False
                                      , "cursor_transform":False
                                      , "texture_space":False
                                      , "remove_on_cancel":False
                                      , "release_confirm":False
                                      , "use_accurate":False})
  bpy.ops.object.editmode_toggle()

  return


###############################################################################################
###############################################################################################
def move_object(in_name, in_location):
     
    bpy.ops.object.select_all(action="DESELECT")
    obj = bpy.data.objects[in_name]
    obj.location = in_location
   
    #bpy.ops.transform.translate(value=in_location
    #    , constraint_axis=(False, False, False)
    #    , mirror=False
    #    , proportional_edit_falloff='SMOOTH'
    #    , proportional_size=1
    #    , release_confirm=True)


###############################################################################################
###############################################################################################
def remove_object(inBase):

        bpy.ops.object.select_all(action="DESELECT")
        objectToSelect = bpy.data.objects[inBase]
        objectToSelect.select_set(True)    
        bpy.context.view_layer.objects.active = objectToSelect
        bpy.ops.object.delete(use_global=False, confirm=False)

###############################################################################################
###############################################################################################
def boolean_difference(inBase, inCutout):

        bpy.ops.object.select_all(action="DESELECT")
        objectToSelect = bpy.data.objects[inBase]
        objectToSelect.select_set(True)    
        bpy.context.view_layer.objects.active = objectToSelect
        print (inBase, bpy.context.active_object.name)

        #bpy.context.space_data.context = 'MODIFIER'
        bpy.ops.object.modifier_add(type='BOOLEAN')
        bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[inCutout]
        bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")


###############################################################################################
###############################################################################################
def build_extruded_plane( 
                 vertex_list                        # list of vertexes.  3 numbers (x,y,z) for each vertex.
               #, vertex_point_index_for_segments    # list of point offsets for each segment
               , extrude_tuple                      # 3 member tuple for extrusion
               , in_name ):
  
        print (" Vertices and edges (straightforward)")
        vertex_point_index_for_segments = []
        for i in range(len(vertex_list)):
          print (i)
          if i%3 == 0:
            vertex_point_index_for_segments.append(i/3)
        vertices = numpy.array(vertex_list, dtype=numpy.float32)
        num_vertices = vertices.shape[0] // 3
        print ("Polygons are defined in loops.")
        
        vertex_index = numpy.array(vertex_point_index_for_segments, dtype=numpy.int32)
        print ("For each polygon the start of its vertex indices in the vertex_index array")
        loop_start = numpy.array([0], dtype=numpy.int32)
        print ("Length of each polygon in number of vertices")
        print("greggo ...", len(vertex_list))
        loop_total = numpy.array([num_vertices], dtype=numpy.int32)
        
        num_vertex_indices = vertex_index.shape[0]
        num_loops = loop_start.shape[0]
        
        print ("Create mesh object based on the arrays above")
        
        mesh = bpy.data.meshes.new(name='created mesh')
        
        mesh.vertices.add(num_vertices)
        mesh.vertices.foreach_set("co", vertex_list)
        
        #mesh.edges.add(num_edges)
        #mesh.edges.foreach_set("vertices", edges)
        
        mesh.loops.add(num_vertex_indices)
        mesh.loops.foreach_set("vertex_index", vertex_index)
        
        mesh.polygons.add(num_loops)
        mesh.polygons.foreach_set("loop_start", loop_start)
        mesh.polygons.foreach_set("loop_total", loop_total)
        
        mesh.update()
        mesh.validate()
        
        print ("Create Object whose Object Data is our new mesh")
        obj = bpy.data.objects.new('created object', mesh)
        
        print ("Add *Object* to the scene, not the mesh")
        scene = bpy.context.scene
        scene.collection.objects.link(obj)
        
        # Select the new object and make it active
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)
        bpy.context.view_layer.objects.active = obj
        
        extrude_plane(extrude_tuple)

        obj = bpy.context.active_object
        obj.name = in_name
        print ("location", obj.location)
        print ("changing origin")
        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')

###############################################################################################
###############################################################################################
def build_cylinder(inName, pos, scale):

        bpy.ops.object.select_all(action="DESELECT")
        bpy.ops.mesh.primitive_cylinder_add(radius=.5, depth=1, enter_editmode=False, location=pos)
        bpy.ops.transform.resize(value=scale, orient_type='GLOBAL'                                  
        , orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1))                                               
        , orient_matrix_type='GLOBAL', constraint_axis=(False, False, True)                             
        , mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH'                  
        , proportional_size=1, use_proportional_connected=False                                         
        , use_proportional_projected=False) 
        obj = bpy.context.active_object
        obj.name = inName

###############################################################################################
###############################################################################################
def build_cube(inName, pos, scale):

        bpy.ops.object.select_all(action="DESELECT")
        bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=pos)
        bpy.ops.transform.resize(value=scale, orient_type='GLOBAL'                                  
        , orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1))                                               
        , orient_matrix_type='GLOBAL', constraint_axis=(False, False, True)                             
        , mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH'                  
        , proportional_size=1, use_proportional_connected=False                                         
        , use_proportional_projected=False) 
        obj = bpy.context.active_object
        obj.name = inName
        return obj

clearscreen()
print (sys.argv)

# Note: we DELETE all objects in the scene and only then create the new mesh!
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()



if True:    
  wall=(52.63,4.75,10) + (4.75,0,0)
  obj = build_cube("wall", (0,0,0),wall)

  # give 3dcursor new coordinates
  bpy.context.scene.cursor.location = Vector((52.63/-2,0.0,0.0))
  
  # set the origin on the current object to the 3dcursor location
  bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
  
  # set 3dcursor location back to the stored location
  bpy.context.scene.cursor.location = Vector((0.0,0.0,0.0))
  obj.location = (0,0,0)
  bpy.ops.wm.save_as_mainfile(filepath=r"C:\Users\groeper\Desktop\Imaging and Music\Blender\fp.blend")

exit(0)
