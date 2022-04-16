import ezdxf
from ezdxf      import units
from datetime   import datetime
from cfg        import *
from common     import *

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Spindle_adapter_connect(ctx , plate_name):
  if (plate_name == 'front'):
    # on spindle plate we need an M6 threaded hole
    hole = 5.0
    EnsureLayer  (ctx , 'th50' , 'through hole 5.0mm (M6 thread)')
    layer = 'th50'
  elif (plate_name == 'spindle_adapter'):
    # on spindle adapter we need an M6 thru-hole
    hole = 6.2
    EnsureLayer  (ctx , 'th62' , 'through hole 6.2mm (M6 screw)')
    layer = 'th62'
  else:
    print("unknown context '%s' for Spindle_adapter_connect" % plate_name)
    exit(1)

  # we need holes to mount the spindle_adapter to spindle_plate
  holesY = [118
           , 80
           , 42
           ]
  for y in holesY:
    ctx['msp'].add_circle(( -49 , y) ,   hole/2, dxfattribs={'layer' : layer})
    ctx['msp'].add_circle((  49 , y) ,   hole/2, dxfattribs={'layer' : layer})

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def SpindleAddOn(ctx , width):
  hole = 6.8

  EnsureLayer  (ctx , 'th68' , 'through hole 6.8mm (M8 thread)')

  # purpose: mount dial indicator for aligning geometry
  ctx['msp'].add_circle(( -width/2 + 13.5 , 80) ,   hole/2, dxfattribs={'layer' : 'th68'})
  ctx['msp'].add_circle(( +width/2 - 13.5 , 80) ,   hole/2, dxfattribs={'layer' : 'th68'})

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def SpindleAdapter(plate_name):
  hole = 6.8

  # on spindle plate we need holes for M6 threads (=5mm)
  # on adapter plate we need holes for M6 screws  (=6.4mm)



  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def ZAxisBackAddOn(ctx , cx , cy):
  hole = 6.8

  EnsureLayer(ctx , 'th68' , 'through hole 6.8mm (M8 thread)')

  # purpose: mount for dial indicator
  ctx['msp'].add_circle(( cx , cy) ,   hole/2, dxfattribs={'layer': 'th68'})
  ctx['msp'].add_circle((-cx , cy) ,   hole/2, dxfattribs={'layer': 'th68'})

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def RailMount(ctx , x , y1 , y2 , y3 , y4):
  hole = 5.2

  EnsureLayer(ctx , 'th52' , 'through hole 5.2mm (M5 screw)')

  for (x,y) in [[x , y1]
               ,[x , y2]
               ,[x , y3]
               ,[x , y4]
               ]:
    ctx['msp'].add_circle(( x , y) , hole/2, dxfattribs={'layer': 'th52'})
    ctx['msp'].add_circle((-x , y) , hole/2, dxfattribs={'layer': 'th52'})

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def ZAxis_Plate(ctx , plate_group , plate_name , plate_variant):
  cr    = 5                     # corner radius
  dbr   = 2.0                   # dog-bone radius => 3mm tool diameter
  cb90  = 0.4142135             # corner bulge = tan(22.5°) for 90° corners
  dbo90 = math.sqrt(2) * dbr    # dog-bone offset for 90° inner corners
  dbb   = 1                     # dogbone bulge

  result = {}

  if (plate_variant==''):
    plate_id = '%s-%s'    % (plate_group,plate_name)
  else:
    plate_id = '%s-%s-%s' % (plate_group,plate_name,plate_variant)





  if (plate_name == 'bottom'):
    # x/y values under the assumption that the center of ballscrew/motor-axis is at (0,0)
    xadj = 10 - cfg['Plates'][plate_group]['back']['thickness']

    (x1,x2,x3,x4      ) = [ -43+xadj  ,  -32.15+xadj , -21.85 , 17]
    (y6,y5,y4,y3,y2,y1) = [ 80
                          , 59.85
                          , 10.15
                          ,-10.15
                          ,-59.85
                          ,-80
                          ]

    # draw outer shape...
    shape = ctx['msp'].add_lwpolyline([( x1+cr    , y1       , 0   ) #  1
                                      ,( x2       , y1       , 0   ) #  2
                                      ,( x2       , y2-dbo90 ,-dbb ) #  3
                                      ,( x2+dbo90 , y2       , 0   ) #  4
                                      ,( x3-dbo90 , y2       ,-dbb ) #  5
                                      ,( x3       , y2-dbo90 , 0   ) #  6
                                      ,( x3       , y1       , 0   ) #  7
                                      ,( x4-cr    , y1       , cb90) #  8
                                      ,( x4       , y1+cr    , 0   ) #  9
                                      ,( x4       , y6-cr    , cb90) # 10
                                      ,( x4-cr    , y6       , 0   ) # 11
                                      ,( x3       , y6       , 0   ) # 12
                                      ,( x3       , y5+dbo90 ,-dbb ) # 13
                                      ,( x3-dbo90 , y5       , 0   ) # 14
                                      ,( x2+dbo90 , y5       ,-dbb ) # 15
                                      ,( x2       , y5+dbo90 , 0   ) # 16
                                      ,( x2       , y6       , 0   ) # 17
                                      ,( x1+cr    , y6       , cb90) # 18
                                      ,( x1       , y6-cr    , 0   ) # 19
                                      ,( x1       , y1+cr    , cb90) # 20
                                      ]
                                     , format='xyb'
                                     )
    shape.close(True)

    # draw inner shape...
    shape = ctx['msp'].add_lwpolyline([( x2+dbo90 , y3       , 0   ) #  1
                                      ,( x3-dbo90 , y3       , dbb ) #  2
                                      ,( x3       , y3+dbo90 , 0   ) #  3
                                      ,( x3       , y4-dbo90 , dbb ) #  4
                                      ,( x3-dbo90 , y4       , 0   ) #  5
                                      ,( x2+dbo90 , y4       , dbb ) #  6
                                      ,( x2       , y4-dbo90 , 0   ) #  7
                                      ,( x2       , y3+dbo90 , dbb ) #  8
                                      ]
                                     , format='xyb'
                                     )
    shape.close(True)







    # add other elements...
    EnsureLayer(ctx , 'thx' , 'through hole 22.5mm')

    ctx['msp'].add_circle((0 , 0) , 22.5/2, dxfattribs={'layer' : 'thx'})
    #BF10_face(msp , 0 , 0 , -90) # BF10 mounted to back instead of bottom!

    EnsureLayer(ctx , 'th52' , 'through hole 5.2mm (M5 screw)')

    for (x,y) in ((-5 ,  66.5)
                 ,(-5 , -66.5)
                 ):
      ctx['msp'].add_circle((x , y) , 5.2/2, dxfattribs={'layer' : 'th52'})

    screw = Screw('M5' , cfg['Plates'][plate_group][plate_name]['thickness']
                       + 15   # thread inside Z-extrusion
                 )
    doc = '%s to Z-extrusion' % (plate_id)
    Add2BOM(ctx , 2, 'DIN912' , screw   , doc)  # screw
    Add2BOM(ctx , 2, 'DIN125' , 'M5'    , doc)  # washer




    EnsureLayer(ctx , 'th68' , 'through hole 6.8mm (M8 thread)')

    for (x,y) in ((x1+32.75 ,  44.75)
                 ,(x1+32.75 , -44.75)
                 ):
      ctx['msp'].add_circle((x ,y) , 6.8/2, dxfattribs={'layer' : 'th68'})



    result['plateWH'] = [(x4 - x1)     , (y6-y1)]
    result['textXY' ] = [(x4 + x1) / 2 ,  y6    ]
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  elif (plate_name == 'top'):
    # x/y values under the assumption that the center of ballscrew/motor-axis is at (0,0)
    xadj = 10 - cfg['Plates'][plate_group]['back']['thickness']

    (x1,x2,x3,x4,x5         ) = [ -33.5 , -17    ,  21.85 ,  32.15-xadj , 46.5-xadj                    ]
    (y8,y7,y6,y5,y4,y3,y2,y1) = [ 80
                                , 59.85
                                , 33.5
                                , 10.15
                                ,-10.15
                                ,-33.5
                                ,-59.85
                                ,-80
                                ]

    # draw outer shape...
    shape = ctx['msp'].add_lwpolyline([( x1+10    , y3       , 0   ) #  1
                                      ,( x2-cr    , y3       ,-cb90) #  2
                                      ,( x2       , y3-cr    , 0   ) #  3
                                      ,( x2       , y1+cr    , cb90) #  4
                                      ,( x2+cr    , y1       , 0   ) #  5
                                      ,( x3       , y1       , 0   ) #  6
                                      ,( x3       , y2-dbo90 ,-dbb ) #  7
                                      ,( x3+dbo90 , y2       , 0   ) #  8
                                      ,( x4-dbo90 , y2       ,-dbb ) #  9
                                      ,( x4       , y2-dbo90 , 0   ) # 10
                                      ,( x4       , y1       , 0   ) # 11
                                      ,( x5-cr    , y1       , cb90) # 12
                                      ,( x5       , y1+cr    , 0   ) # 13
                                      ,( x5       , y8-cr    , cb90) # 14
                                      ,( x5-cr    , y8       , 0   ) # 15
                                      ,( x4       , y8       , 0   ) # 16
                                      ,( x4       , y7+dbo90 ,-dbb ) # 17
                                      ,( x4-dbo90 , y7       , 0   ) # 18
                                      ,( x3+dbo90 , y7       ,-dbb ) # 19
                                      ,( x3       , y7+dbo90 , 0   ) # 20
                                      ,( x3       , y8       , 0   ) # 21
                                      ,( x2+cr    , y8       , cb90) # 22
                                      ,( x2       , y8-cr    , 0   ) # 23
                                      ,( x2       , y6+cr    ,-cb90) # 24
                                      ,( x2-cr    , y6       , 0   ) # 25
                                      ,( x1+10    , y6       , cb90) # 26
                                      ,( x1       , y6-10    , 0   ) # 27
                                      ,( x1       , y3+10    , cb90) # 28
                                      ]
                                     , format='xyb'
                                     )
    shape.close(True)

    # draw inner shape...
    shape = ctx['msp'].add_lwpolyline([( x3+dbo90 , y4       , 0   ) #  1
                                      ,( x4-dbo90 , y4       , dbb ) #  2
                                      ,( x4       , y4+dbo90 , 0   ) #  3
                                      ,( x4       , y5-dbo90 , dbb ) #  4
                                      ,( x4-dbo90 , y5       , 0   ) #  5
                                      ,( x3+dbo90 , y5       , dbb ) #  6
                                      ,( x3       , y5-dbo90 , 0   ) #  7
                                      ,( x3       , y4+dbo90 , dbb ) #  8
                                      ]
                                     , format='xyb'
                                     )
    shape.close(True)


    # add other elements...
    NEMA23(ctx , 0 , 0 , 0)

    EnsureLayer(ctx , 'th52' , 'through hole 5.2mm (M5 screw)')

    for (x,y) in ((5 ,  66.5)
                 ,(5 , -66.5)
                 ):
      ctx['msp'].add_circle((x,y) , 5.2/2, dxfattribs={'layer': 'th52'})

    screw = Screw('M5' , 6    # motor mount + washer
                       + cfg['Plates'][plate_group][plate_name]['thickness']
                       + 10   # locknut + safety threads
                 )
    doc = 'Z-NEMA23 to %s' % (plate_id)
    Add2BOM(ctx , 4, 'DIN912' , screw   , doc)  # screw
    Add2BOM(ctx , 8, 'DIN125' , 'M5'    , doc)  # washer
    Add2BOM(ctx , 4, 'DIN985' , 'M5'    , doc)  # locknut


    screw = Screw('M5' , cfg['Plates'][plate_group][plate_name]['thickness']
                       + 15   # thread inside Z-extrusion
                 )
    doc = '%s to Z-extrusion' % (plate_id)
    Add2BOM(ctx , 2, 'DIN912' , screw   , doc)  # screw
    Add2BOM(ctx , 2, 'DIN125' , 'M5'    , doc)  # washer




    EnsureLayer(ctx , 'th32' , 'through hole 3.2mm (M3 screw)')

    for (x,y) in ((39.32-xadj ,  34.96*2)
                 ,(39.32-xadj ,  34.96*1)
                 ,(39.32-xadj ,  34.96*0)
                 ,(39.32-xadj , -34.96*1)
                 ,(39.32-xadj , -34.96*2)
                 ):
      ctx['msp'].add_circle((x,y) , 3.2/2 , dxfattribs={'layer': 'th32'})

    result['plateWH'] = [(x5 - x1)     , (y8-y1)]
    result['textXY' ] = [(x5 + x1) / 2 ,  y8    ]
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  elif (plate_name == 'front'):
    # free parameters
    width          = 160     #  width of plate
    height         = 140     # height of plate

    width2         =  94     # bottom nose width
    height2        =  20     # bottom nose height

    ZRail_xdist    = 133

    ZBlock_y1      = 118     # might be calculated with offset from plate boundaries
    ZBlock_y2      =  42     # might be calculated with offset from plate boundaries
    ZNut_y         =  80     # how is value calculated?

    cr    = 2.5                   # corner radius
    cb90  = 0.4142135             # corner bulge = tan(22.5°) for 90° corners

    # outer shape of ZAxis-Spindle-Plate
    x0 = -width  / 2    # leftmost X
    x1 = -width2 / 2
    x2 =  width2 / 2
    x3 =  width  / 2    # rightmost X

    y0 =           0    # bottom Y
    y1 =  height2
    y2 =  height        # top Y

    shape = ctx['msp'].add_lwpolyline([( (x1+5    ) , y0       , 0   )  #  0
                                      ,( (x2-5    ) , y0       , cb90)  #  1
                                      ,( (x2      ) , y0+5     , 0   )  #  2
                                      ,( (x2      ) , y1-5     ,-cb90)  #  3
                                      ,( (x2+5    ) , y1       , 0   )  #  4
                                      ,( (x3-cr   ) , y1       , cb90)  #  5
                                      ,( (x3      ) , y1+cr    , 0   )  #  6
                                      ,( (x3      ) , y2-cr    , cb90)  #  7
                                      ,( (x3-cr   ) , y2       , 0   )  #  8
                                      ,( (x0+cr   ) , y2       , cb90)  #  9
                                      ,( (x0      ) , y2-cr    , 0   )  # 10
                                      ,( (x0      ) , y1+cr    , cb90)  # 11
                                      ,( (x0+cr   ) , y1       , 0   )  # 12
                                      ,( (x1-5    ) , y1       ,-cb90)  # 13
                                      ,( (x1      ) , y1-5     , 0   )  # 14
                                      ,( (x1      ) , y0+5     , cb90)  # 15
                                      ]
                                     , format='xyb'
                                     )
    shape.close(True)

    # Assemble parts
    MGN12H(ctx , -ZRail_xdist/2 , ZBlock_y1 , 90   , 5)
    MGN12H(ctx , -ZRail_xdist/2 , ZBlock_y2 , 90   , 5)
    MGN12H(ctx ,  ZRail_xdist/2 , ZBlock_y1 , 90   , 5)
    MGN12H(ctx ,  ZRail_xdist/2 , ZBlock_y2 , 90   , 5)

    if (plate_variant == ''):
      screw = Screw('M3' , cfg['Plates'][plate_group][plate_name]['thickness']
                         - 5     # counter bored
                         + 5     # into MGN12H
                   )
      doc = '%s to Z-MGN12H' % (plate_id)
      Add2BOM(ctx , 4*4, 'DIN912'      , screw   , doc)  # screw
      Add2BOM(ctx , 4*4, 'DIN125'      , 'M3'    , doc)  # washer





      SFU1204_nutholder(ctx , 0 , ZNut_y , 90, 'front')
      screw = Screw('M5' , cfg['Plates'][plate_group][plate_name            ]['thickness']
                         - 5     # counter bored
                         + cfg['Plates'][plate_group]['spindle_plate_spacer']['thickness']
                         + 5     # into nut holder
                   )
      doc = '%s to Z-1204 nutholder' % (plate_id)
      Add2BOM(ctx , 4, 'DIN912'      , screw   , doc)  # screw
      Add2BOM(ctx , 4, 'DIN125'      , 'M5'    , doc)  # washer





    SpindleAddOn(ctx, width)

    # dowel pin between spindle plate and spindle adapter
    EnsureLayer(ctx , 'cb3x5' , 'counter bore 3mm diameter, 5mm deep (dowel pin)')

    ctx['msp'].add_circle(( 0 , ZNut_y) ,   3/2, dxfattribs={'layer': 'cb3x5'})

    if (plate_variant == ''):
      Add2BOM(ctx , 1, 'dowel pin'      , '3x10'    , 'dowel pin')  # dowel pin


    if (plate_variant == ''):
      # we need holes to mount the spindle adapter
      # we need a hole for a dowel pin (passstift) between spindle plate and adapter plate
      Spindle_adapter_connect(ctx , plate_name)
      screw = Screw('M6' , cfg['Plates'][plate_group][plate_name]['thickness']
                         + 10     # thread into spindle-plate
                   )
      doc = 'spindle_adapter to %s' % (plate_id)
      Add2BOM(ctx , 6, 'DIN912'      , screw   , doc)  # screw
      Add2BOM(ctx , 6, 'DIN125'      , 'M6'    , doc)  # washer


    #else:
    #  file_name_add = Spindle_outline(ctx , p_variant)

    result['plateWH'] = [width , height]
    result['textXY' ] = [   -60 ,    140]

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  elif (plate_name == 'spindle_adapter'):
    # free parameters
    width          = 112     #  width of plate
    height         = 140     # height of plate

    width2         =  94     # bottom nose width
    height2        =  20     # bottom nose height

    cr    = 2.5                   # corner radius
    cb90  = 0.4142135             # corner bulge = tan(22.5°) for 90° corners

    # outer shape of ZAxis-Spindle-Plate
    x0 = -width  / 2    # leftmost X
    x1 = -width2 / 2
    x2 =  width2 / 2
    x3 =  width  / 2    # rightmost X

    y0 =           0    # bottom Y
    y1 =  height2
    y2 =  height        # top Y

    shape = ctx['msp'].add_lwpolyline([( (x1+5    ) , y0       , 0   )
                                      ,( (x2-5    ) , y0       , cb90)
                                      ,( (x2      ) , y0+5     , 0   )
                                      ,( (x2      ) , y1-5     ,-cb90)
                                      ,( (x2+5    ) , y1       , 0   )
                                      ,( (x3-cr   ) , y1       , cb90)
                                      ,( (x3      ) , y1+cr    , 0   )
                                      ,( (x3      ) , y2-cr    , cb90)
                                      ,( (x3-cr   ) , y2       , 0   )
                                      ,( (x0+cr   ) , y2       , cb90)
                                      ,( (x0      ) , y2-cr    , 0   )
                                      ,( (x0      ) , y1+cr    , cb90)
                                      ,( (x0+cr   ) , y1       , 0   )
                                      ,( (x1-5    ) , y1       ,-cb90)
                                      ,( (x1      ) , y1-5     , 0   )
                                      ,( (x1      ) , y0+5     , cb90)
                                      ]
                                     , format='xyb'
                                     )
    shape.close(True)

    # Assemble parts
    Spindle_adapter_connect(ctx , plate_name)


    # # bottom/top markers of baseline spindle
    # ctx['msp'].add_lwpolyline([(-90 , -67.5 ) , (90 , -67.5 )] , dxfattribs={'layer': 'outline'})
    # ctx['msp'].add_lwpolyline([(-90 , 171.44) , (90 , 171.44)] , dxfattribs={'layer': 'outline'})


    # holes to mount spindle to spindle adapter (mirrored at Y-axis because we need counterbores on the back)
    #holesY = [40.5 + 90
    #         ,40.5
    #         ]
    #
    #holesX = [-41+25.5
    #         , 41-26.5
    #         ]
    #for y in holesY:
    #  for x in holesX:
    #    msp.add_circle(( x , y) ,   5.2/2)




    # we need a hole for a dowel pin (passstift) between spindle plate and adapter plate



    result['plateWH'] = [width , height]
    result['textXY' ] = [  -60 ,    140]

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

  elif (plate_name == 'back'):
    margin = 0.5
    # x/y values
    (x1,x2,x3,x4,x5,x6,x7,x8,x9,x10) = [-80 , -60 , -28.57 , -18.57 , -10 , 10 , 18.57 , 28.57 , 60 , 80]

    # Y-adjust when top-plate is thicker than 10mm
    # the upper edge has to stay unchanged
    yadj = cfg['Plates'][plate_group]['top']['thickness'] - 10

    if (yadj < -10):
      print("ERROR: ZAxis-top-plate is too thick! (%dmm)" % (cfg['Plates'][plate_group]['top']['thickness']))
      print("       can't shift rail spacer further down")
      exit(1)


    y5  = 280    + yadj
    y4  = 279.5  + yadj
    y3  = 270
    y2  = 260
    y1  = 0.5
    y0  = 0
    ym1 = -cfg['Plates'][plate_group]['bottom']['thickness']

    # draw outer shape...
    shape = ctx['msp'].add_lwpolyline([( x1       , ym1      , 0   ) #  1
                                      ,( x2       , ym1      , 0   ) #  2
                                      ,( x2       , y1-dbo90 ,-dbb ) #  3
                                      ,( x2+dbo90 , y1       , 0   ) #  4
                                      ,( x5-dbo90 , y1       ,-dbb ) #  5
                                      ,( x5       , y1-dbo90 , 0   ) #  6
                                      ,( x5       , ym1      , 0   ) #  7
                                      ,( x6       , ym1      , 0   ) #  8
                                      ,( x6       , y1-dbo90 ,-dbb ) #  9
                                      ,( x6+dbo90 , y1       , 0   ) # 10
                                      ,( x9-dbo90 , y1       ,-dbb ) # 11
                                      ,( x9       , y1-dbo90 , 0   ) # 12
                                      ,( x9       , ym1      , 0   ) # 13
                                      ,( x10      , ym1      , 0   ) # 14
                                      ,( x10      , y5       , 0   ) # 15
                                      ,( x9       , y5       , 0   ) # 16
                                      ,( x9       , y3+dbo90 ,-dbb ) # 17
                                      ,( x9-dbo90 , y3       , 0   ) # 18
                                      ,( x8       , y3       , 0   ) # 19
                                      ,( x8       , y2+dbo90 ,-dbb ) # 20
                                      ,( x8-dbo90 , y2       , 0   ) # 21
                                      ,( x7+dbo90 , y2       ,-dbb ) # 22
                                      ,( x7       , y2+dbo90 , 0   ) # 23
                                      ,( x7       , y3       , 0   ) # 24
                                      ,( x6+dbo90 , y3       ,-dbb ) # 25
                                      ,( x6       , y3+dbo90 , 0   ) # 26
                                      ,( x6       , y4       , 0   ) # 27
                                      ,( x5       , y4       , 0   ) # 28
                                      ,( x5       , y3+dbo90 ,-dbb ) # 29
                                      ,( x5-dbo90 , y3       , 0   ) # 30
                                      ,( x4       , y3       , 0   ) # 31
                                      ,( x4       , y2+dbo90 ,-dbb ) # 32
                                      ,( x4-dbo90 , y2       , 0   ) # 33
                                      ,( x3+dbo90 , y2       ,-dbb ) # 34
                                      ,( x3       , y2+dbo90 , 0   ) # 35
                                      ,( x3       , y3       , 0   ) # 36
                                      ,( x2+dbo90 , y3       ,-dbb ) # 37
                                      ,( x2       , y3+dbo90 , 0   ) # 38
                                      ,( x2       , y5       , 0   ) # 39
                                      ,( x1       , y5       , 0   ) # 40
                                      ]
                                     , format='xyb'
                                     )
    shape.close(True)

    # add other elements...
    MGN12H(ctx , -58 ,  14  ,   0   , 0)
    MGN12H(ctx ,  58 ,  14  ,   0   , 0)
    MGN12H(ctx , -58 , 159  ,   0   , 0)
    MGN12H(ctx ,  58 , 159  ,   0   , 0)

    screw = Screw('M3' , cfg['Plates'][plate_group][plate_name]['thickness']
                       + 5     # into MGN12H
                 )
    doc = '%s X-MGN12H' % (plate_id)
    Add2BOM(ctx , 4*4, 'DIN912'      , screw   , doc)  # screw
    Add2BOM(ctx , 4*4, 'DIN125'      , 'M3'    , doc)  # washer







    # shifted BF10 a little up to avoid contact with bottom-plate
    BF10_footprint(ctx , 0 ,  10+margin  , 90)
    BK10_footprint(ctx , 0 , 212.75      , 90)

    screw = Screw('M6' , 30    # BK10/BF10
                       + 10    # thread into plate
                 )
    doc = 'Z-BF10 to %s' % (plate_id)
    Add2BOM(ctx , 2, 'DIN912'      , screw   , doc)  # screw
    Add2BOM(ctx , 2, 'DIN125'      , 'M6'    , doc)  # washer

    doc = 'Z-BK10 to %s' % (plate_id)
    Add2BOM(ctx , 4, 'DIN912'      , screw   , doc)  # screw
    Add2BOM(ctx , 4, 'DIN125'      , 'M6'    , doc)  # washer


    SFU1605_holder(ctx , 0 , 86.5 , 0)
    screw = Screw('M5' , cfg['Plates'][plate_group][plate_name]['thickness']
                       + cfg['Plates']['Portal']['nut_spacer' ]['thickness']
                       + 5     # into nut holder
                 )
    doc = '%s to X-1605 nutholder' % (plate_id)
    Add2BOM(ctx , 4, 'DIN912'      , screw   , doc)  # screw
    Add2BOM(ctx , 4, 'DIN125'      , 'M5'    , doc)  # washer


    ZAxisBackAddOn(ctx , 40 , 197.78)  # what is the purpose of this?

    # shifted upper spacer a little down to avoid contact with top-plate
    RailMount(ctx , 66.5 , 54 , 122.67 , 191.33-margin  , 260-margin)
    screw = Screw('M5' , cfg['Plates'][plate_group][plate_name   ]['thickness']
                       + cfg['Plates'][plate_group]['rail_spacer']['thickness']
                       + 6     # into sliding nut
                 )
    doc = 'Z-extrusion to %s' % (plate_id)
    Add2BOM(ctx , 4*2, 'DIN912'      , screw   , doc)  # screw
    Add2BOM(ctx , 4*2, 'DIN125'      , 'M5'    , doc)  # washer
    Add2BOM(ctx , 4*2, 'SlidingNut'  , 'M5'    , doc)  # sliding nut






    result['plateWH'] = [x10-x1 , y5-ym1]
    result['textXY' ] = [    0 ,  y5-ym1]

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

  elif (plate_name == 'rail_spacer'):
    d      = 68.67
    width  =   20
    height = d+20
    hole   = 5.2

    (x1,x2) = [-width /2 , width/2]
    (y2,y1) = [ height/2
              ,-height/2
              ]

    cr = 1

    # outer shape...
    shape = ctx['msp'].add_lwpolyline([( x1+cr , y1       , 0   )   #  1
                                      ,( x2-cr , y1       , cb90)   #  2
                                      ,( x2    , y1+cr    , 0   )   #  3
                                      ,( x2    , y2-cr    , cb90)   #  4
                                      ,( x2-cr , y2       , 0   )   #  5
                                      ,( x1+cr , y2       , cb90)   #  6
                                      ,( x1    , y2-cr    , 0   )   #  7
                                      ,( x1    , y1+cr    , cb90)   #  8
                                      ]
                                     , format='xyb'
                                     )
    shape.close(True)

    EnsureLayer(ctx , 'th52' , 'through hole 5.2mm (M5 screw)')

    ctx['msp'].add_circle((0 ,  d/2) , hole/2, dxfattribs={'layer': 'th52'})
    ctx['msp'].add_circle((0 , -d/2) , hole/2, dxfattribs={'layer': 'th52'})

    result['plateWH'] = [x2-x1 ,  y2-y1   ]
    result['textXY' ] = [    0 , (y2-y1)/2]

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

  elif (plate_name == 'motor_spacer'):
    # x/y values under the assumption that the center of ballscrew/motor-axis is at (0,0)
    (x0 , x1) = [-28.5 , 28.5]
    (y0 , y1) = [-28.5 , 28.5]

    # outer shape...
    shape = ctx['msp'].add_lwpolyline([( (x0+cr   ) , y0       , 0   )   #  1
                                      ,( (x1-cr   ) , y0       , cb90)   #  2
                                      ,( (x1      ) , y0+cr    , 0   )   #  3
                                      ,( (x1      ) , y1-cr    , cb90)   #  4
                                      ,( (x1-cr   ) , y1       , 0   )   #  5
                                      ,( (x0+cr   ) , y1       , cb90)   #  6
                                      ,( (x0      ) , y1-cr    , 0   )   #  7
                                      ,( (x0      ) , y0+cr    , cb90)   #  8
                                      ]
                                     , format='xyb'
                                     )
    shape.close(True)

    # add other elements...
    NEMA23(ctx  ,   0    ,   0  , 0)

    result['plateWH'] = [x1-x0 ,  y1-y0]
    result['textXY' ] = [    0 ,  y1   ]

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

  elif (plate_name == 'spindle_plate_spacer'):
    SFU1204_nutholder(ctx , 0 , 0 , 0 , '')

    result['plateWH'] = [36 ,  50]
    result['textXY' ] = [ 0 ,  25]

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

  else:
    print("ERROR: don't know how to draw %s-Plate(%s,'%s')" % (plate_group , plate_name , p_variant))
    exit(1)

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

  return result

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -






