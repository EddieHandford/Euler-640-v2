# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 11:53:55 2019

@author: ED
"""


import numpy as np
import pandas as pd
import itertools

def all_possible_dice_states () : 

    #create input dice array
    state_1 =  [1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
    state_2 =  [1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
    state_3 =  [1 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
    state_4 =  [1 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
    state_5 =  [1 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0]
    state_6 =  [1 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 0]
    state_7 =  [0 , 1 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
    state_8 =  [0 , 1 , 1 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
    state_9 =  [0 , 1 , 0 , 1 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0]
    state_10 = [0 , 1 , 0 , 0 , 1 , 0 , 1 , 0 , 0 , 0 , 0 , 0]
    state_11 = [0 , 1 , 0 , 0 , 0 , 1 , 0 , 1 , 0 , 0 , 0 , 0]
    state_12 = [0 , 0 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0]
    state_13 = [0 , 0 , 1 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0]
    state_14 = [0 , 0 , 1 , 0 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 0]
    state_15 = [0 , 0 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0]
    state_16 = [0 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0]
    state_17 = [0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0]
    state_18 = [0 , 0 , 0 , 1 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0]
    state_19 = [0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0]
    state_20 = [0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 1 , 0]
    state_21 = [0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 1]
    
    possible_dice_states = [state_1 , state_2 , state_3 , state_4 , 
                            state_5 , state_6 , state_7 , state_8 , 
                            state_9 , state_10 , state_11 , state_12,
                            state_13 , state_14 , state_15 , state_16 , 
                            state_17 , state_18 , state_19 , state_20,
                            state_21]
    possible_dice_states = np.asarray(possible_dice_states)
    
    return (possible_dice_states)


