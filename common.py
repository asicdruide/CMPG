import math

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Add2BOM(ctx , cnt , what , variant, doc):

  possible = {'DIN912 M3' : [4,5,6,8,10,12,14,16,18,20,22,25,30,35,40,45,50                            ]   # schraubenkasten.de
             ,'DIN912 M4' : [4,5,6,8,10,12,14,16,18,20,22,25,30,35,40,45,50,55,60,   70,   80          ]   # schraubenkasten.de
             ,'DIN912 M5' : [    6,8,10,12,14,16,18,20,22,25,30,35,40,45,50,55,60,65,70,75,80,   90,100]   # schraubenkasten.de
             ,'DIN912 M6' : [    6,8,10,12,14,16,18,20,22,25,30,35,40,45,50,55,60,65,70,75,80,85,90,100]   # schraubenkasten.de
             }
  var = variant.split('x')
  sel = "%s %s" % (what , var[0])

  if (sel in possible.keys()):
    # select length closest to requested length...
    rl        = int(var[1]) # requested length
    min_error = 1000

    for pl in possible[sel]:
      error = abs(pl - rl)

      if (error <= min_error):
        sl        = pl
        min_error = error

    if (min_error > 0):
      variant = "%sx%s" % (var[0] , sl)
      doc    += ' (exact:%d)' % (rl)

  if (what in ctx['bom'].keys()):
    if (variant in ctx['bom'][what].keys()):
      ctx['bom'][what][variant].append((cnt , doc))
    else:
      ctx['bom'][what][variant] = [(cnt , doc)]
  else:
    ctx['bom'][what] = {variant : [(cnt , doc)]}

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def EnsureLayer(ctx, name , doc):
  colors = {"thx"    :   1   # red
           ,"th68"   :   2   # yellow
           ,"th62"   :   4   # cyan
           ,"th52"   :  30   # orange
           ,"th50"   :   7   # white
           ,"th32"   :   3   # green
           ,"cb3x5"  :   1   # red
           ,"cb8x5"  :   5   # blue
           ,"cb9x5"  :   6   # magenta
           ,"cb11x6" :  96   #
           }

  if (not name in ctx['lay'].keys()):
    # new layer...
    if (name in colors.keys()):
      color = colors[name]
    else:
      color = 1

    ctx['doc'].layers.add(name=name , color=color)
    ctx['lay'][name] = doc

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Screw(variant , length):

  return "%sx%d" % (variant , length+0.5)

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

