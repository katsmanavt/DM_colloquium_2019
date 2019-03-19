from modules.classes import *
from modules.N import *
from modules.Z import *


# Q-1
def RED_Q_Q(q1):
    q = q1.copy()
    gcf = GCF_NN_N(ABS_Z_N(q.m), q.n)
    q.m = DIV_ZZ_Z(q.m, gcf)
    q.n = TRANS_Z_N(DIV_ZZ_Z(TRANS_N_Z(q.n), gcf))
    return q


# Q-2
def INT_Q_B(q):
    m = q.m.copy()
    n = q.n.copy()
    d = MOD_ZZ_Z(m, TRANS_N_Z(n))
    if d == 0:
        A = True
    else:
        A =  False
    return A

# Q=3
def TRANS_Z_Q(k):
    q = Rational()
    q.m = k.copy()
    q.n = Natural(0, 1)
    return q


# Q-4
def TRANS_Q_Z(q):
    q1 = RED_Q_Q(q)
    if q1.n == 1:
        p1 = q1.m
        return p1
    else:
        assert False
        

# Q-5
def ADD_QQ_Q(q1, q2):
    nok = LCM_NN_N(q1.n, q2.n)
    
    t = DIV_NN_N(nok, q1.n)
    t = TRANS_N_Z(t)
    p_1 = MUL_ZZ_Z(q1.m, t)
    
    t = DIV_NN_N(nok, q2.n)
    t - TRANS_N_Z(t)
    p_2 = MUL_ZZ_Z (q2.m, t)
    
    p_3 = ADD_ZZ_Z(p_1, p_2)
    
    q3 = Rational()
    q3.m = p_3
    q3.n = nok
    
    q3 = RED_Q_Q(q3)
    
    return q3


# Q-6

# Q-7

# Q-8
