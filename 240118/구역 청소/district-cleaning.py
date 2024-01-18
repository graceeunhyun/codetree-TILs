a, b = map(int, input().split())
c, d= map(int, input().split())

num = 0
if ( (b< c and a< c) or ( d< a and c < a) ):
    num = (b-a) + (d-c)
else:
    if ( b> c and b< d ):
        num = (d - a) - (b -c)
    elif ( d > a and d < b):
        num = (b - c) - (a - d)
    elif ( d > b and a > c):
        num = d- c
    else:
        num = b- a

print(num-1)