def SFU1204_nutholder(ctx , cx , cy , rotate , context):
  uf     = ctx['unit_factor']
  hole   =   5.2
  hole2  =   9   # counter bore

  holes = [[cx - 24/2 , cy - 35 / 2]
          ,[cx + 24/2 , cy - 35 / 2]
          ,[cx + 24/2 , cy + 35 / 2]
          ,[cx - 24/2 , cy + 35 / 2]
          ]

  EnsureLayer  (ctx , 'th52' , 'through hole 5.2mm (M5 screw)')
  if (context == 'front'):
    EnsureLayer(ctx , 'cb9x5' , 'counter bore 9mm diameter 5mm deep')


  for x,y in holes:
    ctx['msp'].add_circle(rotateXY(x*uf , y*uf , cx*uf , cy*uf , rotate) ,   hole/2*uf , dxfattribs={'layer' : 'th52'})
    # place holes and annotation
    if (context == 'front'):
      ctx['msp'].add_circle(rotateXY(x*uf , y*uf , cx*uf , cy*uf , rotate) ,   hole2/2*uf , dxfattribs={'layer' : 'cb9x5'})

  if (context == 'front'):
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


  shape = ctx['msp'].add_lwpolyline([(p1x*uf , p1y*uf , 0   ) # 1
                                    ,(p2x*uf , p2y*uf , cb90) # 2
                                    ,(p3x*uf , p3y*uf , 0   ) # 3
                                    ,(p4x*uf , p4y*uf , cb90) # 4
                                    ,(p5x*uf , p5y*uf , 0   ) # 5
                                    ,(p6x*uf , p6y*uf , cb90) # 6
                                    ,(p7x*uf , p7y*uf , 0   ) # 7
                                    ,(p8x*uf , p8y*uf , cb90) # 8
                                    ]
                                   , format='xyb'
                                   , dxfattribs={'layer': layer}
                                   )
  shape.close(True)


  # mark center
  ctx['msp'].add_point((cx*uf , cy*uf) , dxfattribs={'layer': 'outline'})

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# floating end ballscrew support
def BF12_face(ctx , cx , cy , rotate , cb_depth):   # center of ballscrew
  uf     = ctx['unit_factor']
  hole1  =   5.2
  hole2  =  26
  B      =  60
  h      =  25
  H1     =  32.5
  H      =  43
  B1     =  34
  P      =  46
  E      =  18

  EnsureLayer(ctx , 'th52' , 'through hole 5.2mm (M5 screw)')
  EnsureLayer(ctx , 'thx'  , 'through hole %dmm' % (hole2))

  mounting_holes = (rotateXY(cx-P/2 , cy         , cx , cy , rotate)
                   ,rotateXY(cx+P/2 , cy         , cx , cy , rotate)
                   ,rotateXY(cx-P/2 , cy-E       , cx , cy , rotate)
                   ,rotateXY(cx+P/2 , cy-E       , cx , cy , rotate)
                   )

  for (x,y) in mounting_holes:
    ctx['msp'].add_circle((x*uf,y*uf) , hole1/2*uf , dxfattribs={'layer' : 'th52'})

  ctx['msp'].add_circle(     rotateXY(cx*uf     , cy*uf         , cx*uf , cy*uf , rotate) , hole2/2*uf, dxfattribs={'layer': 'thx' }) # the large hole

  # draw outline
  shape = ctx['msp'].add_lwpolyline([rotateXY((cx-B/2 )*uf, (cy-h   )*uf , cx*uf , cy*uf , rotate)  # 1
                                    ,rotateXY((cx+B/2 )*uf, (cy-h   )*uf , cx*uf , cy*uf , rotate)  # 2
                                    ,rotateXY((cx+B/2 )*uf, (cy-h+H1)*uf , cx*uf , cy*uf , rotate)  # 3
                                    ,rotateXY((cx+B1/2)*uf, (cy-h+H1)*uf , cx*uf , cy*uf , rotate)  # 4
                                    ,rotateXY((cx+B1/2)*uf, (cy-h+H )*uf , cx*uf , cy*uf , rotate)  # 5
                                    ,rotateXY((cx-B1/2)*uf, (cy-h+H )*uf , cx*uf , cy*uf , rotate)  # 6
                                    ,rotateXY((cx-B1/2)*uf, (cy-h+H1)*uf , cx*uf , cy*uf , rotate)  # 7
                                    ,rotateXY((cx-B/2 )*uf, (cy-h+H1)*uf , cx*uf , cy*uf , rotate)  # 8
                                    ]
                                   , dxfattribs={'layer': 'outline'}
                                   )

  shape.close(True)

  if (cb_depth > 0):
    hole3 = 9   # counter bore

    ln = 'cb%dx%d'                                     % (hole3 , cb_depth)
    ld = 'counter bore %3.1fmm diameter, %3.1fmm deep' % (hole3 , cb_depth)

    EnsureLayer(ctx , ln , ld)

    for (x,y) in mounting_holes:
      ctx['msp'].add_circle((x*uf,y*uf) , hole3/2*uf , dxfattribs={'layer' : ln})





  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# floating end ballscrew support
