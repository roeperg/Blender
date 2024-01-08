
from greg_blender import *
import bpy
import random
import pathlib
import os
import math
cwd = os. getcwd()

C = bpy.context
join_list = []

output_blend =  pathlib.PurePath(__file__).stem

delete_all_objects()

thick = 5.9
half_thick = 5.9/2

if True:
	build_cube("base", (0, 0, (half_thick)), (12, thick, thick))
	build_cylinder("shaft", (40, 0, (half_thick)), (thick, thick, 80), VERTICES=128, ROTATION=(0, 90, 0))
print ("\n\n\n%s/%s.blend\n\n\n" %(cwd, output_blend))
bpy.ops.wm.save_as_mainfile(filepath="%s/%s.blend" %(cwd, output_blend))

#remove_object("cutout")

"""
import addons
	preferences   import =export: import images a planes

	add plane  90% along y access
	add image as plane
	choose picture
	align to plane and overlap it
	size image
	CAN JUST TRIM IMAGE in PLACE WHICH LEAVES IT TEXTURED.  :)
"""

"""
location 12, 9, 0
scale 2.5
text
"""

