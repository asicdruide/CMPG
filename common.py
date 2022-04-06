import math

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

def SFU1204_nutholder(msp , cx , cy , rotate , context):
  hole   =   5.2
  hole2  =   9   # counter bore

  holes = [[cx - 24/2 , cy - 35 / 2]
          ,[cx + 24/2 , cy - 35 / 2]
          ,[cx + 24/2 , cy + 35 / 2]
          ,[cx - 24/2 , cy + 35 / 2]
          ]

  for x,y in holes:
    msp.add_circle(rotateXY(x , y , cx , cy , rotate) ,   hole/2)
    # place holes and annotation
    if (context == 'spindle'):
      msp.add_circle(rotateXY(x , y , cx , cy , rotate) ,   hole2/2 , dxfattribs={'layer' : 'annotation'})

  if (context == 'spindle'):
    msp.add_text("counterbored 5mm deep"
                ,dxfattribs={'style' : 'LiberationSerif'
                            ,'height': 5
                            ,'layer' : 'annotation'
                            }
               ).set_pos((0 , cy) , align='MIDDLE_CENTER')
    layer = 'outline'
  else:
    layer = '0'


  # draw outline
  (x1,x2) = [-36 /2 , 36/2]
  (y2,y1) = [ 50 /2
            ,-50 /2
            ]

  cr    = 1                     # corner radius
  cb90  = 0.4142135             # corner bulge = tan(22.5°) for 90° corners

  (p1x,p1y) = rotateXY(cx+x1+cr , cy+y1          , cx , cy , rotate)
  (p2x,p2y) = rotateXY(cx+x2-cr , cy+y1          , cx , cy , rotate)
  (p3x,p3y) = rotateXY(cx+x2    , cy+y1+cr       , cx , cy , rotate)
  (p4x,p4y) = rotateXY(cx+x2    , cy+y2-cr       , cx , cy , rotate)
  (p5x,p5y) = rotateXY(cx+x2-cr , cy+y2          , cx , cy , rotate)
  (p6x,p6y) = rotateXY(cx+x1+cr , cy+y2          , cx , cy , rotate)
  (p7x,p7y) = rotateXY(cx+x1    , cy+y2-cr       , cx , cy , rotate)
  (p8x,p8y) = rotateXY(cx+x1    , cy+y1+cr       , cx , cy , rotate)


  shape = msp.add_lwpolyline([(p1x,p1y , 0   ) # 1
                             ,(p2x,p2y , cb90) # 2
                             ,(p3x,p3y , 0   ) # 3
                             ,(p4x,p4y , cb90) # 4
                             ,(p5x,p5y , 0   ) # 5
                             ,(p6x,p6y , cb90) # 6
                             ,(p7x,p7y , 0   ) # 7
                             ,(p8x,p8y , cb90) # 8
                             ]
                            , format='xyb'
                            , dxfattribs={'layer': layer}
                            )
  shape.close(True)


  # mark center
  msp.add_point((cx , cy) , dxfattribs={'layer': 'outline'})

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# floating end ballscrew support
def BF12_face(msp , cx , cy , rotate):   # center of ballscrew
  hole1  =   5.2
  hole2  =  26
  B      =  60
  h      =  25
  H1     =  32.5
  H      =  43
  B1     =  34
  P      =  46
  E      =  18

  msp.add_circle(     rotateXY(cx     , cy         , cx , cy , rotate) , hole2/2) # the large hole
  msp.add_circle(     rotateXY(cx-P/2 , cy         , cx , cy , rotate) , hole1/2) # mounting holes
  msp.add_circle(     rotateXY(cx+P/2 , cy         , cx , cy , rotate) , hole1/2) # mounting holes
  msp.add_circle(     rotateXY(cx-P/2 , cy-E       , cx , cy , rotate) , hole1/2) # mounting holes
  msp.add_circle(     rotateXY(cx+P/2 , cy-E       , cx , cy , rotate) , hole1/2) # mounting holes

  # draw outline
  shape = msp.add_lwpolyline([rotateXY(cx-B/2 , cy-h       , cx , cy , rotate)  # 1
                             ,rotateXY(cx+B/2 , cy-h       , cx , cy , rotate)  # 2
                             ,rotateXY(cx+B/2 , cy-h+H1    , cx , cy , rotate)  # 3
                             ,rotateXY(cx+B1/2, cy-h+H1    , cx , cy , rotate)  # 4
                             ,rotateXY(cx+B1/2, cy-h+H     , cx , cy , rotate)  # 5
                             ,rotateXY(cx-B1/2, cy-h+H     , cx , cy , rotate)  # 6
                             ,rotateXY(cx-B1/2, cy-h+H1    , cx , cy , rotate)  # 7
                             ,rotateXY(cx-B/2 , cy-h+H1    , cx , cy , rotate)  # 8
                             ]
                            , dxfattribs={'layer': 'outline'}
                            )

  shape.close(True)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# floating end ballscrew support
