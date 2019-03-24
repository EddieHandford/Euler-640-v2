# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 19:20:56 2019

@author: Eddie
"""

def val_to_list (value):
#    [0. 0. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
    
    
    x0 = value[0]
    x1 = value[1]
   
    x2 = value[2]
    x3 = value[3]
   
    x4 = value[4]
    x5 = value[5]
   
    x6 = value[6]
    x7 = value[7]
   
    x8 = value[8]
    x9 = value[9]
    
    x10 = value[10]
    x11 = value[11]
    
    y = x0 + x1*2 + x2*2**2 + x3*2**3 + x4*2**4 + x5*2**5 + x6*2**6 + x7*2**7 + x8*2**8 + x9*2**9 + x10*2**10 + x11*2**11
    
    
    return(y)