def BF10_face(ctx , cx , cy , rotate):   # center of ballscrew
  uf     = ctx['unit_factor']
  hole1  =   5.2
  hole2  =  23
  B      =  60
  h      =  22
  H1     =  32.5
  H      =  39
  B1     =  34
  P      =  46
  E      =  15

  EnsureLayer(ctx , 'th52' , 'through hole 5.0mm (M6 thread)')

  for (x,y) in [rotateXY(cx-P/2 , cy    , cx , cy , rotate)
               ,rotateXY(cx+P/2 , cy    , cx , cy , rotate)
               ,rotateXY(cx-P/2 , cy-E  , cx , cy , rotate)
               ,rotateXY(cx+P/2 , cy-E  , cx , cy , rotate)
               ]:
    ctx['msp'].add_circle((x*uf , y*uf) , hole1/2*uf, dxfattribs={'layer': 'th52'}) # mounting holes

  ctx['msp'].add_circle(     rotateXY((cx    )*uf , (cy  )*uf  , cx*uf , cy*uf , rotate) , hole2/2*uf) # the large hole


  # draw outline
  shape = ctx['msp'].add_lwpolyline([rotateXY((cx-B/2 )*uf , (cy-h   )*uf , cx*uf , cy*uf , rotate)  # 1
                                    ,rotateXY((cx+B/2 )*uf , (cy-h   )*uf , cx*uf , cy*uf , rotate)  # 2
                                    ,rotateXY((cx+B/2 )*uf , (cy-h+H1)*uf , cx*uf , cy*uf , rotate)  # 3
                                    ,rotateXY((cx+B1/2)*uf , (cy-h+H1)*uf , cx*uf , cy*uf , rotate)  # 4
                                    ,rotateXY((cx+B1/2)*uf , (cy-h+H )*uf , cx*uf , cy*uf , rotate)  # 5
                                    ,rotateXY((cx-B1/2)*uf , (cy-h+H )*uf , cx*uf , cy*uf , rotate)  # 6
                                    ,rotateXY((cx-B1/2)*uf , (cy-h+H1)*uf , cx*uf , cy*uf , rotate)  # 7
                                    ,rotateXY((cx-B/2 )*uf , (cy-h+H1)*uf , cx*uf , cy*uf , rotate)  # 8
                                    ]
                                   , dxfattribs={'layer': 'outline'}
                                   )
  shape.close(True)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# floating end ballscrew support
