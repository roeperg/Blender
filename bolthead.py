
import random
from math import *
import bpy
import mathutils
from mathutils import Vector
import os
import sys
import numpy

BOLT_POINTS="""
A,0,0.577333333,0,BOTTOM
B,0.499987987,0.288666667,0,BOTTOM
C,0.499987987,-0.288666667,0,BOTTOM
D,0,-0.577333333,0,BOTTOM
E,-0.499987987,-0.288666667,0,BOTTOM
F,-0.499987987,0.288666667,0,BOTTOM
G,0,0.577333333,0.3,TOP
H,0.499987987,0.288666667,0.3,TOP
I,0.499987987,-0.288666667,0.3,TOP
J,0,-0.577333333,0.3,TOP
K,-0.499987987,-0.288666667,0.3,TOP
L,-0.499987987,0.288666667,0.3,TOP
M,0,0.577333333,0,S1
N,0,0.577333333,0.3,S1
O,0.499987987,0.288666667,0.3,S1
P,0.499987987,0.288666667,0,S1
Q,0.499987987,0.288666667,0.3,S2
R,0.499987987,-0.288666667,0.3,S2
S,0.499987987,-0.288666667,0,S2
T,0.499987987,0.288666667,0,S2
U,0.499987987,-0.288666667,0.3,S3
V,0,-0.577333333,0.3,S3
W,0,-0.577333333,0,S3
X,0.499987987,-0.288666667,0,S3
Y,0,-0.577333333,0.3,S4
Z,-0.499987987,-0.288666667,0.3,S4
AA,-0.499987987,-0.288666667,0,S4
AB,0,-0.577333333,0,S4
AC,-0.499987987,-0.288666667,0.3,S5
AD,-0.499987987,0.288666667,0.3,S5
AE,-0.499987987,0.288666667,0,S5
AF,-0.499987987,-0.288666667,0,S5
AG,-0.499987987,0.288666667,0.3,S6
AH,0,0.577333333,0.3,S6
AI,0,0.577333333,0,S6
AJ,-0.499987987,0.288666667,0,S6
"""

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
    ##print(pnt, x, y , z, facename)
    keystring = "%0.5f%0.5f%0.5f" %(float(x), float(y), float(z))
    ##print("keystring = ", keystring)
    if keystring not in doneski.keys():
      doneski[keystring] = 1
      bpy.ops.object.text_add(location=(float(x), float(y), float(z)))
      ob=bpy.context.object
      ob.data.body = pnt
      ob.name = "text%s" %pnt
      ob.data.extrude = 0.01
      ob.data.bevel_depth = 0.002
      scale_object(ob.name, (.2,.2,.2))

###############################################################################################
###############################################################################################
def add_text(in_name, in_text, in_location):

  in_text = in_text.strip()
  bpy.ops.object.text_add(location=in_location)
  ob=bpy.context.object
  ob.data.body = str(in_text)
  ob.name = in_name
  ob.data.extrude = 6
  ob.data.bevel_depth = 0.002
  bpy.ops.object.convert(target='MESH')

  scale_object(ob.name, (5,5,5))
  """
bpy.context.area.ui_type = '<UNKNOWN ENUM>'
Copied 1 selected objects
bpy.ops.object.convert(target='MESH')
bpy.data.window_managers["WinMan"].(null) = 'MESH'
  """
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
  current_v = 0
  for foo in barray:
    foo = foo.strip()
    if len(foo) < 8:
      break
    sarray = foo.split(",")

    (pnt, x, y , z, facename) = foo.split(",")
    #(v, z, y, x) = foo.split(",")
    #(v, y, x, z) = foo.split(",")
    ##print("Vert # %d   x=%d  y=%d  z=%d" %(int(v), float(x), float(y), float(z)))

    if saveface != facename:
      saveface = facename
      if len(verts):
        for foo in verts:
          inverts.append(foo)
        infaces.append(tuple(faces))
        verts = []
        faces = []
      points += "\n%s    " %facename

    verts.append((float(x), float(y), float(z)))
    faces.append(int(current_v))
    current_v += 1
    points += "%s-" %pnt

  points += "\n"
  points = points.replace("-\n","\n")
  for foo in verts:
    inverts.append(foo)
  infaces.append(tuple(faces))
  #print("Max v = %d" %current_v)
  #print(points)
  return (inverts, infaces)

