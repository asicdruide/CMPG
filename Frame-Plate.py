import ezdxf
import math
from cfg    import *
from common import *

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Block_connect (p_variant , cx , cy):   # center of ballscrew
  hole  =   6.2

  if (p_variant == 'left'):
    mx = 1
  else:
    mx = -1


  for x,y in [(-28.6 , -32.5)
             ,( 40.5 , -32.5)
             ,( 40.5 ,   7  )
             ,(-28.6 ,  32.5)
             ]:
    msp.add_circle(((cx + x) * mx , cy + y) , hole/2)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Frame_Plate(p_name , p_variant):
  file_name = 'Frame-Plate-%s-%s.dxf' % (p_name , p_variant)


  if (p_variant == 'left'):
    # normal direction
    mx      = 1
  elif (p_variant == 'right'):
    # mirrored in x-direction
    mx      = -1
  else:
    print("ERROR: don't know how to draw Frame_Plate(%s,%s" % (p_name , p_variant))
    exit(1)

  cr    = 3                     # corner radius
  dbr   = 1.5                   # dog-bone radius => 3mm tool diameter
  cb90  = 0.4142135 *mx         # corner bulge = tan(22.5°) for 90° corners
  dbo90 = math.sqrt(2) * dbr    # dog-bone offset for 90° inner corners
  dbb   = -mx                   # dogbone bulge


  # if you intend an increased portal-side thickness (e.g. 20mm) you have to stretch the front/back plates and shift some holes.
  if (cfg['Portal']['side']['thickness'] <= 15):
    # default design, spacers will pad to 15mm...
    shift_x = 0
  else:
    # custom design...
    shift_x = cfg['side']['plate']['thickness'] - 15


  if (p_name == 'front'
      or
      p_name == 'back'
      ):
    # x/y values under the assumption that the center of ballscrew/motor-axis is at (0,0)
    (x0,x1,x2) = [ -36.1  ,  88+shift_x , 163.9+shift_x]
    (y0,y1,y2) = [ -40    ,   0         ,  40          ]

    # draw outer shape...
    shape = msp.add_lwpolyline([( (x0+cr   )*mx , y0       , 0   )
                               ,( (x2-cr   )*mx , y0       , cb90)
                               ,( (x2      )*mx , y0+cr    , 0   )
                               ,( (x2      )*mx , y1-cr    , cb90)
                               ,( (x2-cr   )*mx , y1       , 0   )
                               ,( (x1+cr   )*mx , y1       ,-cb90) # inner corner
                               ,( (x1      )*mx , y1+cr    , 0   )
                               ,( (x1      )*mx , y2-cr    , cb90)
                               ,( (x1-cr   )*mx , y2       , 0   )
                               ,( (x0+cr   )*mx , y2       , cb90)
                               ,( (x0      )*mx , y2-cr    , 0   )
                               ,( (x0      )*mx , y0+cr    , cb90)
                               ]
                              , format='xyb'
                              )
    shape.close(True)


    # add other elements...

    # The center of ballscrew is set at (0,0).
    # The distance between center of ballscrew and center of Y-profile is:
    #  20mm from center of ballscrew to mounting edge of nutholder
    #  15mm portal-side-thickness (either 10mm + 5mm spacer or native 15mm without spacer)
    #  13mm MGN12 height (rail+block)
    #  20mm half width of Y-profile
    #                = 68mm
    Face40x80(msp   , ( 68   +shift_x)*mx ,   0 , 0)
    Side40x40(msp   , (126.75+shift_x)*mx , -20 , 0)   # x is rounded, should be uncritical

    if (p_name == 'front'):
      # front
      BF12_face     (msp ,  0  ,   0 , 0)
    elif (p_name == 'back'):
      # back
      NEMA23       (msp  ,   0    ,   0 , 0)
      Block_connect(p_variant ,   0    ,   0)

    width  = (x2-x0)
    height = (y2-y0)

    text_x = (x2-x0) / 2 *mx
    text_y = y2 + 60

  elif (p_name == 'block'):
    # x/y values under the assumption that the center of ballscrew/motor-axis is at (0,0)
    (x0 , x1 , x2 , x3) = [-36.1 , -17.2 , 17.2 , 48]
    (y0 , y1 , y2 , y3) = [-40   , -17.2 , 14.5 , 40]

    # outer shape...
    shape = msp.add_lwpolyline([( (x0+cr   )*mx , y0       , 0   )
                               ,( (x3-cr   )*mx , y0       , cb90)
                               ,( (x3      )*mx , y0+cr    , 0   )
                               ,( (x3      )*mx , y2-cr    , cb90)
                               ,( (x3-cr   )*mx , y2       , 0   )
                               ,( (x2+cr   )*mx , y2       , cb90)
                               ,( (x2      )*mx , y2-cr    , 0   )
                               ,( (x2      )*mx , y1+dbo90 , dbb )
                               ,( (x2-dbo90)*mx , y1       , 0   )
                               ,( (x1+dbo90)*mx , y1       , dbb )
                               ,( (x1      )*mx , y1+dbo90 , 0   )
                               ,( (x1      )*mx , y3-cr    , cb90)
                               ,( (x1-cr   )*mx , y3       , 0   )
                               ,( (x0+cr   )*mx , y3       , cb90)
                               ,( (x0      )*mx , y3-cr    , 0   )
                               ,( (x0      )*mx , y0+cr    , cb90)
                               ]
                              , format='xyb'
                              )
    shape.close(True)

    # add other elements...
    Block_connect(p_variant ,   0    ,   0)
    BK12_face    (msp ,  0    ,   0  , 0)

    width  = (x3-x0)
    height = (y3-y0)

    text_x = (x3-x0) / 2 *mx
    text_y = y3 + 60

  else:
    print("ERROR: don't know how to draw Frame_Plate(%s,%s)" % (p_name , p_variant))
    exit(1)


  # add identifying text
  txt = (                 "%s" % file_name
        ,    "width=%5.2f[mm]" % width
        ,   "height=%5.2f[mm]" % height
        ,"thickness=%5.2f[mm]" % (cfg['Frame'][p_name]['thickness'])
        , "material=%s"        % (cfg['Frame'][p_name]['material'])
        ,   "amount=%d"        % (cfg['Frame'][p_name]['amount'])
        )

  for i in range(0,len(txt)):
    msp.add_text(txt[i]
                ,dxfattribs={'style' : 'LiberationSerif'
                            ,'height': 5
                            ,'layer' : 'annotation'
                            }
               ).set_pos((text_x , text_y - 10*i) , align='MIDDLE_CENTER')

  return  "%dx_%dmm_%s" % (cfg['Frame'][p_name]['amount']
                          ,cfg['Frame'][p_name]['thickness']
                          ,file_name
                          )

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# loop thru all plates to draw...
for p_name in      cfg['Frame'].keys():
  for p_variant in cfg['Frame'][p_name]['variant']:
    if (           cfg['Frame'][p_name]['thickness'] > 0):
      # Create a new DXF R2010 drawing, official DXF version name: "AC1024"
      doc = ezdxf.new('R2010' , setup=True)

      doc.layers.add(name="annotation"     , color=2)
      doc.layers.add(name="outline"        , color=2)

      # Add new entities to the modelspace:
      msp = doc.modelspace()

      file_name = 'Frame/' + Frame_Plate(p_name , p_variant)

      doc.saveas(file_name)

      print("INFO: file '%s' written" % file_name)
