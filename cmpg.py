import ezdxf
from ezdxf         import units
from cfg           import *
from Frame_Plate   import *
from ZAxis_Plate   import *
from Portal_Plate  import *
from XYZ_extrusion import *
from datetime import datetime

ctx = {'bom' : {} # collect screws/washers/nuts/...
      ,'doc' : 0
      ,'msp' : 0
      ,'lay' : {} # collect optional layers
      }


def Plate(ctx , plate_group , plate_name , plate_variant):
  if (plate_group == 'Frame'):
    return Frame_plate(ctx , plate_group , plate_name , plate_variant)
  elif (plate_group == 'ZAxis'):
    return ZAxis_Plate(ctx , plate_group , plate_name , plate_variant)
  elif (plate_group == 'Portal'):
    return Portal_Plate(ctx , plate_group , plate_name , plate_variant)
  else:
    print("ERROR: unknown plate group (%s)" % (plate_group))
    exit(1)




# for mounting 1605 spindle nut to holder...
screw = Screw('M5' , 10     # spindle nut flange thickness
                   + 10     # thread into nut holder
             )
Add2BOM(ctx , 3*6 , 'DIN912' , screw , '1605 nut to nut holder')    # screw
Add2BOM(ctx , 3*6 , 'DIN125' , 'M5'  , '1605 nut to nut holder')    # washer

# for mounting 1204 spindle nut to holder...
screw = Screw('M4' , 8.5    # spindle nut flange thickness
                   + 8      # thread into nut holder
             )
Add2BOM(ctx , 6 , 'DIN912' , screw , '1204 nut to nut holder')    # screw
Add2BOM(ctx , 6 , 'DIN125' , 'M4'  , '1204 nut to nut holder')    # washer



# brackets to threnghten the frame
doc = 'brackets at inner frame corners'
Add2BOM(ctx ,   8 ,'brackets'   ,  'M5'    , doc)    # sliding nut

Add2BOM(ctx , 2*8 ,'DIN912'     ,  'M5x8'  , doc)    # screw
Add2BOM(ctx , 2*8 ,'DIN125'     ,  'M5'    , doc)    # washer
Add2BOM(ctx , 2*8 ,'SlidingNut' ,  'M5'    , doc)    # sliding nut



# lmit switches
doc = 'mounting Z-limit switches'
Add2BOM(ctx , 2 ,'DIN912'     ,  'M3x16' , doc)    # screw ~11mm in holder + 5mm in sliding nut
Add2BOM(ctx , 2 ,'DIN125'     ,  'M3'    , doc)    # washer
Add2BOM(ctx , 2 ,'SlidingNut' ,  'M3'    , doc)    # sliding nut

doc = 'mounting XY-limit switches'
Add2BOM(ctx , 4 ,'DIN912'     ,  'M3x10' , doc)    # screw ~5mm in holder + 5mm in sliding nut
Add2BOM(ctx , 4 ,'DIN125'     ,  'M3'    , doc)    # washer
Add2BOM(ctx , 4 ,'SlidingNut' ,  'M3'    , doc)    # sliding nut











# loop thru all plates to draw...
for plate_group  in cfg['Plates'].keys():
  for plate_name in cfg['Plates'][plate_group].keys():
    for plate_variant in cfg['Plates'][plate_group][plate_name]['variant']:
      if (           cfg['Plates'][plate_group][plate_name]['thickness'] > 0):
        # Create a new DXF R2010 drawing, official DXF version name: "AC1024"
        ctx['doc'] = ezdxf.new('R2010' , setup=True)

        ctx['doc'].units = units.MM
        my_annotations   = ctx['doc'].layers.add(name="annotation"      , color=7)
        my_outline       = ctx['doc'].layers.add(name="outline"         , color=2)

        ctx['lay'] = dict()

        # Add new entities to the modelspace:
        ctx['msp'] = ctx['doc'].modelspace()

        res = Plate(ctx , plate_group , plate_name , plate_variant)

        file_name = "%dx_%dmm_%s-%s%s.dxf" % (cfg['Plates'][plate_group][plate_name]['amount']
                                             ,cfg['Plates'][plate_group][plate_name]['thickness']
                                             ,plate_group
                                             ,plate_name
                                             ,"" if (plate_variant=='') else "-%s" % plate_variant
                                             )



        # add identifying text
        txt = [               "%s" % file_name
              ,    "width=%5.2fmm" % res['plateWH'][0]
              ,   "height=%5.2fmm" % res['plateWH'][1]
              ,"thickness=%5.2fmm" % (cfg['Plates'][plate_group][plate_name]['thickness'])
              , "material=%s"      % (cfg['Plates'][plate_group][plate_name]['material'])
              ,   "amount=%d"      % (cfg['Plates'][plate_group][plate_name]['amount'])
              ,   "%s"             % (datetime.now().strftime("%a %Y-%b-%d %H:%M:%S"))
              ]

        if (plate_group=='ZAxis' and plate_name == 'back'):
          txt.append("variant for %dmm thick top and %dmm thick bottom"    % (cfg['Plates'][plate_group]['top'   ]['thickness'],cfg['Plates'][plate_group]['bottom']['thickness']))


        for i in range(0,len(txt)):
          ctx['msp'].add_text(txt[i]
                      ,dxfattribs={'style' : 'LiberationSans'
                                  ,'height': 5
                                  ,'layer' : 'annotation'
                                  }
                     ).set_pos((res['textXY'][0] , res['textXY'][1] + len(txt)*10 - 10*i) , align='MIDDLE_CENTER')

        i = 0

        if (len(ctx['lay'].keys()) <= 7):
          text_top = 70
        else:
          text_top = len(ctx['lay'].keys()) * 10

        for ln in ctx['lay'].keys():
          # add comment
          ctx['msp'].add_text(ctx['lay'][ln]
                      ,dxfattribs={'style' : 'LiberationSans'
                                  ,'height': 5
                                  ,'layer' : ln
                                  }
                     ).set_pos((res['textXY'][0] + 80 , res['textXY'][1] + text_top - 10*i) , align='MIDDLE_LEFT')
          i += 1



        file_name = "generated/%s" % (file_name)

        ctx['doc'].saveas(file_name)

        print("INFO: file '%s' written" % file_name)




# calculate other data and write file...
XYZ_extrusion(ctx)



# dump bom to file...
file_name = 'generated/CindyMillBom.txt'

OUT = open(file_name , 'w')

#print("DEBUG: bom=%s" % (ctx['bom']))

for what      in sorted(ctx['bom']      .keys()):
  for variant in sorted(ctx['bom'][what].keys()):
    sum = 0

    for (cnt,doc) in ctx['bom'][what][variant]:
      sum += cnt

    print("%-12s %-5s.........................%3d needed....stock(    ).......to be sourced(    )" % (what, variant, sum)  , file = OUT)

    for (cnt,doc) in ctx['bom'][what][variant]:
      print("  %3d (%s)" % (cnt,doc)                                           , file = OUT)

    print(" "                                                                  , file = OUT)

print("generated on %s" % ((datetime.now().strftime("%a %Y-%b-%d %H:%M:%S")))  , file = OUT)

OUT.close()

print("INFO: file '%s' written" % file_name)

