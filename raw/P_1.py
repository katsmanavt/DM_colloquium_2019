import classes
# import ADD_QQ_Q

def ADD_PP_P (c1, c2):
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
        i = i + 1
        
    c.m = m2
    return c