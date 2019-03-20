from modules.classes import *
from modules.N import *
from modules.Z import *
from modules.Q import *


# P-1
def ADD_PP_P(c1, c2):
    m1 = c1.m
    m2 = c2.m
    c = Polinomial()
    
    if m1 > m2:
        m1, m2 = m2, m1
        c1, c2 = c2, c1
    
    i = 0
    while i <= m2:
        if i <= m1:
            c[i] = ADD_QQ_Q(c1[i], c2[i])
        else:
            c[i] = c2[i]
        i += 1
    
    c.m = m2
    return c


# P-2
def SUB_PP_P(C1, C2):
    c1 = C1.copy()
    c2 = C2.copy()
    mul = Rational (
        Integer(0, -1),
        Natural(0, 1)
    )
    c2 = MUL_PQ_P(c2, mul)
    c = ADD_PP_P(c1, c2)
    
    c.m = DEG_P_N(c)
    return c
    

# P-3
def MUL_PQ_P(C, z):
    m = DEG_P_N(C)
    P = Polinomial
    
    for i in range(m+1):
        if C[i] == 0:
            P[i] = 0
        else:
            P[i] = MUL_QQ_Q(C[i], z)
    
    P.m = m
    return P
    
    
# P-4
def MUL_Pxk_P(a, k):
    c = a.copy()
    if c.m != 0 or c[0] != 0:
        for i in range(m, -1, -1):
            c[i+k] = c[i]
        for i in range(k+1):
            c[i] = 0
        c.m = c.m + k
    return c


# P-5
def LED_P_Q(C):
    return C[DEG_P_N(C)]


# P-6
def DEG_P_N(P):
    i = P.m
    while P[i] != 0 and i > 0:
        i -= 1
    P.m = i 
    return i


# P-7
def FAC_P_Q(p):
    if p.n != 0:
        prevk = ABS_Z_N(p[0].m.copy())
        prevd = ABS_Z_N(p[0].n.copy())
        s = p[0]
        for i in range(1, n+1):
            prevk = LCM_NN_N(prevk, ABS_Z_N(p[i].m))
            prevd = LCM_NN_N(prevd, p[i].n)
            if p[i] != 0:
                s = MUL_ZZ_Z(s, p[i].m)
        q.m = TRANS_N_Z(DIV_NN_N(ABS_Z_N(s), prev_k))
        q.n = prev_d
    else:
        q.m = p[0].m
        q.n = p[0].n
    return q


# P-8
def MUL_PP_P(c1, c2):
    c = Polinomial()
    tmp = Polinomial()
    for i in range(c2.m+1):
        tmp = MUL_PQ_P(c1, c2[i])
        tmp = MUL_Pxk_P(tmp, i)
        c = ADD_PP_P(c, tmp)
    return c


# P-9

# P-10

# P-11

# P-12

# P-13

