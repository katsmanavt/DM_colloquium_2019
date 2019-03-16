# Гусев
from classes import Polinomial
#import SUB_QQ_Q

def SUB_PP_P (c1, c2):
    m1 = c1.m
    m2 = c2.m
    c = Polinomial()
    
    if m1 > m2:
        m1, m2 = m2, m1
        c1, c2 = c2, c1
    
    i = 0
    for i in range (m2):
        if i <= m1:
            c[i] = SUB_QQ_Q(c1[i], c2[i])
        else:
            c[i] = c2[i]
        
    c.m = m2
    return c