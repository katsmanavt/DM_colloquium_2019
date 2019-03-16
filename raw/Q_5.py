import classes
"""
import LCM_NN_N
import DIV_NN_N
import TRANS_N_Z
import MUL_ZZ_Z
import ADD_ZZ_Z
import RED_Q_Q
"""


def ADD_QQ_Q(q1, q2):
    NOK = LCM_NN_N(q1.n.copy(), q2.n.copy())
    
    t = DIV_NN_N(NOK.copy(), q1.n.copy())
    t = TRANS_N_Z(t)
    p_1 = MUL_ZZ_Z(q1.m.copy(), t)
    
    t = DIV_NN_N(NOK.copy(), q2.n)
    t = TRANS_N_Z(t)
    p_2 = MUL_ZZ_Z(q2.m, t)
    
    p_3 = ADD_ZZ_Z(p_1, p_2)
    
    q3 = Rational()
    q3.m = p_3
    q3.n = NOK
    
    RED_Q_Q(q3)
    
    return q3