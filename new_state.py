import numpy as np
import pandas as pd
import itertools

#euler 640 

def new_state (card_states_x , dice_states_x):
    
    float_card_states = card_states_x
    
    x = []
    for i in range (12) : 
        #print(dice_states_x[i])
        if dice_states_x[i] == 1:
            x.append(i+1)
    
    option_1 = x[0]
    option_2 = x[1]
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

    card_index = options[prob_list.index(min(prob_list))];
 
    
    if float_card_states[card_index-1] == 0:
        prob[card_index] = 1              
    else:
        prob_list[prob_list.index(min(prob_list))] = 1;
        card_index = options[prob_list.index(min(prob_list))]; 
        
  
    if float_card_states[card_index-1] == 0:
        prob[card_index] = 1              
    else:
        prob_list[prob_list.index(min(prob_list))] = 1;
        card_index = options[prob_list.index(min(prob_list))]; 
          
        
    if float_card_states[card_index-1] ==1:
        float_card_states[card_index-1] = 0
    else:
        float_card_states[card_index-1] = 1
            
    return(float_card_states)
   
    #return(z)

