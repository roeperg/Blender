from greg_blender import *

###############################################################################################
###############################################################################################
def case_outer():

  rect_verts = []
  rect_faces = []

  (verts, faces) = to_wall(0,0,0,1.6,105,27, len(rect_verts))
  rect_verts += verts
  rect_faces += faces

  (verts, faces) = to_wall(-152,0,0,-150.4,105,90, len(rect_verts))
  rect_verts += verts
  rect_faces += faces

  (verts, faces) = to_wall(0,0,0,-152,105,1.6, len(rect_verts))
  rect_verts += verts
  rect_faces += faces

  (verts, faces) = to_wall(0,0,0,-152,1.6,90, len(rect_verts))
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

case_outer()

move_object("drivecase", (152,-52.5,0))

build_cylinder("upright1", (.5, 52,45),(4,4,90) , ROTATION=(0,0,0))
build_cylinder("upright2", (.5,-52,45),(4,4,90) , ROTATION=(0,0,0))
build_cylinder("upright3", (151.5, 52,45),(4,4,90) , ROTATION=(0,0,0))
build_cylinder("upright4", (151.5,-52,45),(4,4,90) , ROTATION=(0,0,0))

join_list.append("drivecase")
join_list.append("upright1")
join_list.append("upright2")
join_list.append("upright3")
join_list.append("upright4")

build_cylinder("cylcut1", (18,0,18.6),(3.6,3.6,150) , ROTATION=(90,0,0))
build_cylinder("cylcut2", (120,0,18.6),(3.6,3.6,150), ROTATION=(90,0,0))

build_cylinder("cylcut3", (18,0,48.6),(3.6,3.6,150) , ROTATION=(90,0,0))
build_cylinder("cylcut4", (120,0,48.6),(3.6,3.6,150), ROTATION=(90,0,0))

build_cylinder("cylcut5", (18,0,78.6),(3.6,3.6,150) , ROTATION=(90,0,0))
build_cylinder("cylcut6", (120,0,78.6),(3.6,3.6,150), ROTATION=(90,0,0))

boolean_difference("drivecase", "cylcut1")
remove_object("cylcut1")
boolean_difference("drivecase", "cylcut2")
remove_object("cylcut2")
boolean_difference("drivecase", "cylcut3")
remove_object("cylcut3")
boolean_difference("drivecase", "cylcut4")
remove_object("cylcut4")
boolean_difference("drivecase", "cylcut5")
remove_object("cylcut5")
boolean_difference("drivecase", "cylcut6")
remove_object("cylcut6")

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
bpy.ops.wm.save_as_mainfile(filepath=r"C:\Users\roepe\Desktop\Imaging and Music\Blender\drivecase_beta.blend")
bpy.ops.export_mesh.stl(filepath=str(r"C:\Users\roepe\Desktop\Imaging and Music\Blender\drivecase_beta.stl"))
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

