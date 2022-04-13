import math
from cfg        import *
from common     import *

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def PortalBlockConnect (ctx , plate_variant , cx , cy , cb_depth):   # center of ballscrew
  hole = 6.2

  if (plate_variant == 'right'):
    mx = -1
  else:
    mx = 1

  EnsureLayer(ctx , 'th62' , 'through hole 6.2mm (M6 screw)')

  holes = [( 9.5  * mx,  35)
          ,( 9.5  * mx, -35)
          ,(-35.5 * mx,  35)
          ,(-35.5 * mx, -35)
          ]

  for x,y in holes:
    ctx['msp'].add_circle((x + cx*mx , cy + y) , hole/2 , dxfattribs={'layer' : 'th62'})

  if (cb_depth > 0):
    hole2 = 11   # counter bore

    ln = 'cb%dx%d'                                     % (hole2 , cb_depth)
    ld = 'counter bore %3.1fmm diameter, %3.1fmm deep' % (hole2 , cb_depth)

    EnsureLayer(ctx , ln , ld)

    for (x,y) in holes:
      ctx['msp'].add_circle((x + cx*mx , cy + y) , hole2/2 , dxfattribs={'layer' : ln})

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def PortalAddOn (ctx , plate_variant):
  hole = 6.8
  # purpose is to mount the foot of a measuring stand that holds a dial indicator the measure and adjust alignment

  if (plate_variant == 'left'):
    mx = 1
  else:
    mx = -1

  EnsureLayer(ctx , 'th68' , 'through hole 6.8mm (M8 thread)')

  for (x,y) in [[37 + 1*70.59 , 94.7514]
              #,[37 + 2*70.59 , 94.7514]
              #,[37           , 94.7514]
               ]:
    ctx['msp'].add_circle((x * mx , y) , hole/2 , dxfattribs={'layer' : 'th68'})

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Portal_Plate(ctx , plate_group , plate_name , plate_variant):
  result = {}

  if (plate_variant==''):
    plate_id = '%s-%s'    % (plate_group,plate_name)
  else:
    plate_id = '%s-%s-%s' % (plate_group,plate_name,plate_variant)

  if (plate_variant == 'left' or plate_variant == ""):
    # normal direction
    mx      = 1
  elif (plate_variant == 'right'):
    # mirrored in x-direction
    mx      = -1
  else:
    print("ERROR: don't know how to draw Portal_plate(%s,%s)" % (plate_name , plate_variant))
    exit(1)

  cr    = 5                     # corner radius
  dbr   = 2.0                   # dog-bone radius => 4mm tool diameter
  cb90  = 0.4142135 *mx         # corner bulge = tan(22.5°) for 90° corners
  dbo90 = math.sqrt(2) * dbr    # dog-bone offset for 90° inner corners
  dbb   = -mx                   # dogbone bulge


  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  if (plate_name == 'back'):
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
    shape = ctx['msp'].add_lwpolyline([( x[0] , y[0])
                                      ,( x[6] , y[0])
                                      ,( x[6] , y[5])
                                      ,( x[0] , y[5])
                                      ]
                                     , format='xy'
                                     )
    shape.close(True)

    # array of holes...
    EnsureLayer(ctx , 'th52' , 'through hole 5.2mm (M5 screw)')

    for xi in range(1,6):
      for yi in range(1,5):
        ctx['msp'].add_circle((x[xi] , y[yi]) , hole_diameter/2 , dxfattribs={'layer' : 'th52'})

    screw = Screw('M5' , cfg['Plates'][plate_group][plate_name]['thickness']
                       + 6   # thru sliding nut
                 )
    doc = '%s to portal' % (plate_id)
    Add2BOM(ctx , 5*4 , 'DIN912' , screw    , doc)    # screw
    Add2BOM(ctx , 5*4 , 'DIN125' , 'M5'     , doc)    # washer

    result['plateWH'] = [width , height]
    result['textXY' ] = [    0 , height]
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  elif (plate_name == 'side'):
    if (plate_variant == 'left'):
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
    shape = ctx['msp'].add_lwpolyline([( (x0+cr      )*mx , y3         , 0       )   #  1
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
    MGN12H         (ctx ,  27   *mx ,  56      , 0   , cfg['Plates'][plate_group]['side']['thickness']-10)
    MGN12H         (ctx , 188.18*mx ,  56      , 0   , cfg['Plates'][plate_group]['side']['thickness']-10)

    screw = Screw('M3' , 10    # if side is thicker it's counter bored to be effectively 10
                       + 5     # into MGN12H
                 )
    doc = '%s to Y-MGN12H' % (plate_id)
    Add2BOM(ctx , 2*4, 'DIN912'      , screw   , doc)  # screw
    Add2BOM(ctx , 2*4, 'DIN125'      , 'M3'    , doc)  # washer



    SFU1605_holder (ctx , 107.59*mx ,  26      , 0)

    l = cfg['Plates'][plate_group][plate_name]['thickness']

    if (l < 15):
      l = 15  # padded with spacer to be effectively 15 (baseline design)

    screw = Screw('M5' , l
                       + 5   # thread depth in nut holder
                 )
    doc = '%s to Y-1605 nut holder' % (plate_id)
    Add2BOM(ctx , 4 , 'ISO7380' , screw , doc)    # screw
    Add2BOM(ctx , 4 , 'DIN125' , 'M5'   , doc)    # washer



    Face40x60      (ctx ,  35   *mx , 126.059  , 0 , cfg['Plates'][plate_group]['side']['thickness']-10)
    Face40x60      (ctx ,  35   *mx , 251.059  , 0 , cfg['Plates'][plate_group]['side']['thickness']-10)

    screw = Screw('M5' , 10   # if side is thicker it's counter bored to be effectively 10
                       + 15   # thread depth in extrusion
                 )
    doc = '%s to portalX-extrusion' % (plate_id)
    Add2BOM(ctx , 2*6 , 'DIN912' , screw , doc)    # screw
    Add2BOM(ctx , 2*6 , 'DIN125' , 'M5'  , doc)    # washer needed?

    if (plate_variant == 'left'):
      BF12_face         (ctx ,  48       , 188.5590 , -90)

      screw = Screw('M5' , 10   # if side is thicker it's counter bored to be effectively 10
                         + 20   # BF12 support block
                         + 10   # locknut + safety threads
                   )
      doc = 'X-BF12 to %s' % (plate_id)

      Add2BOM(ctx , 4, 'DIN912' , screw   , doc)  # screw
      Add2BOM(ctx , 8, 'DIN125' , 'M5'    , doc)  # washer
      Add2BOM(ctx , 4, 'DIN985' , 'M5'    , doc)  # locknut
    else:
      NEMA23            (ctx , -48       , 188.559  ,   0)
      screw = Screw('M5' , 6    # motor mount + washer
                         + cfg['Plates'][plate_group][plate_name    ]['thickness']
                         + cfg['Plates'][plate_group]['motor_spacer']['thickness']
                         + 10   # locknut + safety threads
                   )

      doc = 'X-NEMA23 to %s' % (plate_id)
      Add2BOM(ctx , 4, 'DIN912' , screw   , doc)  # screw
      Add2BOM(ctx , 8, 'DIN125' , 'M5'    , doc)  # washer
      Add2BOM(ctx , 4, 'DIN985' , 'M5'    , doc)  # locknut





      cb_depth = cfg['Plates'][plate_group]['side']['thickness']-10

      if (cb_depth == 5):
        cb_depth += 1   # my addition that the whole screwhead disappers

      PortalBlockConnect(ctx , plate_variant ,  48  , 188.559 , cb_depth)

      screw = Screw('M6' , cfg['Plates'][plate_group]['side']['thickness'] - cb_depth
                         + 10   # thread length inside steel socket
                   )
      doc = 'steel socket to %s' % (plate_id)
      Add2BOM(ctx , 4, 'DIN912'      , screw    , doc)  # screw
      Add2BOM(ctx , 4, 'DIN125'      , 'M6'     , doc)  # washer
      Add2BOM(ctx , 4, 'SteelSocket' , 'M6x30'  , doc)  # socket




    PortalAddOn(ctx , plate_variant)

    result['plateWH'] = [x5 - x0 , y5 - y0]

    if (plate_variant == 'left'):
      result['textXY' ] = [   40 , y5]
    else:
      result['textXY' ] = [ -160 , y5]

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  elif (plate_name == 'motor_spacer'):
    # x/y values under the assumption that the center of ballscrew/motor-axis is at (0,0)
    (x0 , x1) = [-28.5 , 28.5]
    (y0 , y1) = [-28.5 , 28.5]

    # outer shape...
    shape = ctx['msp'].add_lwpolyline([( (x0+cr   )*mx , y0       , 0   )   #  1
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
    NEMA23(ctx  ,   0    ,   0  , 0)

    result['plateWH'] = [x1-x0 , y1-y0]
    result['textXY' ] = [    0 ,    y1]

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  elif (plate_name == 'nut_spacer'
        or
        plate_name == 'side_plate_spacer'):
    hole = 5.2
    cr   = 1

    # x/y values
    (x0 , x1) = [-20 , 20]
    (y0 , y1) = [-26 , 26]

    # outer shape...
    shape = ctx['msp'].add_lwpolyline([( (x0+cr   )*mx , y0       , 0   )   #  1
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

    SFU1605_holder(ctx , 0 , 0 , 0)
    # BOM with ZAxis...

    result['plateWH'] = [x1-x0 , y1-y0]
    result['textXY' ] = [    0 ,    y1]

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

  elif (plate_name == 'block'):
    # x/y values under the assumption that the center of ballscrew/motor-axis is at (0,0)
    (x0 , x1 , x2     ) = [-17   ,  17.2 , 43  ]
    (y0 , y1 , y2 , y3) = [-42.5 , -17.2 , 17.2 , 42.5]

    mx=-1 # mirror to get the facets on the side towards inside

    # outer shape...
    shape = ctx['msp'].add_lwpolyline([( (x0+cr   )*mx , y0       , 0      )   #  1
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
    PortalBlockConnect(ctx , plate_name ,  0    ,   0 , 0)
    screw = Screw('M6' , cfg['Plates'][plate_group][plate_name]['thickness']
                       + 10   # thread length inside steel socket
                 )
    doc = '%s to steel socket' % (plate_id)
    Add2BOM(ctx , 4, 'DIN912'      , screw   , doc)  # screw
    Add2BOM(ctx , 4, 'DIN125'      , 'M6'    , doc)  # washer




    BK12_face         (ctx        ,  0    ,   0  , 270)
    screw = Screw('M5' , 25   # BK12 block
                       + cfg['Plates'][plate_group][plate_name]['thickness']
                       + 10   # locknut + safety threads
                 )
    doc = 'X-BK12 to %s' % (plate_id)
    Add2BOM(ctx , 4, 'DIN912'      , screw   , doc)  # screw
    Add2BOM(ctx , 8, 'DIN125'      , 'M5'    , doc)  # washer
    Add2BOM(ctx , 4, 'DIN985'      , 'M5'    , doc)  # locknut


    result['plateWH'] = [x2-x0 , y3-y0]
    result['textXY' ] = [    0 ,    y3]

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  else:
    print("ERROR: don't know how to draw Portal_Plate(%s,%s)" % (p_name , plate_name))
    exit(1)
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


  return result



