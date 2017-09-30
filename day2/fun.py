import math

def quadratic(a,b,c):
    for i in (a,b,c):
        if not isinstance(i,(int,float)):
            raise TypeError('bad operand type')
    if b*b < 4*a*c or a == 0:
        raise TypeError('参数错误')
    elif b*b == 4*a*c:
        return (-b/a*0.5)
    else:
        return (((-b + math.sqrt(b*b - 4*a*c))/(2*a)),((-b + math.sqrt(b*b - 4*a*c))/(2*a)))


print(quadratic(1,4,2))
