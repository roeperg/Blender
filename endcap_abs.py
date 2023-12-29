
import random
from math import *
import bpy
import mathutils
from mathutils import Vector
import os
import sys
import numpy

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
def verts_labels(in_text):
  # text is tab delimited
  # vert number, x, y z
  in_text = in_text.replace("\t"," ").strip()
  barray = in_text.split("\n")
  headers = barray.pop(0)
  doneski = {}
  for foo in barray:
    foo = foo.strip()
    if len(foo) < 8:
      break
    (pnt, x, y , z, facename) = foo.split(",")

    keystring = "%03d%03d%03d" %(int(x), int(y), int(z))

    if keystring not in doneski.keys():
      doneski[keystring] = 1
      bpy.ops.object.text_add(location=(int(x), int(y), int(z)))
      ob=bpy.context.object
      ob.data.body = pnt
      ob.name = "text%s" %pnt
      ob.data.extrude = 0.1
      ob.data.bevel_depth = 0.02
      scale_object(ob.name, (2,2,2))

###############################################################################################
###############################################################################################
def verts_faces(inverts, infaces, in_text):
  # text is tab delimited
  # vert number, x, y z
  saveface = ""
  verts = []
  faces = []
  points = ""
  in_text = in_text.replace("\t"," ").strip()
  barray = in_text.split("\n")
  headers = barray.pop(0)

  current_v = 0
  for foo in barray:
    foo = foo.strip()
    if len(foo) < 8:
      break
    sarray = foo.split(",")

    (pnt, x, y , z, facename) = foo.split(",")
    #(v, z, y, x) = foo.split(",")
    #(v, y, x, z) = foo.split(",")
    #print ("Vert # %d   x=%d  y=%d  z=%d" %(int(v), int(x), int(y), int(z)))

    if saveface != facename:
      saveface = facename
      if len(verts):
        for foo in verts:
          inverts.append(foo)
        infaces.append(tuple(faces))
        verts = []
        faces = []
      points += "\n%s    " %facename

    verts.append((int(x), int(y), int(z)))
    faces.append(int(current_v))
    current_v += 1
    points += "%s-" %pnt

  points += "\n"
  points = points.replace("-\n","\n")
  for foo in verts:
    inverts.append(foo)
  infaces.append(tuple(faces))
  print ("Max v = %d" %current_v)
  print (points)
  return (inverts, infaces)

###############################################################################################
###############################################################################################
def base_framework(in_object_name):

  with open(r"C:\Users\roepe\Desktop\Imaging and Music\Blender\vertices.csv", 'r') as content_file:
    f1 = content_file.read()

  print ("length of csv = %d" %len(f1))

  rect_verts = []
  rect_faces = []

  if False:
    verts_labels(f1)
  (temp_rect, temp_face) = verts_faces(rect_verts,rect_faces, f1)

  print (rect_verts)
  print (rect_faces)

  mesh_data = bpy.data.meshes.new("cube_mesh_data")
  mesh_data.from_pydata(rect_verts, [], rect_faces)
  mesh_data.update()

  obj = bpy.data.objects.new(in_object_name, mesh_data)

  scene = bpy.context.scene
  scene.collection.objects.link(obj)
  join_list.append(in_object_name)

###############################################################################################
###############################################################################################
def base_side(in_object_name):

  rect_verts = [
      (-31, -20,0),
      (-31,  20,0),
      ( 31,  20,0),
      ( 31, -20,0),

      (-31,-20,5),
      (-31, 20,5),
      ( 31, 20,5),
      ( 31,-20,5),
  ]

  rect_faces = [
      (0, 1, 2, 3),
      (4, 7, 6, 5),
      (0, 4, 5, 1),
      (1, 5, 6, 2),
      (2, 6, 7, 3),
      (4, 0, 3, 7)
  ]

  mesh_data = bpy.data.meshes.new("cube_mesh_data")
  mesh_data.from_pydata(rect_verts, [], rect_faces)
  mesh_data.update()

  obj = bpy.data.objects.new(in_object_name, mesh_data)

  scene = bpy.context.scene
  scene.collection.objects.link(obj)

