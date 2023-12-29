#! /python37/python

import sys
import win32clipboard
import re



###############################################################################################
###############################################################################################

trash = sys.argv.pop(0)
pattern = sys.argv

with open(r"C:\Users\roepe\Desktop\Imaging and Music\Blender\greggo.csv", 'r') as content_file:
  f1 = content_file.read()

# make a dictionary
points = {}
iarray = f1.split("\n")

for foo in iarray:
  if len(foo) > 8:
    (k,x,y,z,trash) = foo.split(",")
    points[k] = x + chr(9) + y + chr(9) + z

t2=""  

for foo in pattern:
  foo = foo.upper()
  t2 += points[foo] + "\n"
  print(points[foo])

win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(t2)
win32clipboard.CloseClipboard()

