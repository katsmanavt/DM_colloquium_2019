import classes
"""
import DIV_PP_P
import MUL_PP_P
import SUB_PP_P
"""

def MOD_PP_P(c1, c2):
    if (c1.m < c2.m):
        r = c1
    else:
        q = DIV_PP_P(c1, c2)
        c3 = MUL_PP_P(c2, q)
        r = SUB_PP_P(c1, c3)
    return r
