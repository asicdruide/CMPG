import ezdxf
import math
from cfg import *

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def BK12 (lr_id , cx , cy):   # center of ballscrew
  hole1  =   5.2

  if (lr_id == 'left' or lr_id == ""):
    mx = 1
  else:
    mx = -1

  msp.add_circle(((cx     ) * mx , cy  - 23) , hole1/2)
  msp.add_circle(((cx     ) * mx , cy  + 23) , hole1/2)
  msp.add_circle(((cx + 18) * mx , cy  - 23) , hole1/2)
  msp.add_circle(((cx + 18) * mx , cy  + 23) , hole1/2)

  # add outline
  msp.add_lwpolyline([( (cx-25     )*-1*mx , cy-30)
                     ,( (cx-25     )*-1*mx , cy+30)
                     ,( (cx-25+32.5)*-1*mx , cy+30)
                     ,( (cx-25+32.5)*-1*mx , cy+17)
                     ,( (cx-25+43  )*-1*mx , cy+17)
                     ,( (cx-25+43  )*-1*mx , cy-17)
                     ,( (cx-25+32.5)*-1*mx , cy-17)
                     ,( (cx-25+32.5)*-1*mx , cy-30)
                     ,( (cx-25     )*-1*mx , cy-30)
                     ]
                    , dxfattribs={'layer': 'outline'}
                    )

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Block_connect (lr_id , cx , cy):   # center of ballscrew
  hole = 6.2

  if (lr_id == 'left' or lr_id == ""):
    mx = 1
  else:
    mx = -1

  for x,y in [(-9.5  ,  35)
             ,(-9.5  , -35)
             ,( 35.5 ,  35)
             ,( 35.5 , -35)
             ]:
    msp.add_circle((cx*mx + x , cy + y) , hole/2)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def NEMA23 (lr_id , cx , cy):   # center of axis
  hole1  =   5.2
  hole2  =  38.5
  width  = 47.14

  if (lr_id == 'left'):
    mx = 1
  else:
    mx = -1

  msp.add_circle(((cx     ) * mx , cy      ) , hole2/2)

  for x,y in [(- width/2 , - width/2)
             ,(- width/2 , + width/2)
             ,(+ width/2 , - width/2)
             ,(+ width/2 , + width/2)
             ]:
    msp.add_circle(((cx + x)*mx , cy + y) , hole1/2)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def MGN12H(lr_id , cx , cy):
  if (lr_id == 'left' or lr_id == ""):
    mx = 1
  else:
    mx = -1

  width  =  20
  height =  20
  hole   =   3.2

  for (x,y) in [[cx - width / 2 , cy - height / 2]
               ,[cx - width / 2 , cy + height / 2]
               ,[cx + width / 2 , cy - height / 2]
               ,[cx + width / 2 , cy + height / 2]
               ]:
    msp.add_circle((x*mx , y) , hole/2)

  width  = 45.4
  height = 27

  # add outline
  msp.add_lwpolyline([( (cx-(width/2))*mx , cy-(height/2))
                     ,( (cx+(width/2))*mx , cy-(height/2))
                     ,( (cx+(width/2))*mx , cy+(height/2))
                     ,( (cx-(width/2))*mx , cy+(height/2))
                     ,( (cx-(width/2))*mx , cy-(height/2))
                     ]
                    , dxfattribs={'layer': 'outline'}
                    )

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def SFU1605_holder(lr_id , cx , cy , orientation):
  if (orientation == 'vertical'):
    width  = 40
    height = 24
    ow     = 52
    oh     = 40
  elif (orientation == 'horizontal'):
    width  =  24
    height =  40
    ow     =  40
    oh     =  52
  else:
    print("unknown orientation '%s' at SFU1605_holder" % orientation)
    exit(1)

  if (lr_id == 'left' or lr_id == ""):
    mx = 1
  else:
    mx = -1

  hole = 5.2

  for (x,y) in [[cx - (width / 2) , cy - (height / 2)]
               ,[cx - (width / 2) , cy + (height / 2)]
               ,[cx + (width / 2) , cy - (height / 2)]
               ,[cx + (width / 2) , cy + (height / 2)]
               ]:
    msp.add_circle((x*mx , y) , hole/2)


  # add outline
  msp.add_lwpolyline([( (cx-(ow/2))*mx , cy-(oh/2))
                     ,( (cx+(ow/2))*mx , cy-(oh/2))
                     ,( (cx+(ow/2))*mx , cy+(oh/2))
                     ,( (cx-(ow/2))*mx , cy+(oh/2))
                     ,( (cx-(ow/2))*mx , cy-(oh/2))
                     ]
                    , dxfattribs={'layer': 'outline'}
                    )

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def BF12 (lr_id , cx , cy):   # center of ballscrew, floating support
  hole1  =   5.2
  hole2  =  26

  if (lr_id == 'left'):
    mx = 1
  else:
    mx = -1

  msp.add_circle(((cx     ) * mx , cy      ) , hole2/2)

  msp.add_circle(((cx     ) * mx , cy - 23 ) , hole1/2)
  msp.add_circle(((cx     ) * mx , cy + 23 ) , hole1/2)
  msp.add_circle(((cx - 18) * mx , cy - 23 ) , hole1/2)
  msp.add_circle(((cx - 18) * mx , cy + 23 ) , hole1/2)

  # add outline
  msp.add_lwpolyline([( (cx-25     )*mx , cy-30)
                     ,( (cx-25     )*mx , cy+30)
                     ,( (cx-25+32.5)*mx , cy+30)
                     ,( (cx-25+32.5)*mx , cy+17)
                     ,( (cx-25+43  )*mx , cy+17)
                     ,( (cx-25+43  )*mx , cy-17)
                     ,( (cx-25+32.5)*mx , cy-17)
                     ,( (cx-25+32.5)*mx , cy-30)
                     ,( (cx-25     )*mx , cy-30)
                     ]
                    , dxfattribs={'layer': 'outline'}
                    )

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def AddOn (lr_id):
  hole = 6.8

  if (lr_id == 'left'):
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

