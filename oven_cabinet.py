

if False:
	import bpy
	print(bpy.__file__)
	import greg_blender
	print(greg_blender.__file__)
	exit()

from greg_blender import *

###############################################################################################
###############################################################################################

build_cube ("side", (0, 0,0), (29.75,43.25, .5))

"""
		#declare oven=
		 union {
		        box {<0,0,0> <29.75,43.25, .5> texture { pigment{Silver} } }
		        box {<0,0,0> <28.5,43.25,23> translate <.5125,0,0>texture { pigment{Red} } }
		}

		#declare side_panel =
		 union {
		        box {<0,0,0> <5/8,96,23.25> texture { pigment{DarkSlateBlue} } }
		        sphere { <0,0,0> 1 pigment{Red}}
		}

		#declare front_side_panel_top = box {<0,0,0> <28.5,28,5/8> translate y*(96-28)texture { pigment{DarkSlateBlue} } }

		#declare shelf =
		 union {
		        box {<0,0,0> <29.75, 5/8, 23.25> texture { pigment{DarkSlateBlue} } }
		        sphere { <0,0,0> 1 pigment{Red}}
		}

		#macro SAE(inches,fractions)
		 inches + fractions
		#end

"""

#clearscreen()
print (sys.argv)
join_list = []

measures = {}

measures['1/4'] = (.25)
measures['1/2'] = (.5)
measures['5/8'] = (5/8)
measures['7/8'] = (7/8)
measures['5/16'] = (5/16)

print(measures)
#exit()

#bpy.context.scene.unit_settings.system = 'IMPERIAL'
#bpy.context.scene.unit_settings.length_unit = 'INCHES'

deselect_all()
#build_cube ("cut1", (0, 600,0), (1200,1200,30))

# adjust for mm
side_panel_height = 96
side_panel_depth =  23.25
side_panel_width =  5/8

front_panel_height = 91.25
front_panel_depth =  5/8
front_panel_width =  33.25

shelf_height = 5/8
shelf_depth =  23.25
shelf_width =  28.5

print(side_panel_width,side_panel_depth,side_panel_height)

if True:
	print("Building sides")
	build_cube ("side1", (side_panel_width/2,side_panel_depth/2,side_panel_height/2), (side_panel_width,side_panel_depth,side_panel_height))
	build_cube ("side2", (side_panel_width/2,side_panel_depth/2,side_panel_height/2), (side_panel_width,side_panel_depth,side_panel_height))
	move_object("side1", (14.875+(side_panel_width/2), side_panel_depth/2,side_panel_height/2))
	move_object("side2", (-(14.875+(side_panel_width/2)), side_panel_depth/2,side_panel_height/2))
	build_cube ("cut1", (0, 0,2.5), (200,5,5))
	boolean_difference("side1", "cut1")
	boolean_difference("side2", "cut1")
	remove_object("cut1")

if False:
	print("Building front")
	build_cube ("front", (0,-(front_panel_depth/2),50.5), (front_panel_width,front_panel_depth,front_panel_height))

if True:
	print("Building shlf")
	build_cube ("shelf1", (0,0,0), (shelf_width,shelf_depth,shelf_height))
	shelf1_z = 23 + measures['7/8'] + measures['5/16']
	move_object("shelf1", (0, shelf_depth/2, shelf1_z))
	if False:
		print("Getting dimensions")
		dims = get_object_dimensions("side1")

		for bar in dims:
			#print(bar, bar/25.4)
			dims.append(bar/25.4)
		print('Dimensions for     side1  {:0.6f} in x {:0.2f} in x {:0.2f} in'.format( dims[0]/25.4,dims[1]/25.4,dims[2]/25.4 ))

	#print("Setting origin")
	set_object_center("side1")

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

if True:
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

