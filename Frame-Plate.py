import ezdxf
import math

# free parameters
cfg = {'Frame'  : {'front'  : {'thickness' :  10,'material'  : 'alu'}
                  ,'back'   : {'thickness' :  10,'material'  : 'alu'}
                  ,'block'  : {'thickness' :  10,'material'  : 'alu'}
                  }
      ,'Portal' : {'side'   : {'thickness' :  10,'material'  : 'alu'}
                  }
      }

# non obvious dependencies:
#  * if you choose the frame.block.thickness >10mm you have to either shorten the Y-ballscrews(difficult) or grow the frame in y-direction(easy)

# ============================================================================================================

def BF12 (lr_id , cx , cy):   # center of ballscrew
  hole1  =   5.2
  hole2  =  26

  if (lr_id == 'left'):
    mx = 1
  else:
    mx = -1

  msp.add_circle(((cx     ) * mx , cy      ) , hole2/2)

  msp.add_circle(((cx - 23) * mx , cy      ) , hole1/2)
  msp.add_circle(((cx + 23) * mx , cy      ) , hole1/2)
  msp.add_circle(((cx - 23) * mx , cy  - 18) , hole1/2)
  msp.add_circle(((cx + 23) * mx , cy  - 18) , hole1/2)

  # add outline
  msp.add_lwpolyline([( (cx-30)*mx , cy-25     )
                     ,( (cx+30)*mx , cy-25     )
                     ,( (cx+30)*mx , cy-25+32.5)
                     ,( (cx+17)*mx , cy-25+32.5)
                     ,( (cx+17)*mx , cy-25+43  )
                     ,( (cx-17)*mx , cy-25+43  )
                     ,( (cx-17)*mx , cy-25+32.5)
                     ,( (cx-30)*mx , cy-25+32.5)
                     ,( (cx-30)*mx , cy-25     )
                     ]
                    , dxfattribs={'layer': 'outline'}
                    )

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def BK12 (lr_id , cx , cy):   # center of ballscrew
  hole1  =   5.2

  if (lr_id == 'left'):
    mx = 1
  else:
    mx = -1

  msp.add_circle(((cx - 23) * mx , cy      ) , hole1/2)
  msp.add_circle(((cx + 23) * mx , cy      ) , hole1/2)
  msp.add_circle(((cx - 23) * mx , cy  - 18) , hole1/2)
  msp.add_circle(((cx + 23) * mx , cy  - 18) , hole1/2)

  # add outline
  msp.add_lwpolyline([( (cx-30)*mx , cy-25     )
                     ,( (cx+30)*mx , cy-25     )
                     ,( (cx+30)*mx , cy-25+32.5)
                     ,( (cx+17)*mx , cy-25+32.5)
                     ,( (cx+17)*mx , cy-25+43  )
                     ,( (cx-17)*mx , cy-25+43  )
                     ,( (cx-17)*mx , cy-25+32.5)
                     ,( (cx-30)*mx , cy-25+32.5)
                     ,( (cx-30)*mx , cy-25     )
                     ]
                    , dxfattribs={'layer': 'outline'}
                    )

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

  msp.add_circle(((cx - width/2) * mx , cy  + width/2) , hole1/2)
  msp.add_circle(((cx + width/2) * mx , cy  + width/2) , hole1/2)
  msp.add_circle(((cx - width/2) * mx , cy  - width/2) , hole1/2)
  msp.add_circle(((cx + width/2) * mx , cy  - width/2) , hole1/2)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Block_connect (lr_id , cx , cy):   # center of ballscrew
  hole  =   6.2

  if (lr_id == 'left'):
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

def Face40x80 (lr_id , cx , cy):   # center of profile
  hole  =   5.2

  if (lr_id == 'left'):
    mx = 1
  else:
    mx = -1

  for yi in range(0,4):
    msp.add_circle(((cx - 10) * mx , cy + 30 - yi*20) , hole/2)
    msp.add_circle(((cx + 10) * mx , cy + 30 - yi*20) , hole/2)

  # add outline
  msp.add_lwpolyline([( (cx-20)*mx , cy-40     )
                     ,( (cx+20)*mx , cy-40     )
                     ,( (cx+20)*mx , cy+40     )
                     ,( (cx-20)*mx , cy+40     )
                     ,( (cx-20)*mx , cy-40     )
                     ]
                    , dxfattribs={'layer': 'outline'}
                    )

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Side40x40 (lr_id , cx , cy):   # center of holes
  hole  =   5.2

  if (lr_id == 'left'):
    mx = 1
  else:
    mx = -1

  for xi in range(0,4):
    msp.add_circle(((cx + 30 - xi*20) * mx , cy - 10) , hole/2)
    msp.add_circle(((cx + 30 - xi*20) * mx , cy + 10) , hole/2)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Frame_Plate(fb_id , lr_id):
  file_name = ('Frame-Plate-%s-%s.dxf' % (fb_id , lr_id))

  if (lr_id == 'left'):
    # normal direction
    mx      = 1
  elif (lr_id == 'right'):
    # mirrored in x-direction
    mx      = -1
  else:
    print("ERROR: don't know how to draw Frame_Plate(%s,%s" % (fb_id , lr_id))
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


  if (fb_id == 'front'
      or
      fb_id == 'back'
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
    Face40x80(lr_id ,  68   +shift_x ,   0)
    Side40x40(lr_id , 126.75+shift_x , -20)   # x is rounded, should be uncritical

    if (fb_id == 'front'):
      # front
      BF12         (lr_id ,   0    ,   0)
    elif (fb_id == 'back'):
      # back
      NEMA23       (lr_id ,   0    ,   0)
      Block_connect(lr_id ,   0    ,   0)

    width  = (x2-x0)
    height = (y2-y0)

    text_x = (x2-x0) / 2 *mx
    text_y = y2 + 60

  elif (fb_id == 'block'):
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
    Block_connect(lr_id ,   0    ,   0)
    BK12         (lr_id ,   0    ,   0)

    width  = (x3-x0)
    height = (y3-y0)

    text_x = (x3-x0) / 2 *mx
    text_y = y3 + 60

  else:
    print("ERROR: don't know how to draw Frame_Plate(%s,%s)" % (fb_id , lr_id))
    exit(1)


  # add identifying text
  txt = (                 "%s" % file_name
        ,    "width=%5.2f[mm]" % width
        ,   "height=%5.2f[mm]" % height
        ,"thickness=%5.2f[mm]" % (cfg['Frame'][fb_id]['thickness'])
        , "material=%s"        % (cfg['Frame'][fb_id]['material'])
        )

  for i in range(0,5):
    msp.add_text(txt[i]
                ,dxfattribs={'style' : 'LiberationSerif'
                            ,'height': 5
                            ,'layer' : 'annotation'
                            }
               ).set_pos((text_x , text_y - 10*i) , align='MIDDLE_CENTER')

  return file_name

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# loop thru all plates to draw...
for fb_id in ['front' , 'back' , 'block']:
  for lr_id in ['left' , 'right']:

    # Create a new DXF R2010 drawing, official DXF version name: "AC1024"
    doc = ezdxf.new('R2010' , setup=True)

    doc.layers.add(name="annotation"     , color=2)
    doc.layers.add(name="outline"        , color=2)

    # Add new entities to the modelspace:
    msp = doc.modelspace()

    file_name = 'Frame/' + Frame_Plate(fb_id , lr_id)

    doc.saveas(file_name)

    print("INFO: file '%s' written" % file_name)
