n = int(input())
arr = []
for i in range(n):
    value= list(map(int, input().split()))
    arr.append(value)



boolVal = False
for i in range(n):
    max_x1 = 0
    min_x2 = float('inf')

    for j in range(n):

        if(i == j):
            continue
        x1, x2 = arr[j]
        max_x1 = max(max_x1, x1)
        min_x2 = min(min_x2, x2)

    
    if(min_x2 >= max_x1):
        boolVal= True
        break;

if(boolVal):
    print("Yes")
else:
    print("No")