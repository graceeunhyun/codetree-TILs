n = int(input())
arr = []
for i in range(n):
    value = list(input().split())
    arr.append(value)

a = 0
b= 0

total= 0
winner = 0

for i in range(n):
    who, count = arr[i][0], (int)(arr[i][1])
    if(who == 'A'):
        a += count
    elif(who == 'B'):
        b+= count
    
    if( a > b ):
        if( winner != 'A'):
            total+=1
            winner = 'A'
    elif(b > a):
        if( winner!= 'B'):
            total+=1
            winner ='B'
    else:
        total+=1
        winner ='AB'

    #print(a, b, winner, total)

print(total)