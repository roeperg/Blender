from PIL import Image
import sys

def cut_image(file1, rows, columns):

    image1 = Image.open(file1)

    (width, height) = image1.size

    result_width  = width/rows
    result_height = height/columns

    print "height and width of each image will be %d %d" %(result_height, result_width)

    for foo in range(0,rows):
      for goo in range(0,columns):
        result = Image.new('RGB', (result_width, result_height))
        newimage = image1.crop((
                                (1+(foo*result_width))
                              , (1+(goo*result_height))
                              , ((foo+1)*result_width)
                              , ((goo+1)*result_height)
                              ))
        #result.paste(im=newimage, box=(0,0))
        newimage.thumbnail((30,30), Image.ANTIALIAS)
        newimage.save(r"h:\blender\%d%d_%s" %(goo+1,foo+1,file1) )
        newimage=None
##############################################################################################

cut_image(sys.argv[1],3,3)


"""
w, h = yourImage.size
yourImage.crop((0, 30, w, h-30)).save(...)
"""