def BF10_face(msp , cx , cy , rotate):   # center of ballscrew
  hole1  =   5.2
  hole2  =  23
  B      =  60
  h      =  22
  H1     =  32.5
  H      =  39
  B1     =  34
  P      =  46
  E      =  15

  msp.add_circle(     rotateXY(cx     , cy         , cx , cy , rotate) , hole2/2) # the large hole
  msp.add_circle(     rotateXY(cx-P/2 , cy         , cx , cy , rotate) , hole1/2) # mounting holes
  msp.add_circle(     rotateXY(cx+P/2 , cy         , cx , cy , rotate) , hole1/2) # mounting holes
  msp.add_circle(     rotateXY(cx-P/2 , cy-E       , cx , cy , rotate) , hole1/2) # mounting holes
  msp.add_circle(     rotateXY(cx+P/2 , cy-E       , cx , cy , rotate) , hole1/2) # mounting holes

  # draw outline
  shape = msp.add_lwpolyline([rotateXY(cx-B/2 , cy-h       , cx , cy , rotate)  # 1
                             ,rotateXY(cx+B/2 , cy-h       , cx , cy , rotate)  # 2
                             ,rotateXY(cx+B/2 , cy-h+H1    , cx , cy , rotate)  # 3
                             ,rotateXY(cx+B1/2, cy-h+H1    , cx , cy , rotate)  # 4
                             ,rotateXY(cx+B1/2, cy-h+H     , cx , cy , rotate)  # 5
                             ,rotateXY(cx-B1/2, cy-h+H     , cx , cy , rotate)  # 6
                             ,rotateXY(cx-B1/2, cy-h+H1    , cx , cy , rotate)  # 7
                             ,rotateXY(cx-B/2 , cy-h+H1    , cx , cy , rotate)  # 8
                             ]
                            , dxfattribs={'layer': 'outline'}
                            )
  shape.close(True)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# floating end ballscrew support
def BF10_footprint(msp , cx , cy , rotate):
  hole1  =   5.0
  B      =  60
  L      =  20
  P      =  46

  msp.add_circle(     rotateXY(cx , cy-P/2         , cx , cy , rotate) , hole1/2) # mounting holes
  msp.add_circle(     rotateXY(cx , cy+P/2         , cx , cy , rotate) , hole1/2) # mounting holes

  # draw outline
  shape = msp.add_lwpolyline([rotateXY(cx-L/2 , cy-B/2     , cx , cy , rotate)  # 1
                             ,rotateXY(cx+L/2 , cy-B/2     , cx , cy , rotate)  # 2
                             ,rotateXY(cx+L/2 , cy+B/2     , cx , cy , rotate)  # 3
                             ,rotateXY(cx-L/2 , cy+B/2     , cx , cy , rotate)  # 4
                             ]
                            , dxfattribs={'layer': 'outline'}
                            )
  shape.close(True)

  # mark center
  msp.add_point((cx , cy) , dxfattribs={'layer': 'outline'})

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# fixed end ballscrew support
def BK10_footprint(msp , cx , cy , rotate):
  hole   =   5.0
  B      =  60
  L2     =  25
  P      =  46
  C1     =  13

  # mounting holes
  for (x,y) in [rotateXY(cx - C1/2 , cy - P/2, cx , cy , rotate)
               ,rotateXY(cx - C1/2 , cy + P/2, cx , cy , rotate)
               ,rotateXY(cx + C1/2 , cy - P/2, cx , cy , rotate)
               ,rotateXY(cx + C1/2 , cy + P/2, cx , cy , rotate)
               ]:
    msp.add_circle((x , y) , hole/2)


  # draw outline
  shape = msp.add_lwpolyline([rotateXY(cx-L2/2 , cy-B/2     , cx , cy , rotate)  # 1
                             ,rotateXY(cx+L2/2 , cy-B/2     , cx , cy , rotate)  # 2
                             ,rotateXY(cx+L2/2 , cy+B/2     , cx , cy , rotate)  # 3
                             ,rotateXY(cx-L2/2 , cy+B/2     , cx , cy , rotate)  # 4
                             ]
                            , dxfattribs={'layer': 'outline'}
                            )
  shape.close(True)

  # mark center
  msp.add_point((cx , cy) , dxfattribs={'layer': 'outline'})

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

  # mark center
  msp.add_point((cx , cy) , dxfattribs={'layer': 'outline'})

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

def MGN12H(msp , cx , cy , rotate , counterbore_depth):
  width  =  20
  height =  20
  hole   =   3.2

  holes = [rotateXY(cx - width/2 , cy - height/2, cx , cy , rotate)
          ,rotateXY(cx - width/2 , cy + height/2, cx , cy , rotate)
          ,rotateXY(cx + width/2 , cy - height/2, cx , cy , rotate)
          ,rotateXY(cx + width/2 , cy + height/2, cx , cy , rotate)
          ]



  # mouting holes
  for (x,y) in holes:
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


  if (counterbore_depth > 0):
    hole2  =   8   # counter bore

    for (x,y) in holes:
      msp.add_circle((x  , y) , hole2/2 , dxfattribs={'layer' : 'annotation'})

    msp.add_text("counterbored %dmm deep" % counterbore_depth
                ,dxfattribs={'style' : 'LiberationSerif'
                            ,'height': 5
                            ,'layer' : 'annotation'
                            }
               ).set_pos((cx , cy) , align='MIDDLE_CENTER')

  # mark center
  msp.add_point((cx , cy) , dxfattribs={'layer': 'outline'})

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

  # mark center
  msp.add_point((cx , cy) , dxfattribs={'layer': 'outline'})

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

  # mark center
  msp.add_point((cx , cy) , dxfattribs={'layer': 'outline'})

  if (counterbore_depth > 0):
    hole2  =   9   # counter bore

    for (x,y) in holes:
      msp.add_circle((x  , y) , hole2/2 , dxfattribs={'layer' : 'annotation'})

    msp.add_text("counterbored %dmm deep" % counterbore_depth
                ,dxfattribs={'style' : 'LiberationSerif'
                            ,'height': 5
                            ,'layer' : 'annotation'
                            }
               ).set_pos((cx , cy) , align='MIDDLE_CENTER')

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