###############################################################################################
###############################################################################################
def base_points(in_file):

  with open(in_file, 'rt') as content_file:
    f1 = content_file.read()
  ##print(f1)
  verts_labels(f1)

###############################################################################################
###############################################################################################
def base_framework(in_object_name, f1):

  rect_verts = []
  rect_faces = []
  ##print(f1)
  (temp_rect, temp_face) = verts_faces(rect_verts,rect_faces, f1)

  #print(rect_verts)
  #print(rect_faces)

  mesh_data = bpy.data.meshes.new("cube_mesh_data")
  mesh_data.from_pydata(rect_verts, [], rect_faces)
  mesh_data.update()

  obj = bpy.data.objects.new(in_object_name, mesh_data)

  scene = bpy.context.scene
  scene.collection.objects.link(obj)
  join_list.append(in_object_name)
  ##print(join_list)

###############################################################################################
###############################################################################################
def base_side(in_object_name):

  rect_verts = [
      (-31, -60,0),
      (-31,  60,0),
      ( 31,  60,0),
      ( 31, -60,0),

      (-31,-60,2.5),
      (-31, 60,2.5),
      ( 31, 60,2.5),
      ( 31,-60,2.5),
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
  ##print("2")

  bpy.ops.object.join()
  ##print("5")

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
  bpy.ops.object.select_all(action="DESELECT")
  obj = bpy.data.objects[in_object_name]
  print(in_object_name, in_rotation)
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
  #print(inBase, bpy.context.active_object.name)

  #bpy.context.space_data.context = 'MODIFIER'
  bpy.ops.object.modifier_add(type='BOOLEAN')
  bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[inCutout]
  bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

###############################################################################################
###############################################################################################
def build_extruded_plane(
                 vertex_list                        # list of vertexes.  3 numbers (x,y,z) for each vertex.
               , edge_list                          # list of point offsets for each segment
               , extrude_tuple                      # 3 member tuple for extrusion
               , in_name ):

  #print("Vertices and edges (straightforward)")
  vertex_point_index_for_segments = []
  for i in range(len(vertex_list)):
    #print(i)
    if i%3 == 0:
      vertex_point_index_for_segments.append(i/3)
  vertices = numpy.array(vertex_list, dtype=numpy.float32)
  num_vertices = vertices.shape[0] // 3
  #print("Polygons are defined in loops.")

  vertex_index = numpy.array(vertex_point_index_for_segments, dtype=numpy.int32)
  #print("For each polygon the start of its vertex indices in the vertex_index array")
  loop_start = numpy.array([0], dtype=numpy.int32)
  #print("Length of each polygon in number of vertices")
  ##print("greggo ...", len(vertex_list))
  loop_total = numpy.array([num_vertices], dtype=numpy.int32)
  edges = numpy.array(edge_list, dtype=numpy.int32)
  num_edges = edges.shape[0] // 2

  num_vertex_indices = vertex_index.shape[0]
  num_loops = loop_start.shape[0]

  #print("Create mesh object based on the arrays above")

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

  #print("Create Object whose Object Data is our new mesh")
  obj = bpy.data.objects.new('created object', mesh)

  #print("Add *Object* to the scene, not the mesh")
  scene = bpy.context.scene
  scene.collection.objects.link(obj)

  # Select the new object and make it active
  bpy.ops.object.select_all(action='DESELECT')
  obj.select_set(True)
  bpy.context.view_layer.objects.active = obj

  extrude_plane(extrude_tuple)

  obj = bpy.context.active_object
  obj.name = in_name
  #print("location", obj.location)
  #print("changing origin")
  bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')

###############################################################################################
###############################################################################################
def adjust_to_head(in_object_name):
  scale_object(in_object_name, (.98,.98 ,1))

###############################################################################################
###############################################################################################
def adjust_to_hole(in_object_name):
  scale_object(in_object_name, (1.02,1.02 ,6))

###############################################################################################
###############################################################################################
def to_inches(inInches):
  # base is in centimeters
  # convert to inInches
  #  1 inch = 25.7 mm
  #  10 mm = 0.393701 inches

  return inInches * 25.7

###############################################################################################
###############################################################################################

###############################################################################################
###############################################################################################
def build_sae_bolt(in_object_name, in_size, x, y):
  boltsize = to_inches(in_size)
  base_framework(in_object_name, BOLT_POINTS)
  scale_object(in_object_name, (boltsize*.98,boltsize*.98,15))
  move_object(in_object_name, (x,y,0))

###############################################################################################
###############################################################################################
def build_mm_bolt(in_object_name, in_size, x, y):
  boltsize = to_inches(in_size)
  base_framework(in_object_name, BOLT_POINTS)
  scale_object(in_object_name, (boltsize*.98,boltsize*.98,15))
  move_object(in_object_name, (x,y,0))

###############################################################################################
###############################################################################################
def build_sae_bolt_cutout(in_object_name, in_size, x, y):
  boltsize = to_inches(in_size)

  extrude_tuple = (0,0,1)  # ( extrude only along Z)
  points = [
      0,0.577333333,0,
      0.499987987,0.288666667,0,
      0.499987987,-0.288666667,0,
      0,-0.577333333,0,
      -0.499987987,-0.288666667,0,
      -0.499987987,0.288666667,0,
  ]

  edges = [
    0, 1,
    1, 2,
    2, 3,
    3, 4,
    4, 5,
    5, 0,
  ]

  build_extruded_plane( points, edges, extrude_tuple, in_object_name)
  #rotate_object(in_object_name,(0,0,-90))
  #rotate_object(in_object_name,Deg2Rad(0,0,-90))

  scale_object(in_object_name, (boltsize*1.02,boltsize*1.02,100))
  move_object(in_object_name, (x,y,-10))

###############################################################################################
###############################################################################################
def build_sae_bolt_pair(in_base, in_object, in_size, x, y):
  b_name = "Bolt" + in_object
  c_name = "Hole" + in_object
  build_sae_bolt   (b_name, in_size, x, y)
  rotate_object(b_name,(0,0,90))
  print("cutout coords  %d, %d" %(x+33, y))
  build_sae_bolt_cutout(c_name, in_size,   x+33, y)
  rotate_object(c_name,(0,0,90))
  boolean_difference(in_base, c_name)
  remove_object(c_name)

clearscreen()
#print(sys.argv)
join_list = []

BUILD_BASE = False
BUILD_BLOCKY = True #
BUILD_END = False    #
BUILD_FACES = False
BUILD_OUTER = False
BUILD_POINTS = False
BUILD_START_BOX = False
BUILD_TUBE = False
JOIN_OBJECTS = False   #

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

#print("Length = %d" %len(sys.argv) )

if True:  #try:
  bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=(0, 0, 0))
  ob=bpy.context.object
  ob.name="Base"
  scale_object("Base", (160,150,4))
  move_object("Base", (0,75,0))

  sae_sockets = [1/4, 5/16, 3/8, 7/16, 1/2, 9/16, 5/8, 11/16, 3/4, 13/16, 7/8, 15/16,1]
  mm_sockets = [5.5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
  voffset = 10
  hoffset = -60

  for foo in range(len(sae_sockets)):
    build_sae_bolt_pair("Base",str(foo), sae_sockets[foo],  hoffset, voffset)
    voffset += to_inches(sae_sockets[foo]+ .25)
    if foo == 7:
      hoffset = 15
      voffset = 15

  add_text("Text_1", "7/16", (25,25,25))
  boolean_difference("Base", "Text_1")
  remove_object("Text_1")

if False: #except:
  #print("Damn")
  exit(0)


# save blend
#bpy.ops.wm.save_mainfile()
bpy.ops.wm.save_as_mainfile(filepath=r"C:\Users\groeper\Desktop\Imaging and Music\Blender\bolthead.blend")
bpy.ops.export_mesh.stl(filepath=str(r"C:\Users\groeper\Desktop\Imaging and Music\Blender\bolthead.stl"))
exit(0)

