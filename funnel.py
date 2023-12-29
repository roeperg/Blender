
from greg_blender import *

###############################################################################################
###############################################################################################
clearscreen()
print (sys.argv)
join_list = []

deselect_all()
if True:
  build_cone("cone1", (0,0,0), 100,58, 80, ROTATION=(0,0,0), SMOOTH=False, VERTICES=64)
  build_cone("cone2", (0,-2,0), 92,50, 84, ROTATION=(0,0,0), SMOOTH=False, VERTICES=64)
  boolean_difference("cone1", "cone2")
  remove_object("cone2")

  """
  build_funnel("cone1",SAE2Metric("6")
               , TIP1=[65,10]
               , TIP2=[85,15]
               , SMOOTH=False
               , VERTICES=128)
  """

  #join_list = ["cone1"]

if False:
  build_cube("base1",       (0,0,2), (40,40,40))
  build_cube("cut1",        (0,0,0), (40,27.5,40))
  move_object("cut1", (4,0,4))
  boolean_difference("base1", "cut1")
  move_object("cut1", (0,0,0))
  scale_object("cut1",  (50,50,50))
  move_object("cut1", (24,0,24))
  boolean_difference("base1", "cut1")
  remove_object("cut1")

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
bpy.ops.wm.save_as_mainfile(filepath=r"C:\Users\roepe\Desktop\Imaging and Music\Blender\funnel.blend")
bpy.ops.export_mesh.stl(filepath=str(r"C:\Users\roepe\Desktop\Imaging and Music\Blender\funnel.stl"))
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