###############################################################################################
###############################################################################################
def front_side(in_object_name):

  rect_verts = [
      ( -31,-17.5,0),
      (  31,-17.5,0),
      (  31, -22.5,0),
      ( -31, -22.5,0),

      ( -31,-17.5,80),
      (  31,-17.5,80),
      (  31, -22.5,80),
      ( -31, -22.5,80),
  ]

  rect_faces = [
      (0, 1, 2, 3),
      (4, 7, 6, 5),
      (0, 4, 5, 1),
      (1, 5, 6, 2),
      (2, 6, 7, 3),
      (4, 0, 3, 7)
  ]

  mesh_data = bpy.data.meshes.new("cube_mesh_data")
  mesh_data.from_pydata(rect_verts, [], rect_faces)
  mesh_data.update()

  obj = bpy.data.objects.new(in_object_name, mesh_data)

  scene = bpy.context.scene
  scene.collection.objects.link(obj)

###############################################################################################
###############################################################################################
def slanted_side(in_object_name):

  rect_verts = [
  ( 2.5,0,0),       # 0
  ( 2.5,0,80),      # 1
  ( 2.5,40,10),     # 2
  ( 2.5,40,0),      # 3

  (-2.5,0,0),      # 4
  (-2.5,0,80),     # 5
  (-2.5,40,10),    # 6
  (-2.5,40,0),     # 7

  ]

  rect_faces = [
      (0, 1, 2, 3),
      (4, 7, 6, 5),
      (0, 4, 5, 1),
      (1, 5, 6, 2),
      (2, 6, 7, 3),
      (4, 0, 3, 7)
  ]

  mesh_data = bpy.data.meshes.new("cube_mesh_data")
  mesh_data.from_pydata(rect_verts, [], rect_faces)
  mesh_data.update()

  obj = bpy.data.objects.new(in_object_name, mesh_data)

  scene = bpy.context.scene
  scene.collection.objects.link(obj)

###############################################################################################
###############################################################################################
def join_objects_by_name(in_list):

  scene = bpy.context.scene
  bpy.ops.object.select_all(action="DESELECT")

  for ob in in_list:
    obj = bpy.data.objects[ob]
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
  print("2")

  bpy.ops.object.join()
  print("5")

##############################################################################################
###############################################################################################
def extrude_plane(extrusion_tuple):
  bpy.ops.object.editmode_toggle()
  bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False
                                      , "mirror":False}
                                      , TRANSFORM_OT_translate={"value":extrusion_tuple
                                      , "orient_type":'LOCAL'
                                      , "orient_matrix":((1, 0, 0), (0 , 1, 0), (0, 0, 1))
                                      , "orient_matrix_type":'LOCAL'
                                      , "constraint_axis":(False, False, False)  # z was true originally
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
def move_object(in_object_name, in_location):

  bpy.ops.object.select_all(action="DESELECT")
  obj = bpy.data.objects[in_object_name]
  obj.location = in_location

###############################################################################################
###############################################################################################
def scale_object(in_object_name, in_scale):

  bpy.ops.object.select_all(action="DESELECT")
  obj = bpy.data.objects[in_object_name]
  obj.scale = in_scale

###############################################################################################
###############################################################################################
def rotate_object(in_object_name, in_rotation):
  print (in_rotation)
  bpy.ops.object.select_all(action="DESELECT")
  obj = bpy.data.objects[in_object_name]
  obj.rotation_euler = Deg2Rad(in_rotation[0],in_rotation[1],in_rotation[2])

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
                 vertex_csv                         # list of vertexes.  3 numbers (x,y,z) for each vertex.
               , edge_list                          # list of point offsets for each segment
               , extrude_tuple                      # 3 member tuple for extrusion
               , in_object_name ):

  print ("Vertices and edges (straightforward)")
  vertex_point_index_for_segments = []
  vertex_list = []

  with open(vertex_csv, 'r') as content_file:
    f1 = content_file.read()

  print ("length of csv = %d" %len(f1))

  for foo in f1.split("\n"):         # lines
    for bar in foo.split(","):       # members
      try:
        vertex_list.append(float(bar))
      except Exception:
        pass

  print (vertex_list)
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
  edges = numpy.array(edge_list, dtype=numpy.int32)
  num_edges = edges.shape[0] // 2

  num_vertex_indices = vertex_index.shape[0]
  num_loops = loop_start.shape[0]

  print ("Create mesh object based on the arrays above")

  mesh = bpy.data.meshes.new(name='created mesh')

  mesh.vertices.add(num_vertices)
  mesh.vertices.foreach_set("co", vertex_list)

  mesh.edges.add(num_edges)
  mesh.edges.foreach_set("vertices", edges)

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
  obj.name = in_object_name
  print ("location", obj.location)
  print ("changing origin")
  bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')

