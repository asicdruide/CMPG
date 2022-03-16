import math

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def SFU1204_nutholder(msp , cy , orientation):
  if (orientation == 'footprint_vertical'):
    width  =  35
    height =  24
  else:
    print("unknown orientation '%s' at SFU1204_nutholder" % orientation)
    exit(1)

  hole   =   5.2
  hole2  =   9   # counter bore

  holes = [[-width / 2 , cy - height / 2]
          ,[+width / 2 , cy - height / 2]
          ,[+width / 2 , cy + height / 2]
          ,[-width / 2 , cy + height / 2]
          ]

  for x,y in holes:
    msp.add_circle((x , y) ,   hole/2)
    # place holes and annotation
    msp.add_circle((x , y) ,   hole2/2 , dxfattribs={'layer' : 'annotation'})

  msp.add_text("counterbored 5mm deep"
              ,dxfattribs={'style' : 'LiberationSerif'
                          ,'height': 5
                          ,'layer' : 'annotation'
                          }
             ).set_pos((0 , cy) , align='MIDDLE_CENTER')

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def rotateXY(px , py , cx , cy , angle):
  # Rotation (Drehung)
  # Durch das Drehen eines Objektes mit dem Winkel θ um den Koordinatenursprung kommt der Punkt (x,y) auf
  # (x´,y´) = (x·cosθ – y·sinθ, x·sinθ + y·cosθ)
  # zu liegen.
  x = px - cx
  y = py - cy

  sinA = math.sin(angle*math.pi / 180)
  cosA = math.cos(angle*math.pi / 180)

  xx = x*cosA - y*sinA
  yy = x*sinA + y*cosA

  return (xx+cx , yy+cy)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# floating end ballscrew support
def BF12_face(msp , cx , cy , rotate):   # center of ballscrew
  hole1  =   5.2
  hole2  =  26

  msp.add_circle(     rotateXY(cx    , cy         , cx , cy , rotate) , hole2/2) # the large hole
  msp.add_circle(     rotateXY(cx-23 , cy         , cx , cy , rotate) , hole1/2) # mounting holes
  msp.add_circle(     rotateXY(cx+23 , cy         , cx , cy , rotate) , hole1/2) # mounting holes
  msp.add_circle(     rotateXY(cx-23 , cy-18      , cx , cy , rotate) , hole1/2) # mounting holes
  msp.add_circle(     rotateXY(cx+23 , cy-18      , cx , cy , rotate) , hole1/2) # mounting holes

  # draw outline
  shape = msp.add_lwpolyline([rotateXY(cx-30 , cy-25      , cx , cy , rotate)
                             ,rotateXY(cx+30 , cy-25      , cx , cy , rotate)
                             ,rotateXY(cx+30 , cy-25+32.5 , cx , cy , rotate)
                             ,rotateXY(cx+17 , cy-25+32.5 , cx , cy , rotate)
                             ,rotateXY(cx+17 , cy-25+43   , cx , cy , rotate)
                             ,rotateXY(cx-17 , cy-25+43   , cx , cy , rotate)
                             ,rotateXY(cx-17 , cy-25+32.5 , cx , cy , rotate)
                             ,rotateXY(cx-30 , cy-25+32.5 , cx , cy , rotate)
                             ]
                            , dxfattribs={'layer': 'outline'}
                            )
  shape.close(True)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# fixed end ballscrew support
