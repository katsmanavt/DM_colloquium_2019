# Волконенков С.С.

import classes


def TRANS_Z_N (x):
    ans = None
    if x.b == 0:
        ans = Natural(x.n, *[x[i] for i in range(x.n)])
    return ans
