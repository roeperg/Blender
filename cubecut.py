from PIL import Image
import fnmatch
import glob
import os
import sys
import platform


from PIL import Image
import sys

def cut_image(file1):

    starts = {
        "1-ul-":[0  ,0]
      , "2-um-":[105,0]
      , "3-ur-":[210,0]
      , "4-ml-":[0  ,105]
      , "5-mm-":[105,105]
      , "6-mr-":[210,105]
      , "7-ll-":[0  ,210]
      , "8-lm-":[105,210]
      , "9-lr-":[210,210]
    }
    Lydia = Image.open(file1)

    (width, height) = Lydia.size

    Diana = max(float(width),float(height))

    print Diana
    
    Fiona = 300/Diana
    
    result_width  = int(Lydia.size[0]*Fiona)
    result_height = int(Lydia.size[1]*Fiona)
    print "  LARGE", Diana, Fiona, "(",int(Lydia.size[0]*Fiona),int(Lydia.size[1]*Fiona),")"
    
    print "height and width of each image will be %d %d" %(result_height, result_width)

    Lydia.thumbnail(((result_width,result_height)), Image.ANTIALIAS)

    base_image = Image.new('RGB', (300, 300))

    place_width  = 150-(result_width/2)
    place_height = 150-(result_height/2)
     
    base_image.paste(Lydia,(place_width,place_height))

    for foo in starts.keys():
      newimage = base_image.crop((
                              starts[foo][0]
                            , starts[foo][1]
                            , starts[foo][0]+90
                            , starts[foo][1]+90
                            ))
      newimage.thumbnail(((30,30)), Image.ANTIALIAS)
      newimage.save(r"C:\Users\roepe\Desktop\Imaging\Blender\rubik_images\%s_%s" %(foo,os.path.basename(file1)) )
      newimage=None
##############################################################################################

cut_image(sys.argv[1])

exit(0)


 