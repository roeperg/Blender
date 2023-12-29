import sys
sys.path.append('/.../application/app/folder')
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
if False:
	build_cylinder("main", ( 0,0,0), (10.5,10.5,5.2))
	build_cylinder("cut2", ( 0,0,0), (8.2,8.2,10))
	build_cube("cut1" , (0,0,0), (20,2,2.15))
	move_object("cut1", (0,0,-1.607))
	#boolean_difference("main", "cut1")
	boolean_difference("main", "cut2")
	#remove_object("cut1")
	remove_object("cut2")

vert_dict = {
'A':(0,0,0),
'B':(10,0,0),
'C':(10,10,0),
'D':(0,10,0),
'E':(0,0,15),
'F':(10,0,12),
'G':(10,10,8),
'H':(0,10,6),
'I':(5,-8,0),
'J':(25,5,5),
}

face_list = [
'ADCBI',
'ADHE',
'CDHG',
'EFGH',
'AIBFE',
'BFJ',
'CGJ',
'GFJ',
'BCJ',
]


print(vert_dict)
print(face_list)

verts = []
faces = []
pcount=0
for foo in face_list:
	flist=[]
	for bar in foo:
		flist.append(pcount)
		pcount += 1
		verts.append(vert_dict[bar])
	faces.append(tuple(flist))	
print ("\n\n")
print(verts)
print ("\n\n")
print(faces)
print ("\n\n") 


#base_framework("greggo", "greggo.csv")
#base_points("points.csv")

show_mesh_verts(vert_dict)
solid_from_points('thegreg', verts, faces)

build_cylinder("body", ( 5,0,5), (2,2,50),ROTATION=(0,90,90))
boolean_difference("thegreg", "body")
remove_object("body")
###############################################################################################
###############################################################################################
if len(join_list) > 1:
	print ("\n\n\nJoining objects")
	for foo in join_list:
		print(foo)
	join_objects_by_name(join_list)
else:
	print ("Nothing to join")


save_files(__file__.replace(".py",".blend"))
# save_files(os.path.basename(__file__).replace(".py",".blend"))

exit(0)

