
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
	build_cube("main", (0,0,0), (32,20,80))
	build_cube("cut" , (0,0,0), (20,70,80))
	move_object("cut", (0,0,6))
	boolean_difference("main", "cut")
	remove_object("cut")
	rotate_object("main",(90,0,0))
	build_cube("hook",(8,60,0),(16,50,20))
	join_list = ['hook','main']

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