def Face40x60 (lr_id , cx , cy , counterbore_depth):   # center of profile
  hole = 5.2

  if (lr_id == 'left'):
    mx = 1
  else:
    mx = -1

  holes =  [[cx - 20 , cy + 10]
           ,[cx - 20 , cy - 10]
           ,[cx      , cy + 10]
           ,[cx      , cy - 10]
           ,[cx + 20 , cy + 10]
           ,[cx + 20 , cy - 10]
           ]


  for (x,y) in holes:
    msp.add_circle((x * mx , y) , hole/2)

  # add outline
  msp.add_lwpolyline([( (cx-30)*mx , cy-20     )
                     ,( (cx+30)*mx , cy-20     )
                     ,( (cx+30)*mx , cy+20     )
                     ,( (cx-30)*mx , cy+20     )
                     ,( (cx-30)*mx , cy-20     )
                     ]
                    , dxfattribs={'layer': 'outline'}
                    )


  if (counterbore_depth > 0):
    hole2  =   9   # counter bore

    for (x,y) in holes:
      msp.add_circle((x * mx , y) , hole2/2 , dxfattribs={'layer' : 'annotation'})

    msp.add_text("counterbored %d[mm] deep" % counterbore_depth
                ,dxfattribs={'style' : 'LiberationSerif'
                            ,'height': 5
                            ,'layer' : 'annotation'
                            }
               ).set_pos((cx , cy) , align='MIDDLE_CENTER')







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

