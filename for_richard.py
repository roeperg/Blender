

if False:
	import bpy
	print(bpy.__file__)
	import greg_blender
	print(greg_blender.__file__)
	exit()

from greg_blender import *

###############################################################################################
###############################################################################################


#clearscreen()
print (sys.argv)
join_list = []

q_inch = SAE2Metric(.25)
h_inch = SAE2Metric(.5)

print(q_inch, h_inch)

if True:
	s_size = 120    # equates to 4 inch high
	s_off  = 71

if False:
	s_size = 55.5    # equates to 2 inch high
	s_off = 35.5	

deselect_all()
#bpy.context.scene.unit_settings.system = 'IMPERIAL'
#bpy.context.scene.unit_settings.length_unit = 'INCHES'
build_cube ("greg", (0,0,0), (10,10,10))


	
if True:
	deselect_all()
	build_cylinder_diameter("outer1", (0, s_off,0), (s_size+h_inch,s_size+h_inch,6), ROTATION=(0,0,0), SMOOTH=False, VERTICES=128)

	#build_cube ("cut1", (0, 150,0), (300,300,300))
	#boolean_difference("outer1", "cut1")
	#remove_object("cut1")	

	#build_cylinder_diameter("cutout1", (0, s_off,0), (s_size,s_size,6), ROTATION=(0,0,0), SMOOTH=False, VERTICES=128)
	#boolean_difference("outer1", "cutout1")
	#remove_object("cutout1")	

	print("Dimensions: ", get_object_dimensions("outer1"))


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
print("\n\n\nC:/Users/roepe/Desktop/Imaging and Music/Blender/%s\n\n\n" %sys.argv[4] )
bpy.ops.wm.save_as_mainfile(filepath="C:/Users/roepe/Desktop/Imaging and Music/Blender/%s" %sys.argv[4] )
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