def BK12_face(msp , cx , cy , rotate):   # center of ballscrew
  hole1  =   5.2

  msp.add_circle(     rotateXY(cx-23 , cy         , cx , cy , rotate) , hole1/2) # mounting holes
  msp.add_circle(     rotateXY(cx+23 , cy         , cx , cy , rotate) , hole1/2) # mounting holes
  msp.add_circle(     rotateXY(cx-23 , cy-18      , cx , cy , rotate) , hole1/2) # mounting holes
  msp.add_circle(     rotateXY(cx+23 , cy-18      , cx , cy , rotate) , hole1/2) # mounting holes

  # draw outline
  shape = msp.add_lwpolyline([rotateXY(cx-30 , cy-25      , cx , cy , rotate)
                             ,rotateXY(cx+30 , cy-25      , cx , cy , rotate)
                             ,rotateXY(cx+30 , cy-25+32.5 , cx , cy , rotate)
                             ,rotateXY(cx+17 , cy-25+32.5 , cx , cy , rotate)
                             ,rotateXY(cx+17 , cy-25+43   , cx , cy , rotate)
                             ,rotateXY(cx-17 , cy-25+43   , cx , cy , rotate)
                             ,rotateXY(cx-17 , cy-25+32.5 , cx , cy , rotate)
                             ,rotateXY(cx-30 , cy-25+32.5 , cx , cy , rotate)
                             ]
                            , dxfattribs={'layer': 'outline'}
                            )
  shape.close(True)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
