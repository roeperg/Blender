
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
	build_cylinder("rim", ( 0,0,-3.2), (15,15,2))
	build_cylinder("body", ( 0,0,0), (12,12,7.2))
	build_cylinder("cut", ( 0,0,2), (8.18,8.18,10))
	boolean_difference("rim", "cut")
	boolean_difference("body", "cut")
	remove_object("cut")
	join_list = ["body","rim"]

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

