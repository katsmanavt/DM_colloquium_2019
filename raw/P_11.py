from classes import *
"""
import MOD_PP_P
import DEG_P_N
"""

def GCF_PP_P(C,D): 
    nod =  Polinomial()
    
    while (C.m or D.m): 
        if (C.m > D.m):
            C = MOD_PP_P(C, D.copy())
            C.m = DEG_P_N(C)
        else: 
            D = MOD_PP_P(D, C.copy()) 
            D.m = DEG_P_N(D)
            
    if (D.m): 
        for i in range(C.m): 
            nod[i] = C[i] 
    else: 
        for i in range(D.m): 
            nod[i] = D[i] 
    return nod
