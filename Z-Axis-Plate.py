import ezdxf
from cfg    import *
from common import *

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def Z_Axis_Plate(name):
  cr    = 5                     # corner radius
  dbr   = 2.0                   # dog-bone radius => 3mm tool diameter
  cb90  = 0.4142135             # corner bulge = tan(22.5°) for 90° corners
  dbo90 = math.sqrt(2) * dbr    # dog-bone offset for 90° inner corners
  dbb   = 1                     # dogbone bulge

  file_name = ('Z-Axis-Plate-%s.dxf' % (name))

  if (name == 'bottom'):
    # x/y values under the assumption that the center of ballscrew/motor-axis is at (0,0)
    xadj = 10 - cfg['Z-Axis']['back']['thickness']

    (x1,x2,x3,x4      ) = [ -43+xadj  ,  -32.15+xadj , -21.85 , 17                ]
    (y1,y2,y3,y4,y5,y6) = [ -80       ,  -59.85      , -10.15 , 10.15 , 59.85 , 80]

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
    text_y = y6 + 60
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
  elif (name == 'top'):
    # x/y values under the assumption that the center of ballscrew/motor-axis is at (0,0)
    xadj = 10 - cfg['Z-Axis']['back']['thickness']

    (x1,x2,x3,x4,x5         ) = [ -33.5 , -17    ,  21.85 ,  32.15-xadj , 46.5-xadj                    ]
    (y1,y2,y3,y4,y5,y6,y7,y8) = [ -80   , -59.85 , -33.5  , -10.15      , 10.15     , 33.5 , 59.85 , 80]

    # draw outer shape...
    shape = msp.add_lwpolyline([( x1+cr    , y3       , 0   ) #  1
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
                               ,( x1+cr    , y6       , cb90) # 26
                               ,( x1       , y6-cr    , 0   ) # 27
                               ,( x1       , y3+cr    , cb90) # 28
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
    text_y = y8 + 60
  # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



  # add identifying text
  txt = (                 "%s" % file_name
        ,    "width=%5.2f[mm]" % width
        ,   "height=%5.2f[mm]" % height
        ,"thickness=%5.2f[mm]" % (cfg['Z-Axis'][name]['thickness'])
        , "material=%s"        % (cfg['Z-Axis'][name]['material'])
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

# loop thru all defined spindles...
for name in ['bottom'
            ,'top'
            ]:

  # Create a new DXF R2010 drawing, official DXF version name: "AC1024"
  doc = ezdxf.new('R2010' , setup=True)

  doc.layers.add(name="annotation"      , color=2)
  doc.layers.add(name="outline"         , color=2)

  # Add new entities to the modelspace:
  msp = doc.modelspace()

  file_name = 'Z-Axis/' + Z_Axis_Plate(name)

  doc.saveas(file_name)

  print("INFO: file '%s' written" % file_name)









