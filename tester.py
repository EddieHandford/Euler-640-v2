# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 19:44:36 2019

@author: Eddie
"""

import numpy as np
import pandas as pd
import itertools
import copy


new_state (card_states_x , dsx):
    
#card_states_x = card_states[1 , :]
#dsx = dice_states[20 , :]
#card_states_x = copy.deepcopy(card_states[0])
#dice_states_x = copy.deepcopy(dice_states[0])
    
    fcs = copy.deepcopy(card_states_x)
    dice_states_x = copy.deepcopy(dsx)
    
    
    
    x = []
    for i in range (12) : 
        #print(dice_states_x[i])
        if dice_states_x[i] == 1:
            x.append(i+1)
    
    option_1 = x[0]
    option_2 = x[1]
    gamma = len(x)
    if len(x) == 2 :
        option_3 = x[1]
    else:
        option_3 = x[2]
    
    options = [option_1,option_2,option_3]
    #gives the dice rolls
    
    #probability lookup table
    n0  = 0.99
    n1  = 11/36
    n2  = 12/36
    n3  = 13/36
    n4  = 14/36
    n5  = 15/36
    n6  = 16/36
    n7  = 6/36
    n8  = 5/36
    n9  = 4/36
    n10 = 3/36
    n11 = 2/36
    n12 = 1/36
    prob = np.array([n0 , n1 , n2 , n3 , n4 , n5 , n6 , n7 , n8 , n9 , n10 , n11 , n12])
      
    p1 = prob[(options[0])]
    p2 = prob[(options[1])]
    p3 = prob[(options[2])]
    
    prob_list = []
    prob_list.append(p1)
    prob_list.append(p2)
    prob_list.append(p3)
    
    
    
    #which card is lowest probability
    card_index = options[prob_list.index(min(prob_list))];
    
    
    
    #if gamma == 3:
    
    #if card is face down , flip face up
    if fcs[card_index-1] == 0:
        fcs[card_index-1] = 1
          
    #if it is face up , change its probabilty to be 1 , 
    else:
        
        #this line is wrong
        prob_list[prob_list.index(min(prob_list))] = 1
    
        #pick a new card
        card_index = options[prob_list.index(min(prob_list))]; 
        
        #if the next pick is face down , flip it up !
        if fcs[card_index-1] == 0:
            fcs[card_index-1] = 1       
        #if its not face up , change its probabilty to 1     
             
        else:
            
            
            prob_list[prob_list.index(min(prob_list))] = 1
            
            
            #pick the next card!
            card_index = options[prob_list.index(min(prob_list))]; 
          
            #flip this card irrelevant of its state , because you have to !
            if fcs[card_index-1] ==1:
                fcs[card_index-1] = 0
            else:
                fcs[card_index-1] = 1
    
    
    
    #
    #else :
    #    
    #    if fcs[card_index-1] == 0:
    #        fcs[card_index-1] = 1
    #          
    #    #if it is face up , change its probabilty to be 1 , 
    #    else:
    #        prob_list[prob_list.index(min(prob_list))] = 1
    #        
    #        #pick a new card
    #        card_index = options[prob_list.index(min(prob_list))]; 
    #        
    #        if fcs[card_index-1] ==1:
    #            fcs[card_index-1] = 0
    #        else:
    #            fcs[card_index-1] = 1
    #        
            
            
            
            
            
    
    
    #return(float_card_states)
    return(fcs)
       
    #return(z)