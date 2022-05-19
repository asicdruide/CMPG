import math
from cfg        import *
from common     import *


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Frame_Block_connect (ctx , plate_variant , cx , cy , mx):   # center of ballscrew
  hole  = 6.2

  EnsureLayer(ctx , 'th62' , 'through hole 6.2mm (M6 screw)')

  uf = ctx['unit_factor']

  for x,y in [(-28.6 , -32.5)
             ,( 40.5 , -32.5)
             ,( 40.5 ,   7  )
             ,(-28.6 ,  32.5)
             ]:
    ctx['msp'].add_circle((((cx + x) * mx)*uf , (cy + y)*uf) , hole/2*uf , dxfattribs={'layer' : 'th62'})

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Frame_plate(ctx , plate_group , plate_name , plate_variant):
  result = {}

  uf = ctx['unit_factor']

  if (plate_variant==''):
    plate_id = '%s-%s'    % (plate_group,plate_name)
  else:
    plate_id = '%s-%s-%s' % (plate_group,plate_name,plate_variant)


  if (plate_variant == 'left'):
    # normal direction
    mirror_x      = 1
  elif (plate_variant == 'right'):
    # mirrored in x-direction
    mirror_x      = -1
  else:
    print("ERROR: don't know how to draw Frame_Plate(%s,%s" % (plate_name , plate_variant))
    exit(1)

  cr    = 5                     # corner radius
  dbr   = 1.5                   # dog-bone radius => 3mm tool diameter
  cb90  = 0.4142135             # corner bulge = tan(22.5°) for 90° corners
  dbo90 = math.sqrt(2) * dbr    # dog-bone offset for 90° inner corners
  dbb   = 1                     # dogbone bulge


  # if you intend an increased portal-side thickness (e.g. 20mm) you have to stretch the front/back plates and shift some holes.
  if (cfg['Plates']['Portal']['side']['thickness'] <= 15):
    # default design, spacers will pad to 15mm...
    shift_x = 0
  else:
    # custom design...
    shift_x = cfg['Plates']['side']['plate']['thickness'] - 15

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

  if (plate_name == 'front'
      or
      plate_name == 'back'
      ):
    # these two have same outline...

    if (plate_name == 'back'):
      # mirror in x-direction to get chamfers on outside
      mirror_x = -mirror_x


    # I've made a slight deviation from baseline design, here.
    # My intention is to be able to allow longer workpieces to hang over the frame
    # at front and back. To not limit X-opening i've removed the inner triangles.
    # I don't expect that to be a rigity issue.


    # x/y values under the assumption that the center of ballscrew/motor-axis is at (0,0)
    (x0,x1,x2) = [ -36.1     ,  88+shift_x , 163.9+shift_x]
    (y2,y1,y0) = [ 40
                 ,  0
                 ,-40
                 ]

    # draw outer shape...
    shape = ctx['msp'].add_lwpolyline([( (x0+cr   )*mirror_x*uf , (y0   )*uf    , 0            )
                                      ,( (x2-cr   )*mirror_x*uf , (y0   )*uf    , cb90*mirror_x)
                                      ,( (x2      )*mirror_x*uf , (y0+cr)*uf    , 0            )
                                      ,( (x2      )*mirror_x*uf , (y1-cr)*uf    , cb90*mirror_x)
                                      ,( (x2-cr   )*mirror_x*uf , (y1   )*uf    , 0            )
                                      ,( (x1+cr   )*mirror_x*uf , (y1   )*uf    ,-cb90*mirror_x) # inner corner
                                      ,( (x1      )*mirror_x*uf , (y1+cr)*uf    , 0            )
                                      ,( (x1      )*mirror_x*uf , (y2-cr)*uf    , cb90*mirror_x)
                                      ,( (x1-cr   )*mirror_x*uf , (y2   )*uf    , 0            )
                                      ,( (x0+cr   )*mirror_x*uf , (y2   )*uf    , cb90*mirror_x)
                                      ,( (x0      )*mirror_x*uf , (y2-cr)*uf    , 0            )
                                      ,( (x0      )*mirror_x*uf , (y0+cr)*uf    , cb90*mirror_x)
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
    #  = 68mm
    Face40x80(ctx   , ( 68   +shift_x)*mirror_x ,   0 , 0)

    screw = Screw('M5' , cfg['Plates'][plate_group][plate_name]['thickness']
                       + 15   # thread depth
                 )
    doc = '%s to Y-extrusion' % (plate_id)

    Add2BOM(ctx , 8 , 'DIN912' , screw    , doc)    # screw
    Add2BOM(ctx , 8 , 'DIN125' , 'M5'     , doc)    # washer


    Side40x40(ctx   , (126.75+shift_x)*mirror_x , -20 , 0)   # x is rounded, should be uncritical

    screw = Screw('M5' , cfg['Plates'][plate_group][plate_name]['thickness']
                       + 6   # thru sliding nut
                 )
    doc = '%s to frameX-extrusion' % (plate_id)
    Add2BOM(ctx , 8 ,'DIN912'     ,  screw   , doc)    # screw
    Add2BOM(ctx , 8 ,'DIN125'     ,  'M5'    , doc)    # washer
    Add2BOM(ctx , 8 ,'SlidingNut' ,  'M5'    , doc)    # sliding nut

    if (plate_name == 'front'):
      # front
      BF12_face     (ctx ,  0  ,   0 , 0 , 0)

      screw = Screw('M5' , cfg['Plates'][plate_group][plate_name]['thickness']
                         + 20   # BF12 support block
                         + 10   # locknut + safety threads
                   )
      doc = 'Y-BF12 to %s' % (plate_id)

      Add2BOM(ctx , 4, 'DIN912' , screw   , doc)  # screw
      Add2BOM(ctx , 8, 'DIN125' , 'M5'    , doc)  # washer
      Add2BOM(ctx , 4, 'DIN985' , 'M5'    , doc)  # locknut

    elif (plate_name == 'back'):
      # back
      NEMA23             (ctx                 ,   0    ,   0 , 0)

      screw = Screw('M5' , 6    # motor mount + washer
                         + cfg['Plates'][plate_group][plate_name]['thickness']
                         + 10   # locknut + safety threads
                   )

      doc = 'Y-NEMA23 to %s' % (plate_id)
      Add2BOM(ctx , 4, 'DIN912' , screw   , doc)  # screw
      Add2BOM(ctx , 8, 'DIN125' , 'M5'    , doc)  # washer
      Add2BOM(ctx , 4, 'DIN985' , 'M5'    , doc)  # locknut




      Frame_Block_connect(ctx , plate_variant ,   0    ,   0 , mirror_x)

      screw = Screw('M6' , cfg['Plates'][plate_group][plate_name]['thickness']
                         + 15   # thread length inside steel socket
                   )
      doc = 'block to %s' % (plate_id)
      Add2BOM(ctx , 4, 'DIN912'      , screw   , doc)  # screw
      Add2BOM(ctx , 4, 'DIN125'      , 'M6'    , doc)  # washer
      Add2BOM(ctx , 4, 'SteelSocket' , 'M6x40' , doc)  # socket

    result['plateWH'] = [(x2-x0) , (y2-y0)]
    result['textXY' ] = [      0 ,  y2    ]

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

  elif (plate_name == 'block'):
    # x/y values under the assumption that the center of ballscrew/motor-axis is at (0,0)
    (x0 , x1 , x2 , x3) = [-36.1 , -17.2 , 17.2 , 48]
    (y3 , y2 , y1 , y0) = [ 40
                          , 14.5
                          ,-17.2
                          ,-40
                          ]

    cr=5

    # outer shape...
    shape = ctx['msp'].add_lwpolyline([( (x0+cr   )*mirror_x*uf , (y0      )*uf , 0            )
                                      ,( (x3-cr   )*mirror_x*uf , (y0      )*uf , cb90*mirror_x)
                                      ,( (x3      )*mirror_x*uf , (y0+cr   )*uf , 0            )
                                      ,( (x3      )*mirror_x*uf , (y2-cr   )*uf , cb90*mirror_x)
                                      ,( (x3-cr   )*mirror_x*uf , (y2      )*uf , 0            )
                                      ,( (x2+cr   )*mirror_x*uf , (y2      )*uf , cb90*mirror_x)
                                      ,( (x2      )*mirror_x*uf , (y2-cr   )*uf , 0            )
                                      ,( (x2      )*mirror_x*uf , (y1+dbo90)*uf ,-dbb *mirror_x)
                                      ,( (x2-dbo90)*mirror_x*uf , (y1      )*uf , 0            )
                                      ,( (x1+dbo90)*mirror_x*uf , (y1      )*uf ,-dbb *mirror_x)
                                      ,( (x1      )*mirror_x*uf , (y1+dbo90)*uf , 0            )
                                      ,( (x1      )*mirror_x*uf , (y3-cr   )*uf , cb90*mirror_x)
                                      ,( (x1-cr   )*mirror_x*uf , (y3      )*uf , 0            )
                                      ,( (x0+cr   )*mirror_x*uf , (y3      )*uf , cb90*mirror_x)
                                      ,( (x0      )*mirror_x*uf , (y3-cr   )*uf , 0            )
                                      ,( (x0      )*mirror_x*uf , (y0+cr   )*uf , cb90*mirror_x)
                                      ]
                                     , format='xyb'
                                     )
    shape.close(True)

    # add other elements...
    Frame_Block_connect(ctx , plate_variant ,  0    ,   0  , mirror_x)
    screw = Screw('M6' , cfg['Plates'][plate_group][plate_name]['thickness']
                       + 15   # thread length inside steel socket
                 )
    doc = '%s to %s-back' % (plate_id , plate_group)
    Add2BOM(ctx , 4, 'DIN912'      , screw   , doc)  # screw
    Add2BOM(ctx , 4, 'DIN125'      , 'M6'    , doc)  # washer




    BK12_face          (ctx       ,  0    ,   0  , 0)
    screw = Screw('M5' , 25   # BK12 block
                       + cfg['Plates'][plate_group][plate_name]['thickness']
                       + 10   # locknut + safety threads
                 )
    doc = 'Y-BK12 to %s' % (plate_id)
    Add2BOM(ctx , 4, 'DIN912'      , screw   , doc)  # screw
    Add2BOM(ctx , 8, 'DIN125'      , 'M5'    , doc)  # washer
    Add2BOM(ctx , 4, 'DIN985'      , 'M5'    , doc)  # locknut

    result['plateWH'] = [(x3-x0) , (y3-y0)]
    result['textXY' ] = [      0 ,  y3    ]

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

  else:
    print("ERROR: don't know how to draw Frame_Plate(%s,%s)" % (plate_name , plate_variant))
    exit(1)


  return result
