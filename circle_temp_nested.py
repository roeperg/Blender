
from greg_blender import *

###############################################################################################
###############################################################################################

clearscreen()

half_inch = SAE2Metric(".5")
inch = SAE2Metric("1")
print (sys.argv)

join_list = []


diams = [2,4,6,8]

for foo in diams:
	deselect_all()
	objname = "main tube %d" %foo
	inner_diameter = foo*inch
	outer_diameter = inner_diameter + half_inch
	print(outer_diameter, outer_diameter / 12.7)
	build_cylinder_diameter(objname, (0,0,0), (outer_diameter,outer_diameter,6), ROTATION=(0,0,0), SMOOTH=False, VERTICES=128)

	build_cylinder_diameter("cut1", (0,0,0), (inner_diameter,inner_diameter,100), ROTATION=(0,0,0), SMOOTH=False, VERTICES=128)
	boolean_difference(objname, "cut1")
	remove_object("cut1")
	bpy.ops.export_mesh.stl(filepath=str(r"C:\Users\roepe\Desktop\Imaging and Music\Blender\circle_%d.stl" %foo))

print("Done")


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
bpy.ops.wm.save_as_mainfile(filepath=r"C:\Users\roepe\Desktop\Imaging and Music\Blender\%s" %sys.argv[4])
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

