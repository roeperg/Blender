
from greg_blender import *

###############################################################################################
###############################################################################################

#clearscreen()
#print (sys.argv)

join_list = ["barb1","barb2","boss"]
cut_list  = ["cut1","cut2"]

deselect_all()

if True:

  build_cube ("boss",(0,0,0),(30,3,2))
  build_cube ("barb1",(0,0,0),(10,2,2))
  build_cube ("barb2",(0,0,0),(10,2,2))
  move_object("barb1",  (-9.5, 2, 0))
  move_object("barb2",  (-9.5,-2, 0))
  rotate_object("barb1",  (0,0, 20))
  rotate_object("barb2",  (0,0,-20))

  if False:
    build_cube ("cut1",(0,0,0),(30,3,2))
    build_cube ("cut2",(0,0,0),(30,3,2))
    move_object("cut1",  (0, 5, 0))
    move_object("cut2",  (0,-5, 0))

    boolean_difference("barb1","cut1")
    boolean_difference("cut2","barb2")

  #for foo in join_list:
  #  for bar in cut_list:
  #    boolean_difference(foo,bar)
  #for foo in cut_list:
  #  remove_object(foo)

if False:
  build_rounded_cube("base1",       (0,0,2), (36,22,4))
  build_rounded_cube("sidepiece1",  (0, 11,14.5), (36,4,25))
  build_rounded_cube("sidepiece2",  (0,-11,14.5), (36,4,25))
  build_rounded_cube("endcap",        (18,0,14.5), (4,22,25))

  join_objects_by_name(["base1", "sidepiece1", "sidepiece2", "endcap"])

  #build_cube("backleft",   (0,0,0), (36,4,36))
  #build_cube("backright",  (0,0,0), (36,4,36))
  #build_cube("frontleft",  (0,0,0), (36,4,36))
  #build_cube("frontright", (0,0,0), (36,4,36))
  #
  build_cylinder("cut1", (0,0,0), (45,45,150), ROTATION=(90,0,0), SMOOTH=True)
  move_object("cut1", (-18,0,28))
  boolean_difference("endcap", "cut1")
  remove_object("cut1")

  #
  #boolean_difference("backleft", "cut1")
  #boolean_difference("backright", "cut1")
  #boolean_difference("frontleft", "cut1")
  #boolean_difference("frontright", "cut1")
  #
  #move_object("backleft",     (-85, 16, 20))
  #move_object("backright",    ( 85, 16, 20))
  #move_object("frontleft",    (-85,-16, 20))
  #move_object("frontright",   ( 85,-16, 20))
  #rotate_object("backright",  (0,0,180))
  #rotate_object("frontright", (0,0,180))
  #
  #join_list.append("supright")

if False:
  test_my_stuff()

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
bpy.ops.wm.save_as_mainfile(filepath=r"C:\Users\roepe\Desktop\Imaging and Music\Blender\mask_strap.blend")
bpy.ops.export_mesh.stl(filepath=str(r"C:\Users\roepe\Desktop\Imaging and Music\Blender\mask_strap.stl"))
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

