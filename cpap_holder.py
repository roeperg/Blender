
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
	build_cube("main", (0,0,0), (44,58,70))
	build_cube("cut" , (0,0,6), (32,70,70))
	boolean_difference("main", "cut")
	remove_object("cut")

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

