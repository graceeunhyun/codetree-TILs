x, y = tuple(map(int, input().split()))

count = 0

def checkNum(num):
    flag = False;

    sameval = num %10 
    while num>0:
        digit = num %10
        if digit == sameval:
            flag = True
        num //=10
    
    return flag


for i in range(x, y+1):
    if checkNum(i):
        count+=1

print((int)(count/2)+1)