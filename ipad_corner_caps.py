
from greg_blender import *

###############################################################################################
###############################################################################################

#clearscreen()
print (sys.argv)
join_list = []

deselect_all()

if True:
  build_cube("base1",       (0,0,2), (40,40,40))
  build_cube("cut1",        (0,0,2), (40,27.5,40))
  move_object("cut1", (4,0,4))
  boolean_difference("base1", "cut1")
  move_object("cut1", (0,0,0))
  scale_object("cut1",  (50,50,50))
  move_object("cut1", (24,0,24))
  boolean_difference("base1", "cut1")
  remove_object("cut1")

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
bpy.ops.wm.save_as_mainfile(filepath=r"C:\Users\roepe\Desktop\Imaging and Music\Blender\ipad_corner_caps.blend")
bpy.ops.export_mesh.stl(filepath=str(r"C:\Users\roepe\Desktop\Imaging and Music\Blender\ipad_corner_caps.stl"))
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

