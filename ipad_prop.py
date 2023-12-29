
from greg_blender import *

###############################################################################################
###############################################################################################

#clearscreen()
print (sys.argv)
join_list = []

deselect_all()

#build_sphere("balls", (0,0,0), (60,10,80))
#build_frame("back1", (0,18,-10), (212,4,70    ))
#build_frame("back2", (0,18,0)  , (4,212,70    ))
#build_cube("back3", (0,0,0)  , (212,70,4))
#build_cube("back2", (0,0,0)  , (212,4,70))
#build_cube("back1", (0,0,0)  , (4,300,100))

#rotate_object("back1", (0,0,0))
#move_object("back1", (0,18,33))
build_cube("back", (0,18,33), (208,4,70))
build_cube("base", (0,0,-2), (208,36,4))
build_cube("frontleft",  (0,0,0), (36,4,70))
build_cube("frontright", (0,0,0), (36,4,70))
build_cube("left", (-104,0,33), (4,36,70))
build_cube("right", (104,0,33), (4,36,70))
build_cube("supleft", (-69,0,17), (4,36,35))
build_cube("supright", (69,0,17), (4,36,35))

build_cylinder("cutter1", (0,0,0), (45,45,150), ROTATION=(90,0,0), SMOOTH=True)
move_object("cutter1", (18,0,36))
boolean_difference("frontleft", "cutter1")
boolean_difference("frontright", "cutter1")
remove_object("cutter1")

move_object("frontleft", (-85,-18,33))
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

###############################################################################################
###############################################################################################
if False:#if len(join_list) > 1:
  print ("\n\n\nJoining objects")
  for foo in join_list:
    print(foo)
  join_objects_by_name(join_list)
else:
  print ("Nothing to join")

# save blend
#bpy.ops.wm.save_mainfile()
bpy.ops.wm.save_as_mainfile(filepath=r"C:\Users\roepe\Desktop\Imaging and Music\Blender\ipad_prop.blend")
bpy.ops.export_mesh.stl(filepath=str(r"C:\Users\roepe\Desktop\Imaging and Music\Blender\ipad_prop.stl"))
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

