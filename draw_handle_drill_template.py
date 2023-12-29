
from greg_blender import *
import bpy
import random
import pathlib

C = bpy.context

output_blend =  pathlib.PurePath(__file__).stem

delete_all_objects()
join_list = []

if True:
	print("\n"*3, "Starting", "\n"*3)
	build_cube("template", (0, 0, 0), (130, 25, 3))

	build_cylinder("drillhole", ( 0, 0, 0), (5, 5, 10), VERTICES=128)
	build_cylinder("peephole", ( 0, 0, 0), (10, 10, 10), VERTICES=128)
	build_cylinder("level", ( 0, 0, 0), (6.5, 6.5, 28), VERTICES=128)
	rotate_object ("level", (0, 90, 0))
	move_object ("level", ( 0, 12.5, 3))

	boolean_difference("template", "level")
	boolean_difference("template", "peephole")
	move_object ("drillhole", ( 48, 0, 0))
	boolean_difference("template", "drillhole")
	move_object ("drillhole", (-48, 0, 0))
	boolean_difference("template", "drillhole")

	remove_object("level")
	remove_object("peephole")
	remove_object("drillhole")

if False:
	move_object("template", (0, 12.5, 0))
	build_cube("bubble", (0, 1, 6), (48, 2, 8))
	join_objects_by_name(["bubble", "template"])

bpy.ops.wm.save_as_mainfile(filepath=r"C:\Users\roepe\Desktop\Imaging and Music\Blender\%s.blend" %output_blend)

