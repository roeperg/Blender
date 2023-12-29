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

# Vertices and edges (straightforward)

vertices = numpy.array([
    # rectangle
    0, 0, 0,
    2, 0, 0,
    3, 1, 0,
    2, 2, 0,
    0, 2, 0,
], dtype=numpy.float32)

num_vertices = vertices.shape[0] // 3

# Polygons are defined in loops. Here, we define one quad and one triangle

vertex_index = numpy.array([
    0, 1, 2, 3,4
], dtype=numpy.int32)

# For each polygon the start of its vertex indices in the vertex_index array
loop_start = numpy.array([
    0
], dtype=numpy.int32)

# Length of each polygon in number of vertices
loop_total = numpy.array([
    5
], dtype=numpy.int32)

num_vertex_indices = vertex_index.shape[0]
num_loops = loop_start.shape[0]


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

extrude_plane((0,0,3))

bpy.ops.wm.save_as_mainfile(filepath=r"C:\Users\roepe\Desktop\Imaging and Music\Blender\surf.blend")

exit(0)
