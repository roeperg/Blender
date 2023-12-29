
from greg_blender import *

###############################################################################################
###############################################################################################

#clearscreen()
print (sys.argv)
join_list = []

if False:

	print("Initially")
	#bpy.ops.object.select_all(action="DESELECT")
	for foo in bpy.data.objects:
		print(foo.name)

	deselect_all()

	file_path = "C:/Users/roepe/Desktop/Imaging and Music/Blender/Ichthys.blend"
	inner_path = 'Object'
	object_name    = "Ichthys"

	bpy.ops.wm.append(
    filepath=os.path.join(file_path, inner_path, object_name),
    directory=os.path.join(file_path, inner_path),
    filename=object_name
    )	#

	object_name    = "CUTOUT"
	bpy.ops.wm.append(
    filepath=os.path.join(file_path, inner_path, object_name),
    directory=os.path.join(file_path, inner_path),
    filename=object_name
    )	#

	#size to inches
	mm_scale = 25.4
	scale_object("Ichthys",(9*mm_scale,4.5*mm_scale,1))
	scale_object("CUTOUT",( 8.5*mm_scale,4*mm_scale,5))
	# now they are 4 x 8.5 inches
	#boolean_difference("Ichthys", "CUTOUT")
	#remove_object("CUTOUT")

if True:
	deselect_all()
	build_cylinder_diameter("ichy", (0,0,0), (111,111,6), ROTATION=(0,0,0), SMOOTH=False, VERTICES=128)

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
bpy.ops.wm.save_as_mainfile(filepath=r"C:\Users\roepe\Desktop\Imaging and Music\Blender\Ichthys_3.blend" )
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