def NEMA23 (msp , cx , cy , rotate):   # center of axis
  hole1  =   5.2
  hole2  =  38.5
  width  = 47.14
  ow     = 57
  cr     =  3

  msp.add_circle(rotateXY(cx           , cy                , cx , cy , rotate) , hole2/2) # the large hole
  msp.add_circle(rotateXY(cx - width/2 , cy - width/2      , cx , cy , rotate) , hole1/2) # mounting holes
  msp.add_circle(rotateXY(cx - width/2 , cy + width/2      , cx , cy , rotate) , hole1/2) # mounting holes
  msp.add_circle(rotateXY(cx + width/2 , cy - width/2      , cx , cy , rotate) , hole1/2) # mounting holes
  msp.add_circle(rotateXY(cx + width/2 , cy + width/2      , cx , cy , rotate) , hole1/2) # mounting holes

  # add outline
  shape = msp.add_lwpolyline([rotateXY(cx - ow/2 + cr, cy - ow/2     , cx , cy , rotate)   # 1
                             ,rotateXY(cx + ow/2 - cr, cy - ow/2     , cx , cy , rotate)   # 2
                             ,rotateXY(cx + ow/2     , cy - ow/2 + cr, cx , cy , rotate)   # 3
                             ,rotateXY(cx + ow/2     , cy + ow/2 - cr, cx , cy , rotate)   # 4
                             ,rotateXY(cx + ow/2 - cr, cy + ow/2     , cx , cy , rotate)   # 5
                             ,rotateXY(cx - ow/2 + cr, cy + ow/2     , cx , cy , rotate)   # 6
                             ,rotateXY(cx - ow/2     , cy + ow/2 - cr, cx , cy , rotate)   # 7
                             ,rotateXY(cx - ow/2     , cy - ow/2 + cr, cx , cy , rotate)   # 8
                             ]
                            , dxfattribs={'layer': 'outline'}
                            )
  shape.close(True)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Face40x80 (msp , cx , cy , rotate):   # center of profile
  hole = 5.2

  for yi in range(0,4):
    msp.add_circle(rotateXY(cx-10 , cy+30-yi*20    , cx , cy , rotate) , hole/2)
    msp.add_circle(rotateXY(cx+10 , cy+30-yi*20    , cx , cy , rotate) , hole/2)

  # add outline
  shape = msp.add_lwpolyline([rotateXY( cx-20 , cy-40  , cx , cy , rotate)
                             ,rotateXY( cx+20 , cy-40  , cx , cy , rotate)
                             ,rotateXY( cx+20 , cy+40  , cx , cy , rotate)
                             ,rotateXY( cx-20 , cy+40  , cx , cy , rotate)
                             ]
                            , dxfattribs={'layer': 'outline'}
                            )
  shape.close(True)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Side40x40 (msp , cx , cy, rotate):   # center of holes
  hole  =   5.2

  for xi in range(0,4):
    msp.add_circle(rotateXY(cx+30-xi*20 , cy-10, cx , cy , rotate) , hole/2)
    msp.add_circle(rotateXY(cx+30-xi*20 , cy+10, cx , cy , rotate) , hole/2)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def MGN12H(msp , cx , cy , rotate):
  width  =  20
  height =  20
  hole   =   3.2

  # mouting holes
  for (x,y) in [rotateXY(cx - width/2 , cy - height/2, cx , cy , rotate)
               ,rotateXY(cx - width/2 , cy + height/2, cx , cy , rotate)
               ,rotateXY(cx + width/2 , cy - height/2, cx , cy , rotate)
               ,rotateXY(cx + width/2 , cy + height/2, cx , cy , rotate)
               ]:
    msp.add_circle((x , y) , hole/2)

  width  = 45.4
  height = 27

  # add outline
  shape = msp.add_lwpolyline([rotateXY(cx - width/2 , cy - height/2 , cx , cy , rotate)
                             ,rotateXY(cx + width/2 , cy - height/2 , cx , cy , rotate)
                             ,rotateXY(cx + width/2 , cy + height/2 , cx , cy , rotate)
                             ,rotateXY(cx - width/2 , cy + height/2 , cx , cy , rotate)
                             ]
                            , dxfattribs={'layer': 'outline'}
                            )
  shape.close(True)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def SFU1605_holder(msp , cx , cy , rotate):
  width  =  24
  height =  40
  ow     =  40
  oh     =  52

  hole   = 5.2

  # mounting holes
  for (x,y) in [rotateXY(cx - width/2 , cy - height/2, cx , cy , rotate)
               ,rotateXY(cx - width/2 , cy + height/2, cx , cy , rotate)
               ,rotateXY(cx + width/2 , cy - height/2, cx , cy , rotate)
               ,rotateXY(cx + width/2 , cy + height/2, cx , cy , rotate)
               ]:
    msp.add_circle((x , y) , hole/2)


  # add outline
  shape = msp.add_lwpolyline([rotateXY(cx - ow/2 , cy - oh/2 , cx , cy , rotate)
                             ,rotateXY(cx + ow/2 , cy - oh/2 , cx , cy , rotate)
                             ,rotateXY(cx + ow/2 , cy + oh/2 , cx , cy , rotate)
                             ,rotateXY(cx - ow/2 , cy + oh/2 , cx , cy , rotate)
                             ]
                            , dxfattribs={'layer': 'outline'}
                            )
  shape.close(True)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Face40x60 (msp , cx , cy , rotate , counterbore_depth):   # center of profile
  hole = 5.2

  holes =  [rotateXY(cx - 20 , cy + 10 , cx , cy , rotate)
           ,rotateXY(cx - 20 , cy - 10 , cx , cy , rotate)
           ,rotateXY(cx      , cy + 10 , cx , cy , rotate)
           ,rotateXY(cx      , cy - 10 , cx , cy , rotate)
           ,rotateXY(cx + 20 , cy + 10 , cx , cy , rotate)
           ,rotateXY(cx + 20 , cy - 10 , cx , cy , rotate)
           ]


  for (x,y) in holes:
    msp.add_circle((x , y) , hole/2)


  # add outline
  shape = msp.add_lwpolyline([rotateXY(cx-30 , cy-20 , cx , cy , rotate)
                             ,rotateXY(cx+30 , cy-20 , cx , cy , rotate)
                             ,rotateXY(cx+30 , cy+20 , cx , cy , rotate)
                             ,rotateXY(cx-30 , cy+20 , cx , cy , rotate)
                             ]
                            , dxfattribs={'layer': 'outline'}
                            )

  shape.close(True)


  if (counterbore_depth > 0):
    hole2  =   9   # counter bore

    for (x,y) in holes:
      msp.add_circle((x  , y) , hole2/2 , dxfattribs={'layer' : 'annotation'})

    msp.add_text("counterbored %d[mm] deep" % counterbore_depth
                ,dxfattribs={'style' : 'LiberationSerif'
                            ,'height': 5
                            ,'layer' : 'annotation'
                            }
               ).set_pos((cx , cy) , align='MIDDLE_CENTER')







  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

