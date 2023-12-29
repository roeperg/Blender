
from greg_blender import *

###############################################################################################
###############################################################################################
clearscreen()
print (sys.argv)
join_list = []

deselect_all()

if True:
	btm = 66
	top = 66
	side_height = 40
	total_y = 160
	edge = 3

	cutout_tuples = [
		(btm, 0.0, 0.0),
		(top, total_y, 0.0),
		(-top, total_y, 0.0),
		(-btm, 0.0, 0.0),
		]

	shape_tuples = [
		(btm+2, 0.0, 0.0),
		(top+2, total_y+4, 0.0),
		(-top-2, total_y+4, 0.0),
		(-btm-2, 0.0, 0.0),
		]

	edges = [
			1, 2,
			2, 3,
			3, 4,
			4, 1
		]

	build_extruded_plane(
									 cutout_tuples                    # list of vertexes tuples.  3 numbers (x,y,z) for each vertex.
								 , edges                            # list of point offsets for each segment
								 , (0,0,side_height*10)                     # 3 member tuple for extrusion
								 , "cutout" )

	build_extruded_plane(
									 shape_tuples                     # list of vertexes tuples.  3 numbers (x,y,z) for each vertex.
								 , edges                            # list of point offsets for each segment
								 , (0,0,side_height)                        # 3 member tuple for extrusion
								 , "shape" )

	move_object("shape", (0,0,0))
	move_object("cutout", (0,0,0))

	boolean_difference("shape", "cutout")
	remove_object("cutout")

	build_cube("sep", ( 20,0,0), (2,160,side_height))

if False:
	btm = 48
	top = 30
	total_y = 57
	edge = 2

	cutout_tuples = [
		(btm, 0.0, 0.0),
		(top, total_y, 0.0),
		(-top, total_y, 0.0),
		(-btm, 0.0, 0.0),
		]

	shape_tuples = [
		(btm+2, 0.0, 0.0),
		(top+2, total_y+3, 0.0),
		(-top-2, total_y+3, 0.0),
		(-btm-2, 0.0, 0.0),
		]

	edges = [
			1, 2,
			2, 3,
			3, 4,
			4, 1
		]

	build_extruded_plane(
									 cutout_tuples                    # list of vertexes tuples.  3 numbers (x,y,z) for each vertex.
								 , edges                            # list of point offsets for each segment
								 , (0,0,side_height)                     # 3 member tuple for extrusion
								 , "cutout2" )

	build_extruded_plane(
									 shape_tuples                     # list of vertexes tuples.  3 numbers (x,y,z) for each vertex.
								 , edges                            # list of point offsets for each segment
								 , (0,0,side_height)                        # 3 member tuple for extrusion
								 , "shape2" )

	move_object("shape2", (0,-46,0))
	move_object("cutout2", (0,-46,2))

	boolean_difference("shape2", "cutout2")
	remove_object("cutout2")

	build_cube("top2", ( -10.005,108.6,0), (164,2,side_height))
	build_cube("bot2", ( -10.005,-74,0), (164,2,side_height))
	build_cube("right", (71,17.4,0), (2,184.3,side_height))
	build_cube("left", ( -91.004,17.4,0), (2,184.3,side_height))

	join_list = ["shape","shape2","top2","bot2","right","left"]

###############################################################################################
###############################################################################################
if len(join_list) > 1:
	print ("\n\n\nJoining objects")
	for foo in reversed(join_list):
		print(foo)
	join_objects_by_name(join_list)
else:
	print ("Nothing to join")

# save blend
#bpy.ops.wm.save_mainfile()
basename = __file__[:-3]
bpy.ops.wm.save_as_mainfile(filepath=basename + ".blend")
bpy.ops.export_mesh.stl(filepath=basename + ".stl")
exit(0)

