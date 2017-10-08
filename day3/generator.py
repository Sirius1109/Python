##def triangles():
##    L = [1]
##    while True:
##        yield L
##        for i in range(1,len(L)):
##            L[i] = pre[i] + pre[i-1]
##        L.append(1)
##        pre = L[:]
##

def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i] + L[i-1] for i in range(len(L))]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
