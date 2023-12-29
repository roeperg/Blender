import bpy
def view3d_find( return_area = False ):
    # returns first 3d view, normally we get from context
    for area in bpy.context.window.screen.areas:
        if area.type == 'VIEW_3D':
            v3d = area.spaces[0]
            rv3d = v3d.region_3d
            for region in area.regions:
                if region.type == 'WINDOW':
                    if return_area: return region, rv3d, v3d, area
                    return region, rv3d, v3d
    return None, None

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

bpy.ops.mesh.primitive_cube_add()
bpy.context.object.dimensions[0] = 1
bpy.ops.object.editmode_toggle()

region, rv3d, v3d, area = view3d_find(True)

override = {
    'scene'  : bpy.context.scene,
    'region' : region,
    'area'   : area,
    'space'  : v3d
}
print("20 cuts are expected")
bpy.ops.mesh.loopcut_slide(
    override,
    MESH_OT_loopcut = {
        "number_cuts"           : 20,
        "smoothness"            : 0,
        "falloff"               : 'SMOOTH',  # Was 'INVERSE_SQUARE' that does not exist
        "edge_index"            : 2,
        "mesh_select_mode_init" : (True, False, False)
    },
    TRANSFORM_OT_edge_slide = {
        "value"           : 0,
        "mirror"          : False,
        "snap"            : False,
        "snap_target"     : 'CLOSEST',
        "snap_point"      : (0, 0, 0),
        "snap_align"      : False,
        "snap_normal"     : (0, 0, 0),
        "correct_uv"      : False,
        "release_confirm" : False
    }
)

bpy.ops.object.editmode_toggle()

bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Subdivision")

bpy.ops.wm.save_as_mainfile(filepath=r"C:\Users\groeper\Desktop\Imaging and Music\Blender\greggo.blend")

