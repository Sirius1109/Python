def move(n,a='A',b='B',c='C'):
    if n == 1:
        print('move %s --> %s'%(a,c))
    elif n > 1:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)



