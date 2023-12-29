
from greg_blender import *

###############################################################################################
###############################################################################################
clearscreen()
print (sys.argv)
join_list = []

verts = 128
smoothit = False

deselect_all()

if False:
	build_cube("base",   (0,0,0), (44.8,36.6,16.5))

	build_cube("cut1",    (6,0,15), (60,60,16.7))
	rotate_object ("cut1",(0,12,0))
	boolean_difference("base", "cut1")
	remove_object("cut1")

	build_cube("cut2",    (-12,0,8.2), (30,26,20))
	boolean_difference("base", "cut2")
	remove_object("cut2")

	build_cube("cut3",    (-26,0,18), (40,40,40))
	boolean_difference("base", "cut3")
	remove_object("cut3")

	build_cylinder("cyl1", (0,0,0), (5,5,60))
	rotate_object("cyl1",(90,0,0))
	move_object("cyl1", ( 0,0,1.7))
	boolean_difference("base", "cyl1")
	remove_object("cyl1")

if False:
	build_cube("base",   (0,0,0), (44.8,36.6,6.5))
	build_cube("rise",   (0,0,0), (20,36.6,16.7))
	build_cube("cut1",    (0,0,15), (60,60,16.7))
	rotate_object ("cut1",(0,10.4,0))
	boolean_difference("rise", "cut1")
	remove_object("cut1")
	move_object("rise",(12.35,0,5.12))
	build_cube("wing1",    (-3.6,-15.52,8), (12.9,5.4,11))
	build_cube("wing2",    (-3.6, 15.52,8), (12.9,5.4,11))
	build_cylinder("cyl1", (0,0,0), (5,5,60))
	rotate_object("cyl1",(90,0,0))
	move_object("cyl1", ( -3.2,0,9.04))
	boolean_difference("wing1", "cyl1")
	boolean_difference("wing2", "cyl1")
	remove_object("cyl1")

if True:
	build_cylinder("body", ( 0,0,0), (20,20,5))
	build_cube("cut2",   (15.1,0,0), (30,30,30))
	boolean_difference("body", "cut2")
	remove_object("cut2")
	build_cylinder("cut", ( 0,0,2), (14.5,14.5,100))
	boolean_difference("body", "cut")
	remove_object("cut")
	build_cube("stand1",   (0,0,0), (80,3,5))
	build_cube("stand2",   (0,0,0), (80,3,5))
	rotate_object("stand2",(0,0,-60))

	#join_list = ["stand1","stand2","body"]

###############################################################################################
###############################################################################################
if len(join_list) > 1:
	print ("\n\n\nJoining objects")
	for foo in join_list:
		print(foo)
	join_objects_by_name(join_list)
else:
	print ("Nothing to join")

bpy.context.space_data.params.filename = os.path.basename(__file__).replace(".py","")

exit(0)

