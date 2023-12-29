import bpy
import numpy

def extrude_plane(ext):
  bpy.ops.object.editmode_toggle()
  bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False
                                      , "mirror":False}
                                      , TRANSFORM_OT_translate={"value":ext
                                      , "orient_type":'LOCAL'
                                      , "orient_matrix":((1, 0, 0), (0 , 1, 0), (0, 0, 1))
                                      , "orient_matrix_type":'LOCAL'
                                      , "constraint_axis":(False, False, True)
                                      , "mirror":False
                                      , "use_proportional_edit":False
                                      , "proportional_edit_falloff":'SMOOTH'
                                      , "proportional_size":1
                                      , "use_proportional_connected":False
                                      , "use_proportional_projected":False
                                      , "snap":False
                                      , "snap_target":'CLOSEST'
                                      , "snap_point":(0, 0, 0)
                                      , "snap_align":False
                                      , "snap_normal":(0, 0, 0)
                                      , "gpencil_strokes":False
                                      , "cursor_transform":False
                                      , "texture_space":False
                                      , "remove_on_cancel":False
                                      , "release_confirm":False
                                      , "use_accurate":False})
  bpy.ops.object.editmode_toggle()
  return

# Note: we DELETE all objects in the scene and only then create the new mesh!
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Vertices and edges (straightforward)

vertices = numpy.array([
    # rectangle
    0, 0, 0,
    2, 0, 0,
    2, 2, 0,
    0, 2, 0,
    # triangle
    1, 3, 0,
], dtype=numpy.float32)

# Setting edges is optional, as they get created automatically for
# any provided polygons. However, if you need edges that exist separately
# from polygons then use this array.
# XXX these edges only seem to show up after going in-and-out of edit mode.
#edges = numpy.array([
#    0, 1,
#    1, 2,
#    2, 3,
#    3, 0
#], dtype=numpy.int32)

num_vertices = vertices.shape[0] // 3
#num_edges = edges.shape[0] // 2

# Polygons are defined in loops. Here, we define one quad and one triangle

vertex_index = numpy.array([
    0, 1, 2, 3,
    4, 3, 2,
    #0, 5, 1
], dtype=numpy.int32)

# For each polygon the start of its vertex indices in the vertex_index array
loop_start = numpy.array([
    0, 4
], dtype=numpy.int32)

# Length of each polygon in number of vertices
loop_total = numpy.array([
    4, 3
], dtype=numpy.int32)

num_vertex_indices = vertex_index.shape[0]
num_loops = loop_start.shape[0]

## Texture coordinates per vertex *per polygon loop*.
#uv_coordinates = numpy.array([
#    0, 0,
#    1, 0,
#    1, 1,
#    0, 1,
#
#    0.5, 1,
#    0, 0,
#    1, 0,
#
#    0, 1,
#    0.5, 0,
#    1, 1
#], dtype=numpy.float32)
#
## Vertex color per vertex *per polygon loop*
#vertex_colors = numpy.array([
#    1, 0, 0,
#    1, 0, 0,
#    1, 0, 0,
#    1, 0, 0,
#
#    0, 1, 0,
#    0, 1, 0,
#    0, 1, 0,
#
#    1, 0, 0,
#    0, 1, 0,
#    0, 0, 1
#], dtype=numpy.float32)

#print ("greg")
#print(uv_coordinates.shape[0])
#print(vertex_index.shape[0])
#print ("greg")

#assert uv_coordinates.shape[0] == 2*vertex_index.shape[0]
#assert vertex_colors.shape[0] == 3*vertex_index.shape[0]

# Create mesh object based on the arrays above

mesh = bpy.data.meshes.new(name='created mesh')

mesh.vertices.add(num_vertices)
mesh.vertices.foreach_set("co", vertices)

#mesh.edges.add(num_edges)
#mesh.edges.foreach_set("vertices", edges)

mesh.loops.add(num_vertex_indices)
mesh.loops.foreach_set("vertex_index", vertex_index)

mesh.polygons.add(num_loops)
mesh.polygons.foreach_set("loop_start", loop_start)
mesh.polygons.foreach_set("loop_total", loop_total)

## Create UV coordinate layer and set values
#uv_layer = mesh.uv_layers.new()
#for i, uv in enumerate(uv_layer.data):
#    uv.uv = uv_coordinates[2*i:2*i+2]
#
## Create vertex color layer and set values
#vcol_lay = mesh.vertex_colors.new()
#for i, col in enumerate(vcol_lay.data):
#    col.color[0] = vertex_colors[3*i+0]
#    col.color[1] = vertex_colors[3*i+1]
#    col.color[2] = vertex_colors[3*i+2]
#    col.color[3] = 1.0                     # Alpha?
#
# We're done setting up the mesh values, update mesh object and
# let Blender do some checks on it
mesh.update()
mesh.validate()

# Create Object whose Object Data is our new mesh
obj = bpy.data.objects.new('created object', mesh)

# Add *Object* to the scene, not the mesh
scene = bpy.context.scene
scene.collection.objects.link(obj)

# Select the new object and make it active
bpy.ops.object.select_all(action='DESELECT')
obj.select_set(True)
bpy.context.view_layer.objects.active = obj

extrude_plane((0,0,5))

#GREGGOobj.editmode_toggle()
#GREGGObpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False
#GREGGO                                    , "mirror":False}
#GREGGO                                    , TRANSFORM_OT_translate={"value":(1, 0, 3)
#GREGGO                                    , "orient_type":'LOCAL'
#GREGGO                                    , "orient_matrix":((1, 0, 0), (0 , 1, 0), (0, 0, 1))
#GREGGO                                    , "orient_matrix_type":'LOCAL'
#GREGGO                                    , "constraint_axis":(False, False, True)
#GREGGO                                    , "mirror":False
#GREGGO                                    , "use_proportional_edit":False
#GREGGO                                    , "proportional_edit_falloff":'SMOOTH'
#GREGGO                                    , "proportional_size":1
#GREGGO                                    , "use_proportional_connected":False
#GREGGO                                    , "use_proportional_projected":False
#GREGGO                                    , "snap":False
#GREGGO                                    , "snap_target":'CLOSEST'
#GREGGO                                    , "snap_point":(0, 0, 0)
#GREGGO                                    , "snap_align":False
#GREGGO                                    , "snap_normal":(0, 0, 0)
#GREGGO                                    , "gpencil_strokes":False
#GREGGO                                    , "cursor_transform":False
#GREGGO                                    , "texture_space":False
#GREGGO                                    , "remove_on_cancel":False
#GREGGO                                    , "release_confirm":False
#GREGGO                                    , "use_accurate":False})
#GREGGOobj.editmode_toggle()

bpy.ops.wm.save_as_mainfile(filepath=r"C:\Users\roepe\Desktop\Imaging and Music\Blender\surf.blend")

exit(0)