###############################################################################################
###############################################################################################
def build_cube(in_object_name, pos, scale):

  bpy.ops.object.select_all(action="DESELECT")
  bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=pos)
  bpy.ops.transform.resize(value=scale, orient_type='GLOBAL'
  , orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1))
  , orient_matrix_type='GLOBAL', constraint_axis=(False, False, True)
  , mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH'
  , proportional_size=1, use_proportional_connected=False
  , use_proportional_projected=False)
  obj = bpy.context.active_object
  obj.name = in_object_name

###############################################################################################
###############################################################################################
def build_heart(in_object_name):
  pos = (0,0,0)
  bpy.ops.object.select_all(action="DESELECT")
  # cube
  bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=pos)
  bpy.ops.transform.resize(value=(6,300,6), orient_type='GLOBAL'
  , orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1))
  , orient_matrix_type='GLOBAL', constraint_axis=(False, False, True)
  , mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH'
  , proportional_size=1, use_proportional_connected=False
  , use_proportional_projected=False)
  obj = bpy.context.active_object
  obj.name = in_object_name

  bpy.ops.mesh.primitive_cylinder_add(radius=.5, depth=1, enter_editmode=False, location=pos)
  bpy.ops.transform.resize(value=(6,6,300), orient_type='GLOBAL'
      , orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1))
      , orient_matrix_type='GLOBAL', constraint_axis=(False, False, True)
      , mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH'
      , proportional_size=1, use_proportional_connected=False
  , use_proportional_projected=False)
  obj = bpy.context.active_object
  obj.name = "tmp_cyl1"

  bpy.ops.mesh.primitive_cylinder_add(radius=.5, depth=1, enter_editmode=False, location=pos)
  bpy.ops.transform.resize(value=(6,6,300), orient_type='GLOBAL'
      , orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1))
      , orient_matrix_type='GLOBAL', constraint_axis=(False, False, True)
      , mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH'
      , proportional_size=1, use_proportional_connected=False
  , use_proportional_projected=False)
  obj = bpy.context.active_object
  obj.name = "tmp_cyl2"

  rotate_object(in_object_name,(0,45,0))
  rotate_object("tmp_cyl1",(0,90,90))
  rotate_object("tmp_cyl2",(0,90,90))

  move_object("tmp_cyl1",(-2.355,0,-2.3))
  move_object("tmp_cyl2",( 2.355,0,-2.3))

  #join_objects_by_name(["tmp_cyl1","tmp_cyl2", in_object_name])
  #rotate_object(in_object_name,(0,45,90))

###############################################################################################
###############################################################################################
def build_cylinder(in_object_name, pos, scale, ROTATION=(0,0,0)):

  bpy.ops.object.select_all(action="DESELECT")
  bpy.ops.mesh.primitive_cylinder_add(radius=.5, depth=1, enter_editmode=False, location=pos)
  bpy.ops.transform.resize(value=scale, orient_type='GLOBAL'
      , orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1))
      , orient_matrix_type='GLOBAL', constraint_axis=(False, False, True)
      , mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH'
      , proportional_size=1, use_proportional_connected=False
  , use_proportional_projected=False)
  obj = bpy.context.active_object
  obj.name = in_object_name
  print ("\n\n\n\nRotate")
  print (ROTATION)
  print ("\n\n\n\n")
  rotate_object(obj.name, ROTATION)

###############################################################################################
###############################################################################################

clearscreen()
print (sys.argv)
join_list = []

BUILD_END = True
BUILD_TUBE = False
BUILD_START_BOX = False
BUILD_BASE = False
BUILD_FACES = False
BUILD_BLOCKY = True
BUILD_OUTER = False
JOIN_OBJECTS = False

# Note: we DELETE all objects in the scene and only then create the new mesh!
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

