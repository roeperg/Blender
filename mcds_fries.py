
from greg_blender import *

###############################################################################################
###############################################################################################
clearscreen()
print (sys.argv)
join_list = []

verts = 128
smoothit = False

deselect_all()
if True:
  build_cone("Fries", (0,0,0), 100,100, 70, ROTATION=(0,0,0), SMOOTH=smoothit, VERTICES=verts)
  build_cone("cone2", (0,0,3), 94,94, 70, ROTATION=(0,0,0), SMOOTH=smoothit, VERTICES=verts)
  boolean_difference("Fries", "cone2")
  remove_object("cone2")

###############################################################################################
###############################################################################################
if len(join_list) > 1:
  print ("\n\n\nJoining objects")
  for foo in join_list:
    print(foo)
  join_objects_by_name(join_list)
else:
  print ("Nothing to join")

save_files(os.path.basename(__file__).replace(".py",""))

exit(0)

