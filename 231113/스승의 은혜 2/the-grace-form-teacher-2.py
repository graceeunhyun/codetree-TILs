n, b = map(int, input().split())
p = []
#print(n, b)
for i in range(n):
    value = int(input())
    if( value %2 ==0):
        p.append(value)

maxcount = 0
for i in range(n):
    amount = 0
    count = 0 
    for j in range(n):
        if i == j:
            amount += (p[j]/2)
        else:
            amount+= p[j]
    
        if( b >= amount):
            count+=1
    
    maxcount = max(maxcount, count)

print(maxcount)