def Portal_plate(p_id , lr_id):
  if (lr_id == ""):
    file_name = ('Portal-Plate-%s.dxf'    % (p_id))
  else:
    file_name = ('Portal-Plate-%s-%s.dxf' % (p_id , lr_id))

  if (lr_id == 'left' or lr_id == ""):
    # normal direction
    mx      = 1
  elif (lr_id == 'right'):
    # mirrored in x-direction
    mx      = -1
  else:
    print("ERROR: don't know how to draw Portal_plate(%s,%s)" % (p_id , lr_id))
    exit(1)

  cr    = 5                     # corner radius
  dbr   = 2.0                   # dog-bone radius => 4mm tool diameter
  cb90  = 0.4142135 *mx         # corner bulge = tan(22.5°) for 90° corners
  dbo90 = math.sqrt(2) * dbr    # dog-bone offset for 90° inner corners
  dbb   = -mx                   # dogbone bulge


  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  if (p_id == 'back'):
    # fixed parameters
    width           = 666 + (cfg['Ballscrew']['X']['length'] - 650)  # 650 from baseline design
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
  elif (p_id == 'side'):
    if (lr_id == 'left'):
      mx = 1
    else:
      mx = -1

    (x0 , x1 , x2 , x3 , x4 , x5) = (0 ,  5  ,    70   , 87.59  , 210.18    , 215.18)
    (y0 , y1 , y2 , y3 , y4 , y5) = (0 , 31.25 , 42.5  , 54.82  ,  74.4976  , 276.059)

    cr=2.5

    # we have 2 non-right angles
    # corner 16 -- 16 : 17 -- 18   start_angle = 90°     , stop_angle = 125.76°
    # corner 17 -- 18 : 19 -- 20   start_angle = 125.76° , stop_angle = 0°
    (p16cb , p16x , p16y , p17x , p17y) = outer_corner(2.5 , 90     , 125.76)
    (p18cb , p18x , p18y , p19x , p19y) = outer_corner(2.5 , 125.76 , 0     )


    # outer shape...
    shape = msp.add_lwpolyline([( (x0+cr      )*mx , y3         , 0       )   #  1
                               ,( (x1-cr      )*mx , y3         ,-cb90    )   #  2
                               ,( (x1         )*mx , y3-cr      , 0       )   #  3
                               ,( (x1         )*mx , y2+cr      , cb90    )   #  4
                               ,( (x1+cr      )*mx , y2         , 0       )   #  5
                               ,( (x3-cr      )*mx , y2         ,-cb90    )   #  6
                               ,( (x3         )*mx , y2-cr      , 0       )   #  7
                               ,( (x3         )*mx , y0+cr      , cb90    )   #  8
                               ,( (x3+cr      )*mx , y0         , 0       )   #  9
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
                               ,( (x0+cr      )*mx , y5         , cb90    )   # 20
                               ,( (x0         )*mx , y5-cr      , 0       )   # 21
                               ,( (x0         )*mx , y3+cr      , cb90    )   # 22
                               ]
                              , format='xyb'
                              )
    shape.close(True)

    # add other elements...
    MGN12H(lr_id ,  27    , 56)
    MGN12H(lr_id , 188.18 , 56)

    SFU1605_holder(lr_id , 107.59 , 26 , 'horizontal')

    Face40x60(lr_id , 35 , 126.059 , cfg['Portal']['side']['thickness']-10)
    Face40x60(lr_id , 35 , 251.059 , cfg['Portal']['side']['thickness']-10)

    if (lr_id == 'left'):
      BF12(lr_id , 48  , 188.5590)
    else:
      NEMA23       (lr_id , 48 , 188.559)
      Block_connect(lr_id , 48 , 188.559)


    AddOn(lr_id)

    width  = x5 - x0
    height = y5 - y0

    if (lr_id == 'left'):
      text_x = x3
    else:
      text_x = -x3

    text_y = y5
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  elif (p_id == 'motor_spacer'):
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
    NEMA23(lr_id ,   0    ,   0)

    width  = (x1-x0)
    height = (y1-y0)

    text_x = 0
    text_y = y1

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  elif (p_id == 'nut_spacer'):
    hole = 5.2

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

    # add other elements...
    for x,y in [[-12 , -20]
               ,[ 12 , -20]
               ,[ 12 ,  20]
               ,[-12 ,  20]
               ]:
      msp.add_circle((x, y) , hole/2)

    width  = (x1-x0)
    height = (y1-y0)

    text_x = 0
    text_y = y1

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  elif (p_id == 'block'):
    # x/y values under the assumption that the center of ballscrew/motor-axis is at (0,0)
    (x0 , x1 , x2     ) = [-17   ,  17.2 , 43  ]
    (y0 , y1 , y2 , y3) = [-42.5 , -17.2 , 17.2 , 42.5]

    # outer shape...
    shape = msp.add_lwpolyline([( (x0+cr   )*mx , y0       , 0   )   #  1
                               ,( (x2-cr   )*mx , y0       , cb90)   #  2
                               ,( (x2      )*mx , y0+cr    , 0   )   #  3
                               ,( (x2      )*mx , y3-cr    , cb90)   #  4
                               ,( (x2-cr   )*mx , y3       , 0   )   #  5
                               ,( (x0+cr   )*mx , y3       , cb90)   #  6
                               ,( (x0      )*mx , y3-cr    , 0   )   #  7
                               ,( (x0      )*mx , y2+cr    , cb90)   #  8
                               ,( (x0+cr   )*mx , y2       , 0   )   #  9
                               ,( (x1-dbo90)*mx , y2       , dbb )   # 10
                               ,( (x1      )*mx , y2-dbo90 , 0   )   # 11
                               ,( (x1      )*mx , y1+dbo90 , dbb )   # 12
                               ,( (x1-dbo90)*mx , y1       , 0   )   # 13
                               ,( (x0+cr   )*mx , y1       , cb90)   # 14
                               ,( (x0      )*mx , y1-cr    , 0   )   # 15
                               ,( (x0      )*mx , y0+cr    , cb90)   # 16
                               ]
                              , format='xyb'
                              )
    shape.close(True)

    # add other elements...
    Block_connect(lr_id ,   0    ,   0)
    BK12         (lr_id ,   0    ,   0)

    width  = (x2-x0)
    height = (y3-y0)

    text_x = 0
    text_y = y3

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  else:
    print("ERROR: don't know how to draw Portal_Plate(%s,%s)" % (p_id , lr_id))
    exit(1)
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -




  # add identifying text
  txt = (                 "%s" % file_name
        ,    "width=%5.2f[mm]" % width
        ,   "height=%5.2f[mm]" % height
        ,"thickness=%5.2f[mm]" % (cfg['Portal'][p_id]['thickness'])
        , "material=%s"        % (cfg['Portal'][p_id]['material'])
        )

  for i in range(0,5):
    msp.add_text(txt[i]
                ,dxfattribs={'style' : 'LiberationSerif'
                            ,'height': 5
                            ,'layer' : 'annotation'
                            }
               ).set_pos((text_x , text_y + 50 - 10*i) , align='MIDDLE_CENTER')

  return file_name

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# loop thru all plates to draw...
for (p_id , lr_id) in [['back'         , ""     ]
                      ,['block'        , ""     ]
                      ,['side'         , 'left' ]
                      ,['side'         , 'right']
                      ,['motor_spacer' , ""     ]
                      ,['nut_spacer'   , ""     ]
                      ]:

  # Create a new DXF R2010 drawing, official DXF version name: "AC1024"
  doc = ezdxf.new('R2010' , setup=True)

  doc.layers.add(name="annotation"     , color=2)
  doc.layers.add(name="outline"        , color=2)

  # Add new entities to the modelspace:
  msp = doc.modelspace()

  file_name = 'Portal/' + Portal_plate(p_id , lr_id)

  doc.saveas(file_name)

  print("INFO: file '%s' written" % file_name)




