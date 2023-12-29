import random
from math import *
import bpy
import mathutils
from mathutils import Vector


###############################################################################################
###############################################################################################
def testfile():
    print ("check!")
    
###############################################################################################
###############################################################################################
def Deg2Rad(inX,inY,inZ):
    return (pi*inX/180,pi*inY/180,pi*inZ/180)


###############################################################################################
###############################################################################################
def rect(r, theta):
    # theta in degrees
    # returns tuple; (float, float); (x,y)
    
    x = r * cos(radians(theta))
    y = r * sin(radians(theta))
    return x,y

###############################################################################################
###############################################################################################
def polar(x,y):
  #returns r, theta(degrees)
  return hypot(x,y),degrees(atan2(y,x))

###############################################################################################
###############################################################################################
class Point(object):
    def __init__(self, x=None, y=None, r=None, theta=None):
        # x and y or r and theta(degrees)

        if x and y:
            self.c_polar(x, y)
        elif r and theta:
            self.c_rect(r, theta)
        else:
            raise ValueError('Must specify x and y or r and theta')
    def c_polar(self, x, y, f = polar):
        self._x = x
        self._y = y
        self._r, self._theta = f(self._x, self._y)
        self._theta_radians = radians(self._theta)
    def c_rect(self, r, theta, f = rect):
        # theta in degrees
        self._r = r
        self._theta = theta
        self._theta_radians = radians(theta)
        self._x, self._y = f(self._r, self._theta)
    def setx(self, x):
        self.c_polar(x, self._y)
    def getx(self):
        return self._x
    x = property(fget = getx, fset = setx)
    def sety(self, y):
        self.c_polar(self._x, y)
    def gety(self):
        return self._y
    y = property(fget = gety, fset = sety)
    def setxy(self, x, y):
        self.c_polar(x, y)
    def getxy(self):
        return self._x, self._y
    xy = property(fget = getxy, fset = setxy)
    def setr(self, r):
        self.c_rect(r, self._theta)
    def getr(self):
        return self._r
    r = property(fget = getr, fset = setr)
    def settheta(self, theta):
        self.c_rect(self._r, theta)
    def gettheta(self):
        return self._theta
    theta = property(fget = gettheta, fset = settheta)
    def set_r_theta(self, r, theta):
        self.c_rect(r, theta)
    def get_r_theta(self):
        return self._r, self._theta
    r_theta = property(fget = get_r_theta, fset = set_r_theta)
    def __str__(self):
        return '({},{})'.format(self._x, self._y)


###############################################################################################
###############################################################################################
def SetObjFrame(inObj, inLoc, inRot, inScale, inFrame):
        inObj.scale = inScale
        inObj.location = inLoc
        inObj.rotation_euler = inRot
        inObj.keyframe_insert(data_path="location", frame=inFrame)
        inObj.keyframe_insert(data_path="rotation_euler", frame=inFrame)
        inObj.keyframe_insert(data_path="scale", frame=inFrame)


###############################################################################################
###############################################################################################
def build_bulb(inBulb, inX, inY, inZ):

        bpy.ops.object.select_all(action="DESELECT")
        bpy.ops.object.select_pattern(pattern=inBulb)    # MUST EXIST
        bpy.ops.object.duplicate_move(OBJECT_OT_duplicate={"linked":False, "mode":'TRANSLATION'}
          , TRANSFORM_OT_translate={"value":(.1,.1,.1)
          , "constraint_axis":(False, False, False)
          #, "constraint_orientation":'GLOBAL'
          , "mirror":False
          #, "proportional":'DISABLED'
          , "proportional_edit_falloff":'SMOOTH'
          , "proportional_size":1
          , "snap":False
          , "snap_target":'CLOSEST'
          , "snap_point":(0, 0, 0)
          , "snap_align":False
          , "snap_normal":(0, 0, 0)
          , "gpencil_strokes":False
          , "texture_space":False
          , "remove_on_cancel":False
          , "release_confirm":False})

        for obj in bpy.context.selected_objects:
            currentname = obj.name
        print (currentname)
        print (obj.scale.x)        
        bpy.data.objects[currentname].location.xyz = (inX,inY,inZ)  
        return currentname


build_bulb("bulb_red"   , 0,0,0)
build_bulb("bulb_green" , 0,0,3)
build_bulb("bulb_blue"  , 0,0,6)
