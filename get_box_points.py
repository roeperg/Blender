#! /python37/python

import sys

###############################################################################################
###############################################################################################

trash = sys.argv.pop(0)
filename = sys.argv.pop(0)
pattern = sys.argv

if len(pattern) != 3:
  print ("Usage: %s length width height" %trash)
  exit(0)

LWH="LWH"

# make a dictionary

p1 = "%s,%s,%s" %("0","0","0")
p2 = "%s,%s,%s" %(pattern[0],"0","0")
p3 = "%s,%s,%s" %(pattern[0],pattern[1],"0")
p4 = "%s,%s,%s" %("0",pattern[1],"0")
p5 = "%s,%s,%s" %("0","0",pattern[2])
p6 = "%s,%s,%s" %(pattern[0],"0",pattern[2])
p7 = "%s,%s,%s" %(pattern[0],pattern[1],pattern[2])
p8 = "%s,%s,%s" %("0",pattern[1],pattern[2])



s1  = "A,%s,bottom\n" %p1
s1 += "B,%s,bottom\n" %p2
s1 += "C,%s,bottom\n" %p3
s1 += "D,%s,bottom\n" %p4

#s2  = "E,%s,top\n" %("0","0",pattern[2])
#s2 += "F,%s,top\n" %(pattern[0],"0",pattern[2])
#s2 += "G,%s,top\n" %(pattern[0],pattern[1],pattern[2])
#s2 += "H,%s,top\n" %("0",pattern[1],pattern[2])
#
#s3  = "I,%s,side1\n" %("0","0","0")
#s3 += "J,%s,side1\n" %(pattern[0],"0","0")
#s3 += "K,%s,side1\n" %(pattern[0],"0",pattern[2])
#s3 += "L,%s,side1\n" %("0","0",pattern[2])
#
#s4  = "I,%s,side2\n" %("0",pattern[1],"0")
#s4 += "J,%s,side2\n" %(pattern[0],pattern[1],"0")
#s4 += "K,%s,side2\n" %(pattern[0],pattern[1],pattern[2])
#s4 += "L,%s,side2\n" %("0",pattern[1],pattern[2])
#
#s5  = "M,%s,front\n" %("0","0","0")
#s5 += "N,%s,front\n" %("0",pattern[1],"0")
#s5 += "O,%s,front\n" %("0",pattern[1],pattern[2])
#s5 += "P,%s,front\n" %("0","0",pattern[2])
#
#s6  = "Q,%s,front\n" %(pattern[0],"0","0")
#s6 += "R,%s,front\n" %(pattern[0],pattern[1],"0")
#s6 += "S,%s,front\n" %(pattern[0],pattern[1],pattern[2])
#s6 += "T,%s,front\n" %(pattern[0],"0",pattern[2])

output  ="Point	x	y	z	Face\n"  
output += s1
#output += s2
#output += s3
#output += s4
#output += s5
#output += s6

OUT=open(filename,"wt")
OUT.writelines(output)
OUT.close()

pov  = """text {ttf "arial.ttf" "A" .1, 0 pigment { Black } translate <%s> scale 2  }\n""" %p1
pov += """text {ttf "arial.ttf" "B" .1, 0 pigment { Black } translate <%s> scale 2  }\n""" %p2
pov += """text {ttf "arial.ttf" "C" .1, 0 pigment { Black } translate <%s> scale 2  }\n""" %p3
pov += """text {ttf "arial.ttf" "D" .1, 0 pigment { Black } translate <%s> scale 2  }\n""" %p4
pov += """text {ttf "arial.ttf" "E" .1, 0 pigment { Black } translate <%s> scale 2  }\n""" %p5
pov += """text {ttf "arial.ttf" "F" .1, 0 pigment { Black } translate <%s> scale 2  }\n""" %p6
pov += """text {ttf "arial.ttf" "G" .1, 0 pigment { Black } translate <%s> scale 2  }\n""" %p7
pov += """text {ttf "arial.ttf" "H" .1, 0 pigment { Black } translate <%s> scale 2  }\n""" %p8


#pov  = "sphere { <%s> 0.50  texture { pigment { color %s } }}\n" %(p1,"Red")                 
#pov += "sphere { <%s> 0.50  texture { pigment { color %s } }}\n" %(p2,"Green")          
#pov += "sphere { <%s> 0.50  texture { pigment { color %s } }}\n" %(p3,"Blue")   
#pov += "sphere { <%s> 0.50  texture { pigment { color %s } }}\n" %(p4,"Yellow")
#pov += "sphere { <%s> 0.50  texture { pigment { color %s } }}\n" %(p5,"Red")
#pov += "sphere { <%s> 0.50  texture { pigment { color %s } }}\n" %(p6,"Green")
#pov += "sphere { <%s> 0.50  texture { pigment { color %s } }}\n" %(p7,"Blue")
#pov += "sphere { <%s> 0.50  texture { pigment { color %s } }}\n" %(p8,"Yellow")
#
#pov += "cylinder { <%s>  <%s> 0.30  texture { pigment { color %s } }}\n"   %(p1,p2,"Cyan")
#pov += "cylinder { <%s>  <%s> 0.30  texture { pigment { color %s } }}\n"   %(p2,p3,"Cyan")
#pov += "cylinder { <%s>  <%s> 0.30  texture { pigment { color %s } }}\n"   %(p3,p4,"Cyan")
#pov += "cylinder { <%s>  <%s> 0.30  texture { pigment { color %s } }}\n"   %(p4,p1,"Cyan")
#
#pov += "cylinder { <%s>  <%s> 0.30  texture { pigment { color %s } }}\n"   %(p1,p3,"Red")
#pov += "cylinder { <%s>  <%s> 0.30  texture { pigment { color %s } }}\n"   %(p3,p8,"Red")
#pov += "cylinder { <%s>  <%s> 0.30  texture { pigment { color %s } }}\n"   %(p8,p4,"Red")
#pov += "cylinder { <%s>  <%s> 0.30  texture { pigment { color %s } }}\n"   %(p4,p1,"Red")





OUT=open("teststuff.inc","wt")
OUT.writelines(pov)
OUT.close()


#declare Green   = rgb <0, 1, 0>;
#declare Blue    = rgb <0, 0, 1>;
#declare Yellow  = rgb <1,1,0>;
#declare Cyan    = rgb <0, 1, 1>;
#declare Magenta = rgb <1, 0, 1>;
#declare Clear   = rgbf 1;
#declare White   = rgb 1;
#declare Black   = rgb 0;

