#! /python37/python
"""

From the clipboard get sets of alpha points
etc. with spaces between points and newlines between faces.

example
a b c d
h ab l m

"""
import sys
import win32clipboard
import re

###############################################################################################
###############################################################################################

# get clipboard data
win32clipboard.OpenClipboard()
pattern = win32clipboard.GetClipboardData().upper()
win32clipboard.CloseClipboard()

cblf = chr(13) + chr(10)
pattern = pattern.replace(cblf,"\n")

print(pattern)  # DELETE ME


with open(r"C:\Users\roepe\Desktop\Imaging and Music\Blender\greggo.csv", 'r') as content_file:
  f1 = content_file.read().upper()
print (f1)
# make a dictionary
points = {}
iarray = f1.split("\n")

for foo in iarray:
  if len(foo) > 8:
    (k,x,y,z,trash) = foo.split(",")
    points[k] = (x + chr(9) + y + chr(9) + z).upper()

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

