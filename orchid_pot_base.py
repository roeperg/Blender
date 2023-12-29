
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
	build_cube("floor", (0,0,0), (130,130,4))
	build_cube("rs", (63,0,5.5), (4,130,15))
	build_cube("ls", (-63,0,5.5), (4,130,15))
	build_cube("bs", (0,63,5.5), (130, 4,15))
	build_cube("fs", (0,-63,3), (130, 4,10))

if False:
	build_cube("fc1", (0,0,0), (5,30,15))
	build_cube("fc2", (0,0,0), (5,30,15))
	build_cube("c1", (-1.95,0,0), (5,26,25))
	build_cube("c2", (0,0,0), (30,10,25))
	boolean_difference("fc1", "c1")
	boolean_difference("fc1", "c2")
	boolean_difference("fc2", "c1")
	boolean_difference("fc2", "c2")

	remove_object("c1")
	remove_object("c2")

	move_object("fc1", (67.5, 40,5.5))
	move_object("fc2", (67.5,-40,5.5))

if False:
	# hole 26x2
	build_cube("mc1", (0,0,0), (1.90,23,15))
	move_object("mc1", (-68.4, 40,5.5))
	build_cube("mc2", (0,0,0), (6,9,15))
	move_object("mc2", (-66.016, 40,5.5))

	build_cube("mc3", (0,0,0), (1.90,23,15))
	move_object("mc3", (-68.4, -40,5.5))
	build_cube("mc4", (0,0,0), (6,9,15))
	move_object("mc4", (-66.016, -40,5.5))

	#join_list = ["floor","ls","rs","bls","brs","b"]

	"""
	build_cube("cut", (4,0,2), (44,35, 8))
	build_cube("cut2", (-18.5,-1.5,4), (8,32, 6))

	boolean_difference("case", "cut")
	boolean_difference("case", "cut2")
	remove_object("cut")
	remove_object("cut2")
	"""

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

