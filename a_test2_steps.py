import win32clipboard


currx = -2.886
curry = -2
xypoints=[  
  [-2.886,-1.52, 8]
, [-2.72,-1.34, 4]
, [-2.72, 0.0, 23]
, [-2.48, 0.0, 4]
, [-2.48, 0.164, 4]
, [ 2.00, 0.164, 100]
, [ 2.00, -.048, 4]
]
cnt = 0
target="xypoints=[  [%2.4f,%2.4f]"%(-2.886,-2)
for foo in xypoints:
	steps = foo[2]
	stepx = (foo[0]-currx)/foo[2]
	stepy = (foo[1]-curry)/foo[2]
	for goo in range(0,steps):
		cnt += 1
		currx += stepx
		curry += stepy
		target += " ,[%2.4f,%2.4f]"%(currx, curry)

target += "]\n"
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(target)
win32clipboard.CloseClipboard()
print cnt
	