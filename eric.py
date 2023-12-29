
from greg_blender import *

###############################################################################################
###############################################################################################
clearscreen()

join_list = []

verts = 128
smoothit = False

deselect_all()

build_cylinder("cyl1", (0,-0,0),(3.2,7.5,40), SMOOTH=False)
rotate_object ("cyl1",(90,0,0))
build_sphere("cap1", (0,20,0), (3.2,7.5,3.2), SMOOTH=False)
rotate_object ("cap1",(90,0,0))
build_sphere("cap2", (0,-20,0), (3.2,7.5,3.2), SMOOTH=False)
rotate_object ("cap2",(90,0,0))
join_objects_by_name (["cyl1","cap1","cap2"])
move_object("cyl1",(13.5,0,0))

build_cylinder("cyl2", (0,-0,0),(3.2,7.5,40), SMOOTH=False)
rotate_object ("cyl2",(90,0,0))
build_sphere("cap1", (0,20,0), (3.2,7.5,3.2), SMOOTH=False)
rotate_object ("cap1",(90,0,0))
build_sphere("cap2", (0,-20,0), (3.2,7.5,3.2), SMOOTH=False)
rotate_object ("cap2",(90,0,0))
join_objects_by_name (["cyl2","cap1","cap2"])
move_object("cyl2",(-13.5,0,0))

build_cylinder("cyl3", (0,-0,0),(3.2,7.5,27), SMOOTH=False)
rotate_object ("cyl3",(90,0,90))
move_object("cyl3",(0,20,0))

build_cylinder("cyl4", (0,-0,0),(3.2,7.5,27), SMOOTH=False)
rotate_object ("cyl4",(90,0,90))
move_object("cyl4",(0,-20,0))

extrude_tuple = (0,0,40)  # ( extrude only along Z)

join_list = ["cyl1","cyl2","cyl3","cyl4"]

if False:
	btm = 66
	top = 66
	side_height = 40
	total_y = 160
	edge = 3

	cutout_tuples = [
		(0.0, 0.0, 0.0),
		(0.0, 30, 0.0),
		(42, 30, 0.0),
		(42, 0, 0.0),
	]

	edges = [
		5, 6,
		6, 7,
		5, 7

	]

	build_extruded_plane( cutout_tuples, edges, (0,0,3), "base")

	"""
	rotate_object("triangle_base",Deg2Rad(0,0,-90))
	move_object("triangle_base",(0,-30,17.43845))
	build_cylinder("cyl1", (0,-35,0),(17,17,150))
	boolean_difference("triangle_base", "cyl1")
	remove_object("cyl1")
	join_list.append("triangle_base")
	"""

if False:
	build_cube("base",  (0,0,0), (42,29, 54.3))
	#move_object("base", (0,0,-24))
	#build_cube("base2", (0,0,0), (32,26, 54.3))
	#join_objects_by_name(["base","base2"])

	build_cube("hollow", (0,0,0), (36,23,27))
	move_object("hollow", (0,0,-16))
	boolean_difference("base", "hollow")
	remove_object("hollow")

	build_cube("hollow", (0,0,0), (60,14.6,16))
	move_object("hollow", (0,0,-12))
	boolean_difference("base", "hollow")
	remove_object("hollow")

	build_cube("hollow", (0,0,0), (60,16,40))
	move_object("hollow", (0,12,23))
	boolean_difference("base", "hollow")
	remove_object("hollow")

	build_cube("hollow", (0,0,0), (60,16,40))
	move_object("hollow", (0,-16,23))
	boolean_difference("base", "hollow")
	remove_object("hollow")

	build_cylinder("inner", (0,0,0), (6.8,6.8,30), ROTATION=(90,0,0), SMOOTH=False)
	move_object("inner", (0,-12,18))

	build_cylinder("outer", (0,0,0), (14,14,10), ROTATION=(90,0,0), SMOOTH=False)
	move_object("outer", (0,-8,18))

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

