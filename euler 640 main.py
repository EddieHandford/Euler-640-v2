# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 11:44:42 2019

@author: ED
"""


import numpy as np
import pandas as pd
import itertools

from all_possible_card_states import *
from all_possible_dice_states import *
from new_state import *



card_states = all_possible_card_states()
dice_states = all_possible_dice_states()


c = 0   # 0 to 4095
d = 1   # 0 to 20

z = [ 0 ,0, 0, 0 , 0, 0, 0, 0, 0, 0, 0,0]

for d in range (20):
  
    test = new_state(card_states[0] , dice_states[d])
    card_states = all_possible_card_states()
    
    
#print(card_states[4095 , ])
#print(card_states([test] , )

#print(test)