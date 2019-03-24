# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 11:44:42 2019

@author: ED
"""


import numpy as np
import pandas as pd
import itertools
import copy

from all_possible_card_states import *
from all_possible_dice_states import *
from val_to_list import *

from new_state import *



card_states = all_possible_card_states()
dice_states = all_possible_dice_states()


c = 0   # 0 to 4095
d = 0 # 0 to 20

z = [ 0 ,0, 0, 0 , 0, 0, 0, 0, 0, 0, 0,0]

huge_state_array = np.zeros((4096 , 21))

#print(card_states[10 , :])
#print(card_states[: , 0])

for c in range (4096):
  #  print('c is')
  #  print(c)
    
    for d in range (21):
  #      print(card_states[c])
        test = new_state(card_states[c , :] , dice_states[d , :])
   #     print('d is')
    #    print(d)
     #   print()
        val = val_to_list(test)
        huge_state_array[c , d] = val
        
        #if (val_to_list(test)) == 4095:
            #print (val_to_list(test))
       # print(test)
  #  card_states = all_possible_card_states()
    
    
#print(card_states[4095 , ])
#print(card_states([test] , )

#print(test)
    
#new_state(card_states[1 , :] , dice_states[20 , :])