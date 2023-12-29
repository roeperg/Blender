
from greg_blender import *

###############################################################################################
###############################################################################################

#clearscreen()
print (sys.argv)
join_list = []

deselect_all()
if False:
	# 9 inch outside diameter
	outer_diameter = 228.6
	inner_diameter = outer_diameter - 10
	build_cylinder("main tube", (0,0,0), (outer_diameter,outer_diameter,6), ROTATION=(0,0,0), SMOOTH=False, VERTICES=128)
	build_cylinder("cut1", (0,0,0), (200,200,101.6), ROTATION=(0,0,0), SMOOTH=False)
	#move_object("cut1", (0,0,50.8))
	boolean_difference("main tube", "cut1")
	remove_object("cut1")

	build_cube("cut2", ((outer_diameter/2),0,0), (outer_diameter, outer_diameter, 16))
	boolean_difference("main tube", "cut2")
	remove_object("cut2")

	
	build_cube("straight edge", (0,0,0), (5, outer_diameter, 6))

	build_cylinder("center tab", (0,0,0), (30,30,6), ROTATION=(0,0,0), SMOOTH=False, VERTICES=128)
	build_cylinder("cut3", (0,0,0), (8,8,16), ROTATION=(0,0,0), SMOOTH=False, VERTICES=128)
	boolean_difference("center tab", "cut3")
	boolean_difference("straight edge", "cut3")
	remove_object("cut3")

	join_list.append("straight edge")
	join_list.append("center tab")
	join_list.append("main tube")


if False:
	# 9 inch inside diameter
	inner_diameter = 228.6
	outer_diameter = inner_diameter + 10
	build_cylinder("main tube", (0,0,0), (outer_diameter,outer_diameter,6), ROTATION=(0,0,0), SMOOTH=False, VERTICES=128)
	build_cylinder("cut1", (0,0,0), (inner_diameter,inner_diameter,100), ROTATION=(0,0,0), SMOOTH=False, VERTICES=128)
	#move_object("cut1", (0,0,50.8))
	boolean_difference("main tube", "cut1")
	remove_object("cut1")
	
	build_cube("cut2", ((outer_diameter/2),0,0), (outer_diameter, outer_diameter, 16))
	boolean_difference("main tube", "cut2")
	remove_object("cut2")

	
	build_cube("straight edge", (0,0,0), (5, outer_diameter, 6))

	build_cylinder("center tab", (0,0,0), (30,30,6), ROTATION=(0,0,0), SMOOTH=False, VERTICES=128)
	build_cylinder("cut3", (0,0,0), (8,8,16), ROTATION=(0,0,0), SMOOTH=False, VERTICES=128)
	boolean_difference("center tab", "cut3")
	boolean_difference("straight edge", "cut3")
	remove_object("cut3")

	join_list.append("straight edge")
	join_list.append("center tab")
	join_list.append("main tube")



if True:
	inner_diameter = 100
	outer_diameter = inner_diameter + 20
	build_cylinder("main tube", (0,0,0), (outer_diameter,outer_diameter,6), ROTATION=(0,0,0), SMOOTH=False, VERTICES=128)

	build_cylinder("cut1", (0,0,0), (inner_diameter,inner_diameter,100), ROTATION=(0,0,0), SMOOTH=False, VERTICES=128)
	#move_object("cut1", (0,0,50.8))
	boolean_difference("main tube", "cut1")
	remove_object("cut1")
	
	build_cube("cut2", (0,0,0), (outer_diameter, outer_diameter, 10))
	#boolean_difference("main tube", "cut2")
	#rotate_object("main tube", (0,0,45))
	#boolean_difference("main tube", "cut2")
	#remove_object("cut2")

	build_cube("tenon1", (0,0,0), (5,5,6))
	build_cube("tenon2", (0,0,0), (10,5,6))
	rotate_object("tenon1", (0,0,45))
	move_object("tenon1", (0,-55,0))
	move_object("tenon2", (0,-55,0))


###############################################################################################
###############################################################################################
if len(join_list) > 1:
	print ("\n\n\nJoining objects")
	for foo in join_list:
		print(foo)
	join_objects_by_name(join_list)
else:
	print ("Nothing to join")

rotate_object("main tube", (0,0, 45))
# save blend
#bpy.ops.wm.save_mainfile()
bpy.ops.wm.save_as_mainfile(filepath=r"C:\Users\roepe\Desktop\Imaging and Music\Blender\circle_template.blend")
bpy.ops.export_mesh.stl(filepath=str(r"C:\Users\roepe\Desktop\Imaging and Music\Blender\circle_template.stl"))
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