if BUILD_END:

  edges = [
    5, 6,
    6, 7,
    5, 7
  ]

  extrude_tuple = (0,0,30)  # ( extrude only along Z)
  build_extruded_plane( r"C:\Users\roepe\Desktop\Imaging and Music\Blender\end.csv", edges, extrude_tuple, "triangle_base")

  rotate_object("triangle_base",(0,0,-90))
  move_object("triangle_base",(31,-10,15))                            #(0,-30,17.43845))
  build_cylinder("cutout_cylinder", (31,-16,0),(16.5,16.5,150))
  boolean_difference("triangle_base", "cutout_cylinder")
  remove_object("cutout_cylinder")
  #build_cube("cutout_box", (0,0,35),(52,100,60))
  ##move_object("cutout_box", (5,5,44))
  #boolean_difference("triangle_base", "cutout_box")
  #remove_object("cutout_box")
  join_list.append("triangle_base")

if BUILD_TUBE:

  build_cylinder("base_cylinder", (0,0,0),(22,22,6))
  build_cylinder("cutout_cylinder", (0,0,0),(17,17,150))
  boolean_difference("base_cylinder", "cutout_cylinder")
  remove_object("cutout_cylinder")
  join_list.append("base_cylinder")

if BUILD_START_BOX:

  build_cube("start_box", (0,0,0),(62,40,100))
  build_cube("cutout_box", (0,5,5),(52,40,100))
  #move_object("cutout_box", (5,5,44))
  boolean_difference("start_box", "cutout_box")
  remove_object("cutout_box")
  join_list.append("start_box")

if BUILD_BASE:
  points = [
    0,0,0,
    60,0,0,
    90,30,0,
    0,30,0,
  ]

  edges = [
    5, 6,
    6, 7,
    5, 7

  ]

  build_extruded_plane( in_csv, edges, (0,0,120), "base_cutout")
  rotate_object("base_cutout",(0,90,0))
  move_object("base_cutout",(-15,6.1,12))
  join_list.append("triangle_base")
  #boolean_difference("start_box", "base_cutout")
  #remove_object("base_cutout")

if BUILD_FACES:
  slanted_side("leftside")
  slanted_side("rightside")
  base_side("base")
  front_side("front")

  move_object("leftside",(-28.5,-20,0))
  move_object("rightside",(28.5,-20,0))
  #move_object("front",(0,-20,28))
  join_list.append("leftside")
  join_list.append("rightside")
  join_list.append("base")
  join_list.append("front")

if BUILD_BLOCKY:
  base_framework("blocky")
  #build_heart("cutout_heart")
  #move_object("cutout_heart", (0,12,15))
  build_cylinder("cutout_cylinder", (0,26,15),(16.5,10,150), ROTATION=(0,90,0))
  boolean_difference("blocky", "cutout_cylinder")
  remove_object("cutout_cylinder")

  build_cylinder("cutout_cylinder", (0,12,46),(16.5,10,150), ROTATION=(0,90,0))
  boolean_difference("blocky", "cutout_cylinder")
  remove_object("cutout_cylinder")

  build_cylinder("cutout_cylinder", (0,12,15),(16.5,10,150), ROTATION=(0,90,0))
  boolean_difference("blocky", "cutout_cylinder")
  remove_object("cutout_cylinder")

if BUILD_OUTER:
  build_cube("base" , (0,0,0),(62,5,40))
  build_cube("front", (0,0,0),(62,40,5))
  join_list.append("base")
  join_list.append("front")

###############################################################################################
###############################################################################################
if JOIN_OBJECTS:
  if len(join_list) > 1:
    print ("\n\n\nJoining objects")
    for foo in join_list:
      print(foo)
    join_objects_by_name(join_list)
  else:
    print ("Nothing to join")

# save blend
#bpy.ops.wm.save_mainfile()
bpy.ops.wm.save_as_mainfile(filepath=r"C:\Users\roepe\Desktop\Imaging and Music\Blender\endcap_scripted.blend")
bpy.ops.export_mesh.stl(filepath=str(r"C:\Users\roepe\Desktop\Imaging and Music\Blender\endcap_scripted.stl"))
exit(0)

"""
        print ("getting")
        obj.name = in_object_name
        print ("moving", in_object_name)
        move_object(obj, (0,0,0))
        print ("done")

bpy.context.space_data.context = 'MODIFIER'
bpy.ops.object.modifier_add(type='SOLIDIFY')
bpy.context.object.modifiers["Solidify"].thickness = 0.05
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Solidify")
bpy.context.area.ui_type = '<UNKNOWN ENUM>'

"""

