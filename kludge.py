#! /python37/python

import sys
import win32clipboard
import re

###############################################################################################
###############################################################################################

# get clipboard data
win32clipboard.OpenClipboard()
pattern = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

cblf = chr(13) + chr(10)
pattern = pattern.replace(cblf,"\n")



with open(r"C:\Users\roepe\Desktop\Imaging and Music\Blender\cornercap_body_vertices.csv", 'r') as content_file:
  f1 = content_file.read()

# make a dictionary
points = {}
iarray = f1.split("\n")

for foo in iarray:
  if len(foo) > 8:
    (k,x,y,z,trash) = foo.split(",")
    points[k] = x + chr(9) + y + chr(9) + z

t2=""  

for foo in pattern.split("\n"):
  foo = foo.upper()
  pts = foo.split(" ")
  for bar in pts:
	  if len(bar) > 0:
	    t2 += points[bar] + chr(9) + foo.replace(" ","") + "\n"
	    print(points[bar])

win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(t2)
win32clipboard.CloseClipboard()

