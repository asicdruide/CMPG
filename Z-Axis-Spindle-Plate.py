import ezdxf
from cfg    import *
from common import *

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def AddOn(width):
  hole = 6.8

  # purpose?
  # in gallery i saw it threaded, don't know why
  # i'd guess these are holes to screw the rails while plate is mounted
  msp.add_circle(( -width/2 + 13.5 , 80) ,   hole/2)
  msp.add_circle(( +width/2 - 13.5 , 80) ,   hole/2)

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Spindle_outline(spindle):
  name = spindle['name']
  y    = spindle['bottom']

  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  if (name == 'GPenny 2.2kW ER20 square air cooled flange'):
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
  elif (name == 'AliEx  1.5kW ER11 square air cooled flange'):
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
  elif (name == 'Amazon 1.5kW ER11 square air cooled flange'):
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
  elif (name == 'GPenny 1.5kW ER20 square air cooled flange'):
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
    print("unknown spindle name '%s' at spindle" % name)
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

  msp.add_lwpolyline(points                                   , dxfattribs={'layer': 'spindle_outline'})

  # reference line of bottom/top of default spindle...
  msp.add_lwpolyline([(-width1 , -67.5 ) , (width1 , -67.5 )] , dxfattribs={'layer': 'spindle_outline'})
  msp.add_lwpolyline([(-width1 , 171.44) , (width1 , 171.44)] , dxfattribs={'layer': 'spindle_outline'})

  return

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Z_Axis_Spindle_Plate(spindle):
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
  MGN12H(msp , -ZRail_xdist/2 , ZBlock_y1 , 0)
  MGN12H(msp , -ZRail_xdist/2 , ZBlock_y2 , 0)
  MGN12H(msp ,  ZRail_xdist/2 , ZBlock_y1 , 0)
  MGN12H(msp ,  ZRail_xdist/2 , ZBlock_y2 , 0)

  SFU1204_nutholder(msp , ZNut_y , 'footprint_vertical')

  AddOn(width)

  Spindle_outline(spindle)

  # add identifying text
  file_name = ('Z-Axis-Spindle-Plate-%s.dxf' % spindle['id'])

  txt = (                 "%s" % file_name
        ,    "width=%5.2f[mm]" % width
        ,   "height=%5.2f[mm]" % height
        ,"thickness=%5.2f[mm]" % (cfg['Z-Axis']['spindle']['thickness'])
        , "material=%s"        % (cfg['Z-Axis']['spindle']['material'])
        , "spindle=%s"         % (spindle['name'])
        )

  for i in range(0,len(txt)):
    msp.add_text(txt[i]
                ,dxfattribs={'style' : 'LiberationSerif'
                            ,'height': 5
                            ,'layer' : 'annotation'
                            }
               ).set_pos((0 , height + 120 - 10*i) , align='MIDDLE_CENTER')

  return file_name

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# loop thru all defined spindles...
for Spindle in [{'name' : 'GPenny 2.2kW ER20 square air cooled flange', 'id' : 'GP_2.2kW_ER20' , 'bottom' : 40}   # e.g. https://de.aliexpress.com/item/1005002490128320.html?spm=a2g0o.store_pc_groupList.8148356.31.3e704e2bZPBZpF
               ,{'name' : 'Amazon 1.5kW ER11 square air cooled flange', 'id' : 'AM_1.5kW_ER11' , 'bottom' : 9.44} # e.g. https://www.amazon.com/gp/product/B06Y42QL2R
               ,{'name' : 'GPenny 1.5kW ER20 square air cooled flange', 'id' : 'GP_1.5kW_ER20' , 'bottom' : 40}   # e.g. https://de.aliexpress.com/item/1005002490128320.html?spm=a2g0o.store_pc_groupList.8148356.10.763a5056MfIubV
               ,{'name' : 'AliEx  1.5kW ER11 square air cooled flange', 'id' : 'AE_1.5kW_ER11' , 'bottom' : 28}   # e.g. https://fr.aliexpress.com/item/32953548253.html?srcSns=sns_Copy&spreadType=socialShare&bizType=ProductDetail&social_params=20498188540&aff_fcid=394633005d0f4e22a981cdcb4ef84ff9-1646684439869-04366-_mKItZoY&tt=MG&aff_fsk=_mKItZoY&aff_platform=default&sk=_mKItZoY&aff_trace_key=394633005d0f4e22a981cdcb4ef84ff9-1646684439869-04366-_mKItZoY&shareId=20498188540&businessType=ProductDetail&platform=AE&terminal_id=21deee05b3694129af60a740b84b062b&afSmartRedirect=y
               ]:

  # Create a new DXF R2010 drawing, official DXF version name: "AC1024"
  doc = ezdxf.new('R2010' , setup=True)

  doc.layers.add(name="annotation"      , color=2)
  doc.layers.add(name="spindle_outline" , color=2)

  # Add new entities to the modelspace:
  msp = doc.modelspace()

  file_name = 'Z-Axis/' + Z_Axis_Spindle_Plate(Spindle)

  doc.saveas(file_name)

  print("INFO: file '%s' written" % file_name)









