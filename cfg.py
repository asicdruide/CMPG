

# non obvious dependencies:
#  * if you choose the portal.block.thickness >10mm you have to either shorten the X-ballscrew (difficult) or grow the frame in x-direction(easy)
#  * if you choose the  frame.block.thickness >10mm you have to either shorten the Y-ballscrews(difficult) or grow the frame in y-direction(easy)


cfg = {'Plates' : {'Frame'     : {'front'                : {'thickness' :  10,'material' : 'alu' , 'variant' : ['left','right'],'amount':1}
                                 ,'back'                 : {'thickness' :  10,'material' : 'alu' , 'variant' : ['left','right'],'amount':1}
                                 ,'block'                : {'thickness' :  10,'material' : 'alu' , 'variant' : ['left','right'],'amount':1}
                                 }
                  ,'Portal'    : {'side'                 : {'thickness' :  15,'material' : 'alu' , 'variant' : ['left','right'],'amount':1}
                                 ,'back'                 : {'thickness' :  10,'material' : 'alu' , 'variant' : [''            ],'amount':1}
                                 ,'block'                : {'thickness' :  10,'material' : 'alu' , 'variant' : [''            ],'amount':1}
                                 ,'motor_spacer'         : {'thickness' :   0,'material' : 'alu' , 'variant' : [''            ],'amount':1}
                                 ,'nut_spacer'           : {'thickness' :  10,'material' : 'alu' , 'variant' : [''            ],'amount':1}
                                 ,'side_plate_spacer'    : {'thickness' :   0,'material' : 'alu' , 'variant' : [''            ],'amount':2}
                                 }



                   ,'ZAxis'    : {'front'                : {'thickness' :  10,'material' : 'alu' , 'variant' : [''            ],'amount':1}
                                 ,'bottom'               : {'thickness' :  10,'material' : 'alu' , 'variant' : [''            ],'amount':1}
                                 ,'top'                  : {'thickness' :  15,'material' : 'alu' , 'variant' : [''            ],'amount':1}
                                 ,'back'                 : {'thickness' :  10,'material' : 'alu' , 'variant' : [''            ],'amount':1}
                                 ,'rail_spacer'          : {'thickness' :   7,'material' : 'alu' , 'variant' : [''            ],'amount':4}
                                 ,'motor_spacer'         : {'thickness' :   0,'material' : 'alu' , 'variant' : [''            ],'amount':1}
                                 ,'spindle_plate_spacer' : {'thickness' :   3,'material' : 'alu' , 'variant' : [''            ],'amount':1}
                              #  ,'spindle_adapter'      : {'thickness' :  10,'material' : 'alu' , 'variant' : [''            ],'amount':1}
                                 }
                  }

      ,'Ballscrew' : {'X'                    : {'length' : 700}  #  650 is baseline design
                     ,'Y'                    : {'length' : 800}  # 1000 is baseline design
                     ,'Z'                    : {'length' : 250}  # don't change this!
                     }
      ,'unit_factor' : 1.0
      }


# baseline design assumes a portal side thickness of 15mm
# if you have 10, you need a spacer of 5mm
cfg['Plates']['Portal']['side_plate_spacer']['thickness']=  15 - cfg['Plates']['Portal']['side']['thickness']

# baseline design assumes a total thickness of 20mm
# if you have 10, you need a spacer of 10mm
cfg['Plates']['Portal']['motor_spacer']['thickness']=  20 - cfg['Plates']['Portal']['side']['thickness']

# baseline design assumes a Z-Axis-top thickness of 15mm
# if you have 10, you need a spacer of 5mm
cfg['Plates']['ZAxis']['motor_spacer']['thickness']=  15 - cfg['Plates']['ZAxis']['top']['thickness']
