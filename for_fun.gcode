; Bed leveling Ender 3 by ingenioso3D

G90

G28 ; Home all axis
G1 Z5 ; Lift Z axis
G1 X32 Y36 ; Move to Position 1
G1 Z0
G1 Z30 ; Lift Z axis
G1 X32 Y206 ; Move to Position 2
G1 Z0
G1 Z15 ; Lift Z axis
G1 X202 Y206 ; Move to Position 3
G1 Z0
G1 Z50 ; Lift Z axis
G1 X202 Y36 ; Move to Position 4
G1 Z0

G28; Home all axis
M84 ; disable motors



