
from greg_blender import *

###############################################################################################
###############################################################################################
clearscreen()
print (sys.argv)
join_list = []

deselect_all()

tip_outer_diameter = 11.5
tip_length = 16
tip_thickness = 2
cup_diameter = 55
cup_thickness = 3




build_cylinder("tip", (0,0,0), (tip_outer_diameter,tip_outer_diameter,tip_length), ROTATION=(0,0,0), SMOOTH=False, VERTICES=128)
build_cylinder("cut1", (0,0,0), (tip_outer_diameter-tip_thickness,tip_outer_diameter-tip_thickness,160), ROTATION=(0,0,0), SMOOTH=False, VERTICES=128)
boolean_difference("tip", "cut1")

build_sphere("head",(0,0,0), (cup_diameter,cup_diameter,cup_diameter))
build_sphere("cut2",(0,0,0), (cup_diameter-cup_thickness,cup_diameter-cup_thickness,cup_diameter-cup_thickness))
boolean_difference("head", "cut1")
boolean_difference("head", "cut2")

build_cube("cut3", (0,0, -150), (300,300,300))
boolean_difference("head", "cut3")

#remove_object("cut1")
#remove_object("cut2")
#remove_object("cut3")

#  join_list = ["tip","head"]


###############################################################################################
###############################################################################################
if len(join_list) > 1:
  print ("\n\n\nJoining objects")
  for foo in reversed(join_list):
    print(foo)
  join_objects_by_name(join_list)
else:
  print ("Nothing to join")

# save blend
#bpy.ops.wm.save_mainfile()
bpy.ops.wm.save_as_mainfile(filepath=r"C:\Users\roepe\Desktop\Imaging and Music\Blender\bead_funnel.blend")
bpy.ops.export_mesh.stl(filepath=str(r"C:\Users\roepe\Desktop\Imaging and Music\Blender\bead_funnel.stl"))
exit(0)

