import bpy

def createMaterials():
  # Image texture
  imgPath = r"C:\Users\roepe\Desktop\Imaging\Blender\rubik_images\1-ul-_rise.jpg"
  img = bpy.data.add_image(imgPath)
  imtex = bpy.data.textures.new('ImageTex')
  imtex.type = 'IMAGE'
  imtex = imtex.recast_type()
  imtex.image = img
  
  # Marble texture
  mbtex = bpy.data.textures.new('MarbleTex')
  mbtex.type = 'MARBLE'
  mbtex = mbtex.recast_type()
  mbtex.noise_depth = 1
  mbtex.noise_size = 1.6
  mbtex.noisebasis2 = 'SIN'
  mbtex.turbulence = 5
  
  # Cloud texture
  cltex = bpy.data.textures.new('CloudsTex')
  cltex.type = 'CLOUDS'
  # Cloud texture by default, don't need to recast
  cltex.noise_basis = 'BLENDER_ORIGINAL'
  cltex.noise_size = 1.05
  cltex.noise_type = 'SOFT_NOISE'
  
  # Create new material
  mat = bpy.data.materials.new('TexMat')
  mat.alpha = 0
  
  # Map image to color, this is the default
  mat.add_texture(texture = imtex, texture_coordinates = 'UV')
  im_mtex = mat.textures[0]
  
  # Map marble to specularity
  mat.add_texture(texture = mbtex, texture_coordinates = 'UV', map_to = 'SPECULARITY')
  mb_mtex = mat.textures[1]
  
  # Map cloud to alpha, reflection and normal, but not diffuse
  mat.add_texture(texture = cltex, texture_coordinates = 'UV', map_to = 'ALPHA')
  cl_mtex = mat.textures[2]
  cl_mtex.map_reflection = True
  cl_mtex.map_normal = True
  
  # Create new material
  mat2 = bpy.data.materials.new('Blue')
  mat2.diffuse_color = (0.0, 0.0, 1.0)
  mat2.specular_color = (1.0, 1.0, 0.0)
  
  # Pick active object, remove its old material (assume exactly one old material).
  ob = bpy.context.object
  bpy.ops.object.material_slot_remove()
  
  # Add the two materials to mesh
  me = ob.data
  me.add_material(mat)
  me.add_material(mat2)
  
  return

createMaterials()