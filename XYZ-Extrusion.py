from cfg      import *
from datetime import datetime


file_name = 'XYZ-Extrustion.txt'

OUT = open(file_name , 'w')


gantryXextrusion  = cfg['Ballscrew']['X']['length']
gantryXextrusion += 5           # at floating end
gantryXextrusion += 11          # at fixed end


frameXextrusion   =  gantryXextrusion
frameXextrusion  -= 13       # left  side MGN12 rail+block
frameXextrusion  -= 40       # left  side Y-extrusion
frameXextrusion  -= 40       # right side Y-extrusion
frameXextrusion  -= 13       # right side MGN12 rail+block



frameYextrusion   = cfg['Ballscrew']['Y']['length']
frameYextrusion  += 21      # at fixed end
frameYextrusion  -= 25      # at floating end
# baseline design is longer by 4mm but i'n sure this is correct!
# please have a look at XYZ-Extrusion.dxf



gantryZextrusion  = cfg['Ballscrew']['Z']['length']
gantryZextrusion += 5           # at floating end
gantryZextrusion += 15          # at fixed end


print("Extrusions:"                                                                      , file = OUT)
print(" * frame-X-extrusion  (2 x 40x40) %5dmm" % (frameXextrusion )                     , file = OUT)
print(" * frame-Y-extrusion  (2 x 40x80) %5dmm" % (frameYextrusion )                     , file = OUT)
print(" * gantry-X-extrusion (2 x 40x60) %5dmm" % (gantryXextrusion)                     , file = OUT)
print(" * gantry-Z-extrusion (2 x 20x20) %5dmm" % (gantryZextrusion)                     , file = OUT)

print(""                                                                                 , file = OUT)

print("Work-Area:"                                                                       , file = OUT)
print(" * X                              %5dmm" % (cfg['Ballscrew']['X']['length'] - 175), file = OUT)  # from CindMill docu
print(" * Y                              %5dmm" % (cfg['Ballscrew']['Y']['length'] - 250), file = OUT)  # from CindMill docu
print(" * Z                              %5dmm" % (cfg['Ballscrew']['Z']['length'] - 130), file = OUT)  # from CindMill docu

print(""                                                                                 , file = OUT)


outerXframe  = gantryXextrusion
outerXframe += 15                                       # sum of actual right-side width + spacers
outerXframe += 15                                       # sum of actual left-side width + spacers



outerYframe  = frameYextrusion
outerYframe += 2*cfg['Portal']['side']['thickness']    # actual side width
outerYframe += 20                                      # BF12 is mounted outside



print("outer frame:"                                                                     , file = OUT)
print(" * X                              %5dmm (+Xstepper)" % (outerXframe)              , file = OUT)
print(" * Y                              %5dmm (+Ystepper)" % (outerYframe)              , file = OUT)

print("generated on %s" % ((datetime.now().strftime("%a %Y-%b-%d %H:%M:%S")))            , file = OUT)

OUT.close()

print("INFO: file '%s' written" % file_name)

