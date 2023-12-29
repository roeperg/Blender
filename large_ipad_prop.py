from greg_blender import *

###############################################################################################
###############################################################################################
def case_outer():

  rect_verts = []
  rect_faces = []

  (verts, faces) = to_wall(0,0,0,6,212,27, len(rect_verts))
  rect_verts += verts
  rect_faces += faces

  (verts, faces) = to_wall(-152,0,0,-150.4,105,90, len(rect_verts))
  rect_verts += verts
  rect_faces += faces

  (verts, faces) = to_wall(0,0,0,-152,105,6, len(rect_verts))
  rect_verts += verts
  rect_faces += faces

  (verts, faces) = to_wall(0,0,0,-152,6,90, len(rect_verts))
  rect_verts += verts
  rect_faces += faces

  (verts, faces) = to_wall(0,105,0,-152,103.4,90, len(rect_verts))
  rect_verts += verts
  rect_faces += faces

  mesh_data = bpy.data.meshes.new("cube_mesh_data")
  mesh_data.from_pydata(rect_verts, [], rect_faces)
  mesh_data.update()

  obj = bpy.data.objects.new("drivecase", mesh_data)

  scene = bpy.context.scene
  scene.collection.objects.link(obj)

###############################################################################################
###############################################################################################

clearscreen()
print (sys.argv)
join_list = []

deselect_all()
"""
build_cube("back", (0,18,33), (212,4,70))
build_cube("base", (0,0,0), (212,40,4))
build_cube("frontleft",  (-85,-18,33), (40,4,70))
build_cube("frontright", (-85,-18,33), (40,4,70))
build_cube("left", (-104,0,33), (4,40,70))
build_cube("right", (104,0,33), (4,40,70))
build_cube("supleft", (-69,0,17), (4,40,35))
build_cube("supright", (69,0,17), (4,40,35))

build_cylinder("cutter1", (-65,-25,70), (60,60,30), ROTATION=(90,0,0))

boolean_difference("frontleft", "cutter1")
boolean_difference("frontright", "cutter1")
remove_object("cutter1")

move_object("frontright", (85,-18,33))
rotate_object("frontright", (0,0,180))

join_list.append("back")
join_list.append("base")
join_list.append("frontleft")
join_list.append("frontright")
join_list.append("left")
join_list.append("right")
join_list.append("supleft")
join_list.append("supright")
"""

#build_cube("corner", (0,0,0), (36,36,24))
#build_cube("cutter1", (16,-16,0), (36,36,30))
#build_cube("cutter2", (4,-4,0), (36,36,17.5))

#boolean_difference("corner", "cutter1")
#boolean_difference("corner", "cutter2")
#remove_object("cutter1")
#remove_object("cutter2")

build_cube("base01", (   0,0  ,0), (258,36,4))
build_cube("base02", ( 112.5,0,3.5), ( 30,36,4))
build_cube("base03", (-112.5,0,3.5), ( 30,36,4))
build_cube("corner02", ( 127  ,0,14), (4,36,25))
build_cube("corner03", (-127  ,0,14), (4,36,25))
build_cube("corner04", (-120  , -16,14), (14,4,25))
build_cube("corner06", ( 0    ,  16,14), (258,4,25))
build_cube("corner07", ( 120  ,-16,14), (14,4,25))
build_cube("corner08", ( 110  ,-16,8.5), (25,4,14))
build_cube("corner09", (-110  ,-16,8.5), (25,4,14))

build_cylinder("cyl01", ( 112, 8,-1.5), (6,6,6))
build_cylinder("cyl02", (-112, 8,-1.5), (6,6,6))
build_cylinder("cyl03", ( 112,-8,-1.5), (6,6,6))
build_cylinder("cyl04", (-112,-8,-1.5), (6,6,6))

build_cylinder("cyl05", (-10,17, 8), (3,3,12), ROTATION=(90,0,0))
build_cylinder("cyl06", ( 10,17, 8), (3,3,12), ROTATION=(90,0,0))
build_cylinder("cyl07", (-10,17,20), (3,3,12), ROTATION=(90,0,0))
build_cylinder("cyl08", ( 10,17,20), (3,3,12), ROTATION=(90,0,0))

boolean_difference("base01", "cyl01")
boolean_difference("base01", "cyl03")
boolean_difference("base02", "cyl01")
boolean_difference("base02", "cyl03")

boolean_difference("base01", "cyl02")
boolean_difference("base01", "cyl04")
boolean_difference("base03", "cyl02")
boolean_difference("base03", "cyl04")

boolean_difference("corner06", "cyl05")
boolean_difference("corner06", "cyl06")
boolean_difference("corner06", "cyl07")
boolean_difference("corner06", "cyl08")

remove_object("cyl01")
remove_object("cyl02")
remove_object("cyl03")
remove_object("cyl04")
remove_object("cyl05")
remove_object("cyl06")
remove_object("cyl07")
remove_object("cyl08")

join_list = ["base01","base02","base03","corner02","corner03","corner04","corner06","corner07","corner08","corner09"]

###############################################################################################
###############################################################################################

if len(join_list) > 1:
  print ("\n\n\nJoining objects")
  for foo in join_list:
    print(foo)
  join_objects_by_name(join_list)
else:
  print ("Nothing to join")

# save blend
#bpy.ops.wm.save_mainfile()
bpy.ops.wm.save_as_mainfile(filepath=r"C:\Users\roepe\Desktop\Imaging and Music\Blender\large_ipad_prop.blend")
bpy.ops.export_mesh.stl(filepath=str(r"C:\Users\roepe\Desktop\Imaging and Music\Blender\large_ipad_prop.stl"))
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

