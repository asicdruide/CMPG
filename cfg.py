

# non obvious dependencies:
#  * if you choose the portal.block.thickness >10mm you have to either shorten the X-ballscrew (difficult) or grow the frame in x-direction(easy)
#  * if you choose the  frame.block.thickness >10mm you have to either shorten the Y-ballscrews(difficult) or grow the frame in y-direction(easy)


cfg = {'Portal'    : {'back'              : {'thickness' :  10,'material' : 'alu'}
                     ,'side'              : {'thickness' :  10,'material' : 'alu'}
                     ,'block'             : {'thickness' :  10,'material' : 'alu'}
                     ,'motor_spacer'      : {'thickness' :  10,'material' : 'alu'}
                     ,'nut_spacer'        : {'thickness' :  10,'material' : 'alu'}
                     }

      ,'Frame'     : {'front'             : {'thickness' :  10,'material' : 'alu'}
                     ,'back'              : {'thickness' :  10,'material' : 'alu'}
                     ,'block'             : {'thickness' :  10,'material' : 'alu'}
                     }


      ,'Z-Axis'    : {'spindle'           : {'thickness' :  10,'material' : 'alu'}
                     ,'bottom'            : {'thickness' :  10,'material' : 'alu'}
                     ,'top'               : {'thickness' :  10,'material' : 'alu'}
                     ,'back'              : {'thickness' :  10,'material' : 'alu'}
                     }

      ,'Ballscrew' : {'X'                 : {'length' : 700}  #  650 is baseline design
                     ,'Y'                 : {'length' : 800}  # 1000 is baseline design
                     ,'Z'                 : {'length' : 250}  # don't change this!
                     }
      }



cfg['Portal']['side_plate_spacer'] = {'thickness' :  15 - cfg['Portal']['side']['thickness'],'material'  : 'alu'}

