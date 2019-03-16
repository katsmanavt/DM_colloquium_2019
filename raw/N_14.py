# Гусев
import classes
#import GCF_NN_N
#import  MUL_NN_N
#import DIV_NN_N

def LCM_NN_N(a, b):
    return DIV_NN_N(MUL_NN_N(a, b), GCF_NN_N(a, b))