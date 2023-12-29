
from greg_blender import *

###############################################################################################
###############################################################################################
clearscreen()
print (sys.argv)
join_list = []

deselect_all()

if True:
  build_funnel("greg",SAE2Metric("7")
               , TIP1=[65,10]
               , TIP2=[85,15]
               , SMOOTH=False
               , VERTICES=128)

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
bpy.ops.wm.save_as_mainfile(filepath=r"C:\Users\roepe\Desktop\Imaging and Music\Blender\chlorine_funnel.blend")
bpy.ops.export_mesh.stl(filepath=str(r"C:\Users\roepe\Desktop\Imaging and Music\Blender\chlorine_funnel.stl"))
exit(0)