def BF10_footprint(ctx , cx , cy , rotate):
  uf     = ctx['unit_factor']
  hole1  =   5.0
  B      =  60
  L      =  20
  P      =  46

  EnsureLayer(ctx , 'th50' , 'through hole 5.0mm (M6 thread)')

  for (x,y) in [rotateXY(cx , cy-P/2  , cx , cy , rotate)
               ,rotateXY(cx , cy+P/2  , cx , cy , rotate)
               ]:
    ctx['msp'].add_circle((x*uf , y*uf) , hole1/2*uf, dxfattribs={'layer': 'th50'}) # mounting holes

  # draw outline
  shape = ctx['msp'].add_lwpolyline([rotateXY((cx-L/2)*uf , (cy-B/2)*uf , cx*uf , cy*uf , rotate)  # 1
                                    ,rotateXY((cx+L/2)*uf , (cy-B/2)*uf , cx*uf , cy*uf , rotate)  # 2
                                    ,rotateXY((cx+L/2)*uf , (cy+B/2)*uf , cx*uf , cy*uf , rotate)  # 3
                                    ,rotateXY((cx-L/2)*uf , (cy+B/2)*uf , cx*uf , cy*uf , rotate)  # 4
                                    ]
                                   , dxfattribs={'layer': 'outline'}
                                   )
  shape.close(True)

  # mark center
  ctx['msp'].add_point((cx*uf , cy*uf) , dxfattribs={'layer': 'outline'})

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# fixed end ballscrew support
def BK10_footprint(ctx , cx , cy , rotate):
  uf     = ctx['unit_factor']
  hole   =   5.0
  B      =  60
  L2     =  25
  P      =  46
  C1     =  13

  EnsureLayer(ctx , 'th50' , 'through hole 5.0mm (M6 thread)')

  # mounting holes
  for (x,y) in [rotateXY(cx - C1/2 , cy - P/2, cx , cy , rotate)
               ,rotateXY(cx - C1/2 , cy + P/2, cx , cy , rotate)
               ,rotateXY(cx + C1/2 , cy - P/2, cx , cy , rotate)
               ,rotateXY(cx + C1/2 , cy + P/2, cx , cy , rotate)
               ]:
    ctx['msp'].add_circle((x*uf , y*uf) , hole/2*uf, dxfattribs={'layer': 'th50'})


  # draw outline
  shape = ctx['msp'].add_lwpolyline([rotateXY((cx-L2/2)*uf , (cy-B/2)*uf , cx*uf , cy*uf , rotate)  # 1
                                    ,rotateXY((cx+L2/2)*uf , (cy-B/2)*uf , cx*uf , cy*uf , rotate)  # 2
                                    ,rotateXY((cx+L2/2)*uf , (cy+B/2)*uf , cx*uf , cy*uf , rotate)  # 3
                                    ,rotateXY((cx-L2/2)*uf , (cy+B/2)*uf , cx*uf , cy*uf , rotate)  # 4
                                    ]
                                   , dxfattribs={'layer': 'outline'}
                                   )
  shape.close(True)

  # mark center
  ctx['msp'].add_point((cx*uf , cy*uf) , dxfattribs={'layer': 'outline'})

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# fixed end ballscrew support
def BK12_face(ctx , cx , cy , rotate):   # center of ballscrew
  uf     = ctx['unit_factor']
  hole1  =   5.2

  EnsureLayer(ctx , 'th52' , 'through hole 5.2mm (M5 screw)')

  for (x,y) in [rotateXY(cx-23 , cy         , cx , cy , rotate)
               ,rotateXY(cx+23 , cy         , cx , cy , rotate)
               ,rotateXY(cx-23 , cy-18      , cx , cy , rotate)
               ,rotateXY(cx+23 , cy-18      , cx , cy , rotate)
               ]:
    ctx['msp'].add_circle((x*uf , y*uf) , hole1/2*uf, dxfattribs={'layer': 'th52'})

  # draw outline
  shape = ctx['msp'].add_lwpolyline([rotateXY((cx-30)*uf , (cy-25     )*uf , cx*uf , cy*uf , rotate)
                                    ,rotateXY((cx+30)*uf , (cy-25     )*uf , cx*uf , cy*uf , rotate)
                                    ,rotateXY((cx+30)*uf , (cy-25+32.5)*uf , cx*uf , cy*uf , rotate)
                                    ,rotateXY((cx+17)*uf , (cy-25+32.5)*uf , cx*uf , cy*uf , rotate)
                                    ,rotateXY((cx+17)*uf , (cy-25+43  )*uf , cx*uf , cy*uf , rotate)
                                    ,rotateXY((cx-17)*uf , (cy-25+43  )*uf , cx*uf , cy*uf , rotate)
                                    ,rotateXY((cx-17)*uf , (cy-25+32.5)*uf , cx*uf , cy*uf , rotate)
                                    ,rotateXY((cx-30)*uf , (cy-25+32.5)*uf , cx*uf , cy*uf , rotate)
                                    ]
                                   , dxfattribs={'layer': 'outline'}
                                   )
  shape.close(True)

  # mark center
  ctx['msp'].add_point((cx*uf , cy*uf) , dxfattribs={'layer': 'outline'})

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#
def NEMA23 (ctx , cx , cy , rotate):   # center of axis
  uf     = ctx['unit_factor']
  hole1  =   5.2
  hole2  =  38.5
  width  = 47.14
  ow     = 57
  cr     =  3

  EnsureLayer(ctx , 'thx'  , 'through hole 38.5mm')
  EnsureLayer(ctx , 'th52' , 'through hole 5.2mm (M5 screw)')

  for (x,y) in [rotateXY(cx - width/2 , cy - width/2      , cx , cy , rotate)
               ,rotateXY(cx - width/2 , cy + width/2      , cx , cy , rotate)
               ,rotateXY(cx + width/2 , cy - width/2      , cx , cy , rotate)
               ,rotateXY(cx + width/2 , cy + width/2      , cx , cy , rotate)
               ]:
    ctx['msp'].add_circle((x*uf , y*uf) , hole1/2*uf, dxfattribs={'layer': 'th52'})

  ctx['msp'].add_circle(rotateXY(cx*uf , cy*uf , cx*uf , cy*uf , rotate) , hole2/2*uf, dxfattribs={'layer': 'thx' }) # the large hole

  # add outline
  shape = ctx['msp'].add_lwpolyline([rotateXY((cx - ow/2 + cr)*uf, (cy - ow/2     )*uf , cx*uf , cy*uf , rotate)   # 1
                                    ,rotateXY((cx + ow/2 - cr)*uf, (cy - ow/2     )*uf , cx*uf , cy*uf , rotate)   # 2
                                    ,rotateXY((cx + ow/2     )*uf, (cy - ow/2 + cr)*uf , cx*uf , cy*uf , rotate)   # 3
                                    ,rotateXY((cx + ow/2     )*uf, (cy + ow/2 - cr)*uf , cx*uf , cy*uf , rotate)   # 4
                                    ,rotateXY((cx + ow/2 - cr)*uf, (cy + ow/2     )*uf , cx*uf , cy*uf , rotate)   # 5
                                    ,rotateXY((cx - ow/2 + cr)*uf, (cy + ow/2     )*uf , cx*uf , cy*uf , rotate)   # 6
                                    ,rotateXY((cx - ow/2     )*uf, (cy + ow/2 - cr)*uf , cx*uf , cy*uf , rotate)   # 7
                                    ,rotateXY((cx - ow/2     )*uf, (cy - ow/2 + cr)*uf , cx*uf , cy*uf , rotate)   # 8
                                    ]
                                   , dxfattribs={'layer': 'outline'}
                                   )
  shape.close(True)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Face40x80 (ctx , cx , cy , rotate):   # center of profile
  uf   = ctx['unit_factor']
  hole = 5.2

  EnsureLayer(ctx , 'th52' , 'through hole 5.2mm (M5 screw)')

  for yi in range(0,4):
    for xi in [-10,10]:
      ctx['msp'].add_circle(rotateXY((cx+xi)*uf , (cy+30-yi*20)*uf    , cx*uf , cy*uf , rotate) , hole/2*uf, dxfattribs={'layer': 'th52'})

  # add outline
  shape = ctx['msp'].add_lwpolyline([rotateXY( (cx-20)*uf , (cy-40)*uf  , cx*uf , cy*uf , rotate)
                                    ,rotateXY( (cx+20)*uf , (cy-40)*uf  , cx*uf , cy*uf , rotate)
                                    ,rotateXY( (cx+20)*uf , (cy+40)*uf  , cx*uf , cy*uf , rotate)
                                    ,rotateXY( (cx-20)*uf , (cy+40)*uf  , cx*uf , cy*uf , rotate)
                                    ]
                                   , dxfattribs={'layer': 'outline'}
                                   )
  shape.close(True)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Side40x40 (ctx , cx , cy, rotate):   # center of holes
  uf    = ctx['unit_factor']
  hole  =   5.2

  EnsureLayer(ctx , 'th52' , 'through hole 5.2mm (M5 screw)')

  for xi in range(0,4):
    for yi in [-10,10]:
      ctx['msp'].add_circle(rotateXY((cx+30-xi*20)*uf , (cy+yi)*uf, cx*uf , cy*uf , rotate) , hole/2*uf, dxfattribs={'layer': 'th52'})

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def MGN12H(ctx , cx , cy , rotate , counterbore_depth):
  uf     = ctx['unit_factor']
  width  =  20
  height =  20
  hole   =   3.2

  holes = [rotateXY(cx - width/2 , cy - height/2, cx , cy , rotate)
          ,rotateXY(cx - width/2 , cy + height/2, cx , cy , rotate)
          ,rotateXY(cx + width/2 , cy - height/2, cx , cy , rotate)
          ,rotateXY(cx + width/2 , cy + height/2, cx , cy , rotate)
          ]

  EnsureLayer(ctx , 'th32' , 'through hole 3.2mm (M3 screw)')


  # mouting holes
  for (x,y) in holes:
    ctx['msp'].add_circle((x*uf , y*uf) , hole/2*uf , dxfattribs={'layer': 'th32'})

  width  = 45.4
  height = 27

  # add outline
  shape = ctx['msp'].add_lwpolyline([rotateXY((cx - width/2)*uf , (cy - height/2)*uf , cx*uf , cy*uf , rotate)
                                    ,rotateXY((cx + width/2)*uf , (cy - height/2)*uf , cx*uf , cy*uf , rotate)
                                    ,rotateXY((cx + width/2)*uf , (cy + height/2)*uf , cx*uf , cy*uf , rotate)
                                    ,rotateXY((cx - width/2)*uf , (cy + height/2)*uf , cx*uf , cy*uf , rotate)
                                    ]
                                   , dxfattribs={'layer': 'outline'}
                                   )
  shape.close(True)

  # mark center
  ctx['msp'].add_point((cx*uf , cy*uf) , dxfattribs={'layer': 'outline'})


  if (counterbore_depth > 0):
    hole2 = 8   # counter bore

    ln = 'cb%dx%d'                           % (hole2 , counterbore_depth)
    ld = 'counter bore %3.1fmm %3.1fmm deep' % (hole2 , counterbore_depth)

    EnsureLayer(ctx , ln , ld)

    for (x,y) in holes:
      ctx['msp'].add_circle((x*uf  , y*uf) , hole2/2*uf , dxfattribs={'layer' : ln})

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def SFU1605_holder(ctx , cx , cy , rotate):
  uf     = ctx['unit_factor']
  width  =  24
  height =  40
  ow     =  40
  oh     =  52

  hole   = 5.2

  EnsureLayer(ctx , 'th52' , 'through hole 5.2mm (M5 screw)')

  # mounting holes
  for (x,y) in [rotateXY(cx - width/2 , cy - height/2, cx , cy , rotate)
               ,rotateXY(cx - width/2 , cy + height/2, cx , cy , rotate)
               ,rotateXY(cx + width/2 , cy - height/2, cx , cy , rotate)
               ,rotateXY(cx + width/2 , cy + height/2, cx , cy , rotate)
               ]:
    ctx['msp'].add_circle((x*uf , y*uf) , hole/2*uf, dxfattribs={'layer': 'th52'})


  # add outline
  shape = ctx['msp'].add_lwpolyline([rotateXY((cx - ow/2)*uf , (cy - oh/2)*uf , cx*uf , cy*uf , rotate)
                                    ,rotateXY((cx + ow/2)*uf , (cy - oh/2)*uf , cx*uf , cy*uf , rotate)
                                    ,rotateXY((cx + ow/2)*uf , (cy + oh/2)*uf , cx*uf , cy*uf , rotate)
                                    ,rotateXY((cx - ow/2)*uf , (cy + oh/2)*uf , cx*uf , cy*uf , rotate)
                                    ]
                                   , dxfattribs={'layer': 'outline'}
                                   )
  shape.close(True)

  # mark center
  ctx['msp'].add_point((cx*uf , cy*uf) , dxfattribs={'layer': 'outline'})

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Face40x60 (ctx , cx , cy , rotate , counterbore_depth):   # center of profile
  uf   = ctx['unit_factor']
  hole = 5.2

  holes =  [rotateXY(cx - 20 , cy + 10 , cx , cy , rotate)
           ,rotateXY(cx - 20 , cy - 10 , cx , cy , rotate)
           ,rotateXY(cx      , cy + 10 , cx , cy , rotate)
           ,rotateXY(cx      , cy - 10 , cx , cy , rotate)
           ,rotateXY(cx + 20 , cy + 10 , cx , cy , rotate)
           ,rotateXY(cx + 20 , cy - 10 , cx , cy , rotate)
           ]

  EnsureLayer(ctx , 'th52' , 'through hole 5.2mm (M5 screw)')

  for (x,y) in holes:
    ctx['msp'].add_circle((x*uf , y*uf) , hole/2*uf , dxfattribs={'layer': 'th52'})


  # add outline
  shape = ctx['msp'].add_lwpolyline([rotateXY((cx-30)*uf , (cy-20)*uf , cx*uf , cy*uf , rotate)
                                    ,rotateXY((cx+30)*uf , (cy-20)*uf , cx*uf , cy*uf , rotate)
                                    ,rotateXY((cx+30)*uf , (cy+20)*uf , cx*uf , cy*uf , rotate)
                                    ,rotateXY((cx-30)*uf , (cy+20)*uf , cx*uf , cy*uf , rotate)
                                    ]
                                   , dxfattribs={'layer': 'outline'}
                                   )

  shape.close(True)

  # mark center
  ctx['msp'].add_point((cx*uf , cy*uf) , dxfattribs={'layer': 'outline'})



  if (counterbore_depth > 0):
    hole2  =   9   # counter bore

    ln = 'cb%dx%d'                           % (hole2 , counterbore_depth)
    ld = 'counter bore %3.1fmm %3.1fmm deep' % (hole2 , counterbore_depth)

    EnsureLayer(ctx , ln , ld)

    for (x,y) in holes:
      ctx['msp'].add_circle((x*uf  , y*uf) , hole2/2*uf , dxfattribs={'layer' : ln})

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

