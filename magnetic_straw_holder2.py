
from greg_blender import *

###############################################################################################
###############################################################################################
clearscreen()
print (sys.argv)
join_list = []

verts = 128
smoothit = False

#   inside is 32mm x 46mm x 70mm
deselect_all()
if True:
	build_cylinder("main", ( 0,0,0), (10.5,10.5,5.2))
	build_cylinder("cut2", ( 0,0,0), (8.2,8.2,10))
	build_cube("cut1" , (0,0,0), (20,2,2.15))
	move_object("cut1", (0,0,1.8))
	#boolean_difference("main", "cut1")
	boolean_difference("main", "cut2")
	#remove_object("cut1")
	remove_object("cut2")

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

