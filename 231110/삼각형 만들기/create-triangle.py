n = int(input())
arr = []
for i in range (n):
    str_val = list(map(int, input().split()))
    arr.append(str_val)


#print(arr)
max_val = float('-inf') 
for i in range(n-2):
    for j in range(i+1, n):
        for k in range(j+1, n):
            size = 0 
            x1, y1 = arr[i]
            x2, y2 = arr[j]
            x3, y3 = arr[k]

            if((x1 == x2 or x2 ==x3 or x3 ==x1) and (y1 ==y2 or y2 ==y3 or y3 ==y1) ):
                size = (1/2)*abs((x1*y2 + x2*y3 + x3*y1) - (x2*y1 + x3*y2 + x1*y3))


            max_val = max(max_val, size)

print((int)(max_val*2))