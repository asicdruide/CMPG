import ezdxf
import math
from ezdxf    import units
from cfg      import *
from common   import *
from datetime import datetime

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Block_connect (p_variant , cx , cy):   # center of ballscrew
  hole = 6.2

  if (p_variant == 'right'):
    mx = -1
  else:
    mx = 1

  for x,y in [( 9.5  * mx,  35)
             ,( 9.5  * mx, -35)
             ,(-35.5 * mx,  35)
             ,(-35.5 * mx, -35)
             ]:
    msp.add_circle((x + cx*mx , cy + y) , hole/2)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def AddOn (p_variant):
  hole = 6.8
  # purpose is to mount the foot of a measuring stand that holds a dial indicator the measure and adjust alignment

  if (p_variant == 'left'):
    mx = 1
  else:
    mx = -1

  for (x,y) in [[37 + 1*70.59 , 94.7514]
              #,[37 + 2*70.59 , 94.7514]
              #,[37           , 94.7514]
               ]:
    msp.add_circle((x * mx , y) , hole/2)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def outer_corner (cr , start_angle , stop_angle):
  # example:
  # * cr          =   5
  # * start_angle =  90°     (vertical, border between first and second quadrant))
  # * stop_angle  =  125.76° (about half into 2nd quadrant)
  #
  # => inner angle = 360° - start_angle - stop_angle = 144.24°
  # => theta       = 180° - inner_angle = 35.76°
  inner_angle = 360 - start_angle - stop_angle
  theta       = 180 - inner_angle

  cb  = math.tan((theta / 4) * math.pi / 180)          # corner bulge = tan(theta/4)
  cbo = math.tan((theta / 2) * math.pi / 180)*cr       # corner offset (distance between sharp corner and tangent point)

  #print("DEBUG:          cr=%5.2f     start_angle=%5.2f    stop_angle=%5.2f" % (cr , start_angle , stop_angle))
  #print("DEBUG: inner_angle=%5.2f           theta=%5.2f                     cb=%12.6f    cbo=%12.6f" % (inner_angle , theta , cb , cbo))


  # offset of starting line:
  cbo_xs = math.cos(start_angle*math.pi/180) * cbo
  cbo_ys = math.sin(start_angle*math.pi/180) * cbo

  # offset of end point
  cbo_xe = math.cos((stop_angle)*math.pi/180) * cbo
  cbo_ye = math.sin((stop_angle)*math.pi/180) * cbo

  #print("DEBUG: cbo_xs=%10.6f     cbo_ys=%16.6f" % (cbo_xs , cbo_ys))
  #print("DEBUG: cbo_xe=%10.6f     cbo_ye=%16.6f" % (cbo_xe , cbo_ye))

  return (cb , cbo_xs , cbo_ys , cbo_xe , cbo_ye)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Portal_plate(p_name , p_variant):
  if (p_variant == ""):
    file_name = 'Portal-%s.dxf'    % (p_name)

  else:
    file_name = 'Portal-%s-%s.dxf' % (p_name , p_variant)


  if (p_variant == 'left' or p_variant == ""):
    # normal direction
    mx      = 1
  elif (p_variant == 'right'):
    # mirrored in x-direction
    mx      = -1
  else:
    print("ERROR: don't know how to draw Portal_plate(%s,%s)" % (p_name , p_variant))
    exit(1)

  cr    = 5                     # corner radius
  dbr   = 2.0                   # dog-bone radius => 4mm tool diameter
  cb90  = 0.4142135 *mx         # corner bulge = tan(22.5°) for 90° corners
  dbo90 = math.sqrt(2) * dbr    # dog-bone offset for 90° inner corners
  dbb   = -mx                   # dogbone bulge


  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  if (p_name == 'back'):
    # fixed parameters
    margin = 2

    width           = 666 + (cfg['Ballscrew']['X']['length'] - 650) - margin  # 650 from baseline design
    height          = 160     # height of plate
    border_distance =   7.5
    hole_diameter   =   5.2
    y_spacing       =  20
    x_spacing       = (width - 2*border_distance) / 4  # distribute 5 holes over the distance

    x = [0,0,0,0,0,0,0]
    y = [0,0,0,0,0,0]

    x[0] = -width  / 2                  # leftmost X
    x[1] = x[0] + border_distance
    x[2] = x[1] + x_spacing
    x[3] = x[2] + x_spacing
    x[4] = x[3] + x_spacing
    x[5] = x[4] + x_spacing
    x[6] = width / 2                    # rightmost X

    y[0] = 0                            # bottom Y
    y[1] = y[0] + border_distance
    y[2] = y[1] + y_spacing

    y[5] = height                       # top Y
    y[4] = y[5] - border_distance
    y[3] = y[4] - y_spacing


    # outer shape...
    shape = msp.add_lwpolyline([( x[0] , y[0])
                               ,( x[6] , y[0])
                               ,( x[6] , y[5])
                               ,( x[0] , y[5])
                               ]
                              , format='xy'
                              )
    shape.close(True)


    # array of holes...
    for xi in range(1,6):
      for yi in range(1,5):
        msp.add_circle((x[xi] , y[yi]) , hole_diameter/2)


    text_x = 0
    text_y = height
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  elif (p_name == 'side'):
    if (p_variant == 'left'):
      mx = 1
    else:
      mx = -1

    (x0 , x1 , x2 , x3 , x4 , x5) = (0 ,  5  ,    70   , 87.59  , 210.18    , 215.18)
    (y5 , y4 , y3 , y2 , y1 , y0) = ( 276.059
                                    ,  74.4976
                                    ,  54.82
                                    ,  42.5
                                    ,  31.25
                                    ,   0
                                    )

    cr=2.5

    # we have 2 non-right angles
    # corner 16 -- 16 : 17 -- 18   start_angle = 90°     , stop_angle = 125.76°
    # corner 17 -- 18 : 19 -- 20   start_angle = 125.76° , stop_angle = 0°
    (p16cb , p16x , p16y , p17x , p17y) = outer_corner(5   , 90     , 125.76)
    (p18cb , p18x , p18y , p19x , p19y) = outer_corner(5   , 125.76 , 0     )


    # outer shape...
    shape = msp.add_lwpolyline([( (x0+cr      )*mx , y3         , 0       )   #  1
                               ,( (x1-cr      )*mx , y3         ,-cb90    )   #  2
                               ,( (x1         )*mx , y3-cr      , 0       )   #  3
                               ,( (x1         )*mx , y2+cr      , cb90    )   #  4
                               ,( (x1+cr      )*mx , y2         , 0       )   #  5
                               ,( (x3-5       )*mx , y2         ,-cb90    )   #  6
                               ,( (x3         )*mx , y2-5       , 0       )   #  7
                               ,( (x3         )*mx , y0+1       , cb90    )   #  8
                               ,( (x3+1       )*mx , y0         , 0       )   #  9
                               ,( (x4-cr      )*mx , y0         , cb90    )   # 10
                               ,( (x4         )*mx , y0+cr      , 0       )   # 11
                               ,( (x4         )*mx , y1-cr      ,-cb90    )   # 12
                               ,( (x4+cr      )*mx , y1         , 0       )   # 13
                               ,( (x5-cr      )*mx , y1         , cb90    )   # 14
                               ,( (x5         )*mx , y1+cr      , 0       )   # 15
                               ,( (x5+p16x    )*mx , y4-p16y    , p16cb*mx)   # 16
                               ,( (x5+p17x    )*mx , y4+p17y    , 0       )   # 17
                               ,( (x2+p18x    )*mx , y5+p18y    ,-p18cb*mx)   # 18
                               ,( (x2+p19x    )*mx , y5+p19y    , 0       )   # 19
                               ,( (x0+5       )*mx , y5         , cb90    )   # 20
                               ,( (x0         )*mx , y5-5       , 0       )   # 21
                               ,( (x0         )*mx , y3+cr      , cb90    )   # 22
                               ]
                              , format='xyb'
                              )
    shape.close(True)

    # add other elements...
    MGN12H         (msp ,  27   *mx ,  56      , 0   , 0)
    MGN12H         (msp , 188.18*mx ,  56      , 0   , 0)
    SFU1605_holder (msp , 107.59*mx ,  26      , 0)

    Face40x60      (msp ,  35   *mx , 126.059  , 0 , cfg['Portal']['side']['thickness']-10)
    Face40x60      (msp ,  35   *mx , 251.059  , 0 , cfg['Portal']['side']['thickness']-10)

    if (p_variant == 'left'):
      BF12_face    (msp ,  48       , 188.5590 , -90)
    else:
      NEMA23       (msp , -48       , 188.559  ,   0)
      Block_connect(p_variant ,  48  , 188.559)

    AddOn(p_variant)

    width  = x5 - x0
    height = y5 - y0

    if (p_variant == 'left'):
      text_x = x3
    else:
      text_x = -x3

    text_y = y5
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  elif (p_name == 'motor_spacer'):
    # x/y values under the assumption that the center of ballscrew/motor-axis is at (0,0)
    (x0 , x1) = [-28.5 , 28.5]
    (y0 , y1) = [-28.5 , 28.5]

    # outer shape...
    shape = msp.add_lwpolyline([( (x0+cr   )*mx , y0       , 0   )   #  1
                               ,( (x1-cr   )*mx , y0       , cb90)   #  2
                               ,( (x1      )*mx , y0+cr    , 0   )   #  3
                               ,( (x1      )*mx , y1-cr    , cb90)   #  4
                               ,( (x1-cr   )*mx , y1       , 0   )   #  5
                               ,( (x0+cr   )*mx , y1       , cb90)   #  6
                               ,( (x0      )*mx , y1-cr    , 0   )   #  7
                               ,( (x0      )*mx , y0+cr    , cb90)   #  8
                               ]
                              , format='xyb'
                              )
    shape.close(True)

    # add other elements...
    NEMA23(msp  ,   0    ,   0  , 0)

    width  = (x1-x0)
    height = (y1-y0)

    text_x = 0
    text_y = y1

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  elif (p_name == 'nut_spacer'
        or
        p_name == 'side_plate_spacer'):
    hole = 5.2
    cr   = 1



    # x/y values
    (x0 , x1) = [-20 , 20]
    (y0 , y1) = [-26 , 26]

    # outer shape...
    shape = msp.add_lwpolyline([( (x0+cr   )*mx , y0       , 0   )   #  1
                               ,( (x1-cr   )*mx , y0       , cb90)   #  2
                               ,( (x1      )*mx , y0+cr    , 0   )   #  3
                               ,( (x1      )*mx , y1-cr    , cb90)   #  4
                               ,( (x1-cr   )*mx , y1       , 0   )   #  5
                               ,( (x0+cr   )*mx , y1       , cb90)   #  6
                               ,( (x0      )*mx , y1-cr    , 0   )   #  7
                               ,( (x0      )*mx , y0+cr    , cb90)   #  8
                               ]
                              , format='xyb'
                              )
    shape.close(True)

    SFU1605_holder(msp , 0 , 0 , 0)

    width  = (x1-x0)
    height = (y1-y0)

    text_x = 0
    text_y = y1

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  elif (p_name == 'block'):
    # x/y values under the assumption that the center of ballscrew/motor-axis is at (0,0)
    (x0 , x1 , x2     ) = [-17   ,  17.2 , 43  ]
    (y0 , y1 , y2 , y3) = [-42.5 , -17.2 , 17.2 , 42.5]

    mx=-1 # mirror to get the facets on the side towards inside

    # outer shape...
    shape = msp.add_lwpolyline([( (x0+cr   )*mx , y0       , 0      )   #  1
                               ,( (x2-cr   )*mx , y0       , cb90*mx)   #  2
                               ,( (x2      )*mx , y0+cr    , 0      )   #  3
                               ,( (x2      )*mx , y3-cr    , cb90*mx)   #  4
                               ,( (x2-cr   )*mx , y3       , 0      )   #  5
                               ,( (x0+cr   )*mx , y3       , cb90*mx)   #  6
                               ,( (x0      )*mx , y3-cr    , 0      )   #  7
                               ,( (x0      )*mx , y2+cr    , cb90*mx)   #  8
                               ,( (x0+cr   )*mx , y2       , 0      )   #  9
                               ,( (x1-dbo90)*mx , y2       , dbb *mx)   # 10
                               ,( (x1      )*mx , y2-dbo90 , 0      )   # 11
                               ,( (x1      )*mx , y1+dbo90 , dbb *mx)   # 12
                               ,( (x1-dbo90)*mx , y1       , 0      )   # 13
                               ,( (x0+cr   )*mx , y1       , cb90*mx)   # 14
                               ,( (x0      )*mx , y1-cr    , 0      )   # 15
                               ,( (x0      )*mx , y0+cr    , cb90*mx)   # 16
                               ]
                              , format='xyb'
                              )
    shape.close(True)

    # add other elements...
    Block_connect(p_variant ,  0    ,   0)
    BK12_face    (msp       ,  0    ,   0  , 270)

    width  = (x2-x0)
    height = (y3-y0)

    text_x = 0
    text_y = y3

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  else:
    print("ERROR: don't know how to draw Portal_Plate(%s,%s)" % (p_name , p_variant))
    exit(1)
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -




  # add identifying text
  txt = (               "%s" % file_name
        ,    "width=%5.2fmm" % width
        ,   "height=%5.2fmm" % height
        ,"thickness=%5.2fmm" % (cfg['Portal'][p_name]['thickness'])
        , "material=%s"      % (cfg['Portal'][p_name]['material'])
        ,   "amount=%d"      % (cfg['Portal'][p_name]['amount'])
        ,   "%s"             % (datetime.now().strftime("%a %Y-%b-%d %H:%M:%S"))
        )

  for i in range(0,len(txt)):
    msp.add_text(txt[i]
                ,dxfattribs={'style' : 'LiberationSerif'
                            ,'height': 5
                            ,'layer' : 'annotation'
                            }
               ).set_pos((text_x , text_y + 70 - 10*i) , align='MIDDLE_CENTER')

  return  "%dx_%dmm_%s" % (cfg['Portal'][p_name]['amount']
                          ,cfg['Portal'][p_name]['thickness']
                          ,file_name
                          )

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# loop thru all plates to draw...
for p_name in      cfg['Portal'].keys():
  for p_variant in cfg['Portal'][p_name]['variant']:
    if (           cfg['Portal'][p_name]['thickness'] > 0):
      # Create a new DXF R2010 drawing, official DXF version name: "AC1024"
      doc = ezdxf.new('R2010' , setup=True)

      my_annotations = doc.layers.add(name="annotation"      , color=2)
      my_outline     = doc.layers.add(name="outline"         , color=2)
      doc.units      = units.MM


      # Add new entities to the modelspace:
      msp = doc.modelspace()

      file_name = 'Portal/' + Portal_plate(p_name , p_variant)

      doc.saveas(file_name)

      print("INFO: file '%s' written" % file_name)

      #my_annotations.off()
      #my_outline    .off()
      #
      #file_name = file_name.replace(".dxf", "_plain.dxf")
      #
      #doc.saveas(file_name)
      #
      #print("INFO: file '%s' written" % file_name)



