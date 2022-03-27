import ezdxf
from ezdxf    import units
from cfg      import *
from common   import *
from datetime import datetime

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def SpindleAddOn(width):
  hole = 6.8

  # purpose?
  # in gallery i saw it threaded, don't know why
  # i'd guess these are holes to screw the rails while plate is mounted
  msp.add_circle(( -width/2 + 13.5 , 80) ,   hole/2)
  msp.add_circle(( +width/2 - 13.5 , 80) ,   hole/2)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def BackAddOn(cx , cy):
  hole = 6.8

  # purpose?
  msp.add_circle(( cx , cy) ,   hole/2)
  msp.add_circle((-cx , cy) ,   hole/2)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def RailMount(x , y1 , y2 , y3 , y4):
  hole = 5.2

  for (x,y) in [[x , y1]
               ,[x , y2]
               ,[x , y3]
               ,[x , y4]
               ]:
    msp.add_circle(( x , y) , hole/2)
    msp.add_circle((-x , y) , hole/2)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Spindle_outline(msp , p_variant):
  spindle = ({'name' : 'GPenny 2.2kW ER20 square air cooled flange', 'id' : 'GP_2.2kW_ER20' , 'bottom' : 40}   # e.g. https://de.aliexpress.com/item/1005002490128320.html?spm=a2g0o.store_pc_groupList.8148356.31.3e704e2bZPBZpF
            ,{'name' : 'Amazon 1.5kW ER11 square air cooled flange', 'id' : 'AM_1.5kW_ER11' , 'bottom' : 9.44} # e.g. https://www.amazon.com/gp/product/B06Y42QL2R
            ,{'name' : 'GPenny 1.5kW ER20 square air cooled flange', 'id' : 'GP_1.5kW_ER20' , 'bottom' : 40}   # e.g. https://de.aliexpress.com/item/1005002490128320.html?spm=a2g0o.store_pc_groupList.8148356.10.763a5056MfIubV
            ,{'name' : 'AliEx  1.5kW ER11 square air cooled flange', 'id' : 'AE_1.5kW_ER11' , 'bottom' : 28}   # e.g. https://fr.aliexpress.com/item/32953548253.html?srcSns=sns_Copy&spreadType=socialShare&bizType=ProductDetail&social_params=20498188540&aff_fcid=394633005d0f4e22a981cdcb4ef84ff9-1646684439869-04366-_mKItZoY&tt=MG&aff_fsk=_mKItZoY&aff_platform=default&sk=_mKItZoY&aff_trace_key=394633005d0f4e22a981cdcb4ef84ff9-1646684439869-04366-_mKItZoY&shareId=20498188540&businessType=ProductDetail&platform=AE&terminal_id=21deee05b3694129af60a740b84b062b&afSmartRedirect=y
            )

  v_name = spindle[p_variant]['name']
  y      = spindle[p_variant]['bottom']

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  if (v_name == 'GPenny 2.2kW ER20 square air cooled flange'):
    hole_x_width  =  95
    hole_y_space  =  35
    hole          =   5   # threaded with M6
    width1        = 110
    width2        =  80
    width3        =  65
    width4        =  34

    x1  = -width1 / 2    # leftmost X
    x2  = -width2 / 2
    x3  = -width3 / 2
    x4  = -width4 / 2
    x5  =  width4 / 2
    x6  =  width3 / 2
    x7  =  width2 / 2
    x8  =  width1 / 2    # rightmost X


    y1  =  y  - 30 - 10 - 20 - 43   # bottom Y (collet)
    y2  =  y1 + 43
    y3  =  y2 + 20
    y4  =  y3 + 10
    y5  =  y
    y6  =  y5 + 3*hole_y_space + 31
    y7  =  y6 + 28        # top Y

    mountN = 3
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  elif (v_name == 'AliEx  1.5kW ER11 square air cooled flange'):
    hole_x_width  =  95
    hole_y_space  =  35
    hole          =   5   # threaded with M6
    width1        = 110
    width2        =  80
    width3        =  60
    width4        =  19

    x1  = -width1 / 2    # leftmost X
    x2  = -width2 / 2
    x3  = -width3 / 2
    x4  = -width4 / 2
    x5  =  width4 / 2
    x6  =  width3 / 2
    x7  =  width2 / 2
    x8  =  width1 / 2    # rightmost X


    # no data from drawing, estimating that first hole is 25 + 30 + 25 from collet...
    y1  =  y  - 25 - 10 - 20 - 25   # bottom Y (collet)
    y2  =  y1 + 25
    y3  =  y2 + 20
    y4  =  y3 + 10
    y5  =  y
    y6  =  y5 + 3*hole_y_space + 25
    y7  =  y6 + 28        # top Y

    mountN = 4
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  elif (v_name == 'Amazon 1.5kW ER11 square air cooled flange'):
    hole_x_width  =  81
    hole_y_space  =  38
    hole          =   5   # threaded with M6
    width1        =  91
    width2        =  67
    width3        =  51
    width4        =  22

    x1  = -width1 / 2    # leftmost X
    x2  = -width2 / 2
    x3  = -width3 / 2
    x4  = -width4 / 2
    x5  =  width4 / 2
    x6  =  width3 / 2
    x7  =  width2 / 2
    x8  =  width1 / 2    # rightmost X


    y1  =  y  - 20 - 7 - 18 - 32 # bottom Y (collet)
    y2  =  y1 + 32
    y3  =  y2 + 18
    y4  =  y3 +  7
    y5  =  y
    y6  =  y5 + 3*hole_y_space + 20
    y7  =  y6 + 28        # top Y

    mountN = 4
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  elif (v_name == 'GPenny 1.5kW ER20 square air cooled flange'):
    hole_x_width  =  95
    hole_y_space  =  61
    hole          =   5   # threaded with M6
    width1        = 110
    width2        =  75
    width3        =  68
    width4        =  34

    x1  = -width1  / 2    # leftmost X
    x2  = -width2  / 2
    x3  = -width3  / 2
    x4  = -width4  / 2

    x5  =  width4  / 2
    x6  =  width3  / 2
    x7  =  width2  / 2
    x8  =  width1  / 2    # rightmost X

    y1  =  y  - 40 - 8 - 20 - 10 - 47 # bottom Y (collet)
    y2  =  y1 + 47
    y3  =  y2 + 10
    y4  =  y3 + 28
    y5  =  y
    y6  =  y5 + hole_y_space + 38
    y7  =  y6 + 37        # top Y

    mountN = 2
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  else:
    print("unknown spindle name '%s' at spindle" % v_name)
    exit(1)
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


  # place holes...
  for i in range(0,mountN):
    msp.add_circle((-hole_x_width / 2 , y + i*hole_y_space) , hole/2)
    msp.add_circle(( hole_x_width / 2 , y + i*hole_y_space) , hole/2)


  # draw outline of spindle
  points = [(x1 , y4)
           ,(x2 , y4)
           ,(x2 , y3)
           ,(x3 , y3)
           ,(x3 , y2)
           ,(x4 , y2)
           ,(x4 , y1)
           ,(x5 , y1)
           ,(x5 , y2)
           ,(x6 , y2)
           ,(x6 , y3)
           ,(x7 , y3)
           ,(x7 , y4)
           ,(x8 , y4)
           ,(x8 , y6)
           ,(x7 , y6)
           ,(x7 , y7)
           ,(x2 , y7)
           ,(x2 , y6)
           ,(x1 , y6)
           ,(x1 , y4)
           ]

  msp.add_lwpolyline(points                                   , dxfattribs={'layer': 'outline'})

  # reference line of bottom/top of default spindle...
  msp.add_lwpolyline([(-width1 , -67.5 ) , (width1 , -67.5 )] , dxfattribs={'layer': 'outline'})
  msp.add_lwpolyline([(-width1 , 171.44) , (width1 , 171.44)] , dxfattribs={'layer': 'outline'})

  return "-"+spindle[p_variant]['id']

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Z_Axis_Plate(p_name , p_variant):
  cr    = 5                     # corner radius
  dbr   = 2.0                   # dog-bone radius => 3mm tool diameter
  cb90  = 0.4142135             # corner bulge = tan(22.5°) for 90° corners
  dbo90 = math.sqrt(2) * dbr    # dog-bone offset for 90° inner corners
  dbb   = 1                     # dogbone bulge

  file_name_add = ""

  if (p_name == 'bottom'):
    # x/y values under the assumption that the center of ballscrew/motor-axis is at (0,0)
    xadj = 10 - cfg['Z-Axis']['back']['thickness']

    (x1,x2,x3,x4      ) = [ -43+xadj  ,  -32.15+xadj , -21.85 , 17]
    (y6,y5,y4,y3,y2,y1) = [ 80
                          , 59.85
                          , 10.15
                          ,-10.15
                          ,-59.85
                          ,-80
                          ]

    # draw outer shape...
    shape = msp.add_lwpolyline([( x1+cr    , y1       , 0   ) #  1
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
    shape = msp.add_lwpolyline([( x2+dbo90 , y3       , 0   ) #  1
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
    msp.add_circle((0 , 0) , 11.25)
    #BF10_face(msp , 0 , 0 , -90)

    msp.add_circle((-5 ,  66.5) , 5.2/2)
    msp.add_circle((-5 , -66.5) , 5.2/2)

    msp.add_circle((x1+32.75 ,  44.75) , 6.8/2)
    msp.add_circle((x1+32.75 , -44.75) , 6.8/2)


    width  = (x4-x1)
    height = (y6-y1)

    text_x = (x4 + x1) / 2
    text_y = y6
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  elif (p_name == 'top'):
    # x/y values under the assumption that the center of ballscrew/motor-axis is at (0,0)
    xadj = 10 - cfg['Z-Axis']['back']['thickness']

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
    shape = msp.add_lwpolyline([( x1+10    , y3       , 0   ) #  1
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
    shape = msp.add_lwpolyline([( x3+dbo90 , y4       , 0   ) #  1
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
    NEMA23(msp , 0 , 0 , 0)
    #
    msp.add_circle((5 ,  66.5) , 5.2/2)
    msp.add_circle((5 , -66.5) , 5.2/2)

    msp.add_circle((39.32-xadj ,  34.96*2) , 3.2/2)
    msp.add_circle((39.32-xadj ,  34.96*1) , 3.2/2)
    msp.add_circle((39.32-xadj ,  34.96*0) , 3.2/2)
    msp.add_circle((39.32-xadj , -34.96*1) , 3.2/2)
    msp.add_circle((39.32-xadj , -34.96*2) , 3.2/2)


    width  = (x5-x1)
    height = (y8-y1)

    text_x = (x5 + x1) / 2
    text_y = y8
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  elif (p_name == 'spindle'):
    # free parameters
    width          = 160     #  width of plate
    height         = 140     # height of plate

    width2         =  94     # bottom nose width
    height2        =  20     # bottom nose height

    ZRail_xdist    = 133

    ZBlock_y1      = 118     # might be calculated with offset from plate boundaries
    ZBlock_y2      =  42     # might be calculated with offset from plate boundaries
    ZNut_y         =  78     # how is value calculated?

    cr    = 3                     # corner radius
    cb90  = 0.4142135             # corner bulge = tan(22.5°) for 90° corners

    # outer shape of Z-Axis-Spindle-Plate
    x0 = -width  / 2    # leftmost X
    x1 = -width2 / 2
    x2 =  width2 / 2
    x3 =  width  / 2    # rightmost X

    y0 =           0    # bottom Y
    y1 =  height2
    y2 =  height        # top Y

    shape = msp.add_lwpolyline([( (x1+cr   ) , y0       , 0   )
                               ,( (x2-cr   ) , y0       , cb90)
                               ,( (x2      ) , y0+cr    , 0   )
                               ,( (x2      ) , y1-cr    ,-cb90)
                               ,( (x2+cr   ) , y1       , 0   )
                               ,( (x3-cr   ) , y1       , cb90)
                               ,( (x3      ) , y1+cr    , 0   )
                               ,( (x3      ) , y2-cr    , cb90)
                               ,( (x3-cr   ) , y2       , 0   )
                               ,( (x0+cr   ) , y2       , cb90)
                               ,( (x0      ) , y2-cr    , 0   )
                               ,( (x0      ) , y1+cr    , cb90)
                               ,( (x0+cr   ) , y1       , 0   )
                               ,( (x1-cr   ) , y1       ,-cb90)
                               ,( (x1      ) , y1-cr    , 0   )
                               ,( (x1      ) , y0+cr    , cb90)
                               ]
                              , format='xyb'
                              )
    shape.close(True)

    # Assemble parts
    MGN12H(msp , -ZRail_xdist/2 , ZBlock_y1 , 90)
    MGN12H(msp , -ZRail_xdist/2 , ZBlock_y2 , 90)
    MGN12H(msp ,  ZRail_xdist/2 , ZBlock_y1 , 90)
    MGN12H(msp ,  ZRail_xdist/2 , ZBlock_y2 , 90)

    SFU1204_nutholder(msp , 0 , ZNut_y , 90, 'spindle')

    SpindleAddOn(width)

    file_name_add = Spindle_outline(msp , p_variant)

    text_x =   0
    text_y = 200

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

  elif (p_name == 'back'):
    margin = 0.5
    # x/y values
    (x1,x2,x3,x4,x5,x6,x7,x8,x9,x10) = [-80 , -60 , -28.57 , -18.57 , -10 , 10 , 18.57 , 28.57 , 60 , 80]

    # Y-adjust when top-plate is thicker than 10mm
    # the upper edge has to stay unchanged
    yadj = cfg['Z-Axis']['top']['thickness'] - 10

    if (yadj < -10):
      print("ERROR: Z-Axis-top-plate is too thick! (%dmm)" % (cfg['Z-Axis']['top']['thickness']))
      print("       can't shift rail spacer further down")
      exit(1)


    y5  = 280    + yadj
    y4  = 279.5  + yadj
    y3  = 270
    y2  = 260
    y1  = 0.5
    y0  = 0
    ym1 = -cfg['Z-Axis']['bottom']['thickness']

    # draw outer shape...
    shape = msp.add_lwpolyline([( x1       , ym1      , 0   ) #  1
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
    MGN12H(msp , -58 ,  14  ,   0)
    MGN12H(msp ,  58 ,  14  ,   0)
    MGN12H(msp , -58 , 159  ,   0)
    MGN12H(msp ,  58 , 159  ,   0)

    # shifted BF10 a little up to avoid contact with bottom-plate
    BF10_footprint(msp , 0 ,  10+margin  , 90)
    BK10_footprint(msp , 0 , 212.75      , 90)

    SFU1605_holder(msp , 0 , 86.5 , 0)

    BackAddOn(40 , 197.78)  # what is the purpose of this?

    # shifted upper spacer a little down to avoid contact with top-plate
    RailMount(66.5 , 54 , 122.67 , 191.33-margin  , 260-margin)


    width  = x10-x1    #  width of plate
    height = y5-ym1    # height of plate
    text_x = 0
    text_y = height

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

  elif (p_name == 'rail_spacer'):
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
    shape = msp.add_lwpolyline([( x1+cr , y1       , 0   )   #  1
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

    msp.add_circle((0 ,  d/2) , hole/2)
    msp.add_circle((0 , -d/2) , hole/2)


    width  = x2-x1     #  width of plate
    height = y2-y1     # height of plate
    text_x = 0
    text_y = height/2

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

  elif (p_name == 'motor_spacer'):
    # x/y values under the assumption that the center of ballscrew/motor-axis is at (0,0)
    (x0 , x1) = [-28.5 , 28.5]
    (y0 , y1) = [-28.5 , 28.5]

    # outer shape...
    shape = msp.add_lwpolyline([( (x0+cr   ) , y0       , 0   )   #  1
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
    NEMA23(msp  ,   0    ,   0  , 0)

    width  = (x1-x0)
    height = (y1-y0)

    text_x = 0
    text_y = y1

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

  elif (p_name == 'spindle_plate_spacer'):
    SFU1204_nutholder(msp , 0 , 0 , 0 , '')

    width  = 36
    height = 50

    text_x = 0
    text_y = 25

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

  else:
    print("ERROR: don't know how to draw Z-Axis-Plate(%s,%s)" % (p_name , p_variant))
    exit(1)

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

  file_name = ('Z-Axis-%s%s.dxf' % (p_name , file_name_add))



  # add identifying text
  txt = [                 "%s" % file_name
        ,    "width=%5.2f[mm]" % width
        ,   "height=%5.2f[mm]" % height
        ,"thickness=%5.2f[mm]" % (cfg['Z-Axis'][p_name]['thickness'])
        , "material=%s"        % (cfg['Z-Axis'][p_name]['material'])
        ,   "amount=%d"        % (cfg['Z-Axis'][p_name]['amount'])
        ,   "%s"               % (datetime.now().strftime("%a %Y-%b-%d %H:%M:%S"))
        ]

  if (p_name == 'back'):
    txt.append("variant for %dmm thick top and %dmm thick bottom"    % (cfg['Z-Axis']['top'   ]['thickness'],cfg['Z-Axis']['bottom']['thickness']))




  for i in range(0,len(txt)):
    msp.add_text(txt[i]
                ,dxfattribs={'style' : 'LiberationSerif'
                            ,'height': 5
                            ,'layer' : 'annotation'
                            }
               ).set_pos((text_x , text_y + 10*len(txt) - 10*i) , align='MIDDLE_CENTER')


  return  "%dx_%dmm_%s" % (cfg['Z-Axis'][p_name]['amount']
                          ,cfg['Z-Axis'][p_name]['thickness']
                          ,file_name
                          )

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# loop thru all defined spindles...
for p_name in      cfg['Z-Axis'].keys():
  for p_variant in cfg['Z-Axis'][p_name]['variant']:
    if (           cfg['Z-Axis'][p_name]['thickness'] > 0):
      # Create a new DXF R2010 drawing, official DXF version name: "AC1024"
      doc = ezdxf.new('R2010' , setup=True)

      my_annotations = doc.layers.add(name="annotation"      , color=2)
      my_outline     = doc.layers.add(name="outline"         , color=2)
      doc.units      = units.MM

      # Add new entities to the modelspace:
      msp = doc.modelspace()

      file_name = 'Z-Axis/' + Z_Axis_Plate(p_name , p_variant)

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










