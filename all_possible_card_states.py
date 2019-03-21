import numpy as np
import pandas as pd
import itertools




def all_possible_card_states ():
    #prodices a 4096 by 12 array with all permutations of states
    possible_card_states_i = [] #[1,12]
    z = np.array(np.zeros((1,12)))  
    for i in itertools.product ( [0,1] , repeat = 12):  
        possible_card_states_i = np.asarray([i])
        x = np.array(possible_card_states_i)
        z = np.concatenate((z, x ) , axis=0)    
    z = np.delete(z , (0) , axis= 0)
    possible_card_states = z
    return (possible_card_states)