n = int(input())
arr = [] 
for i in range(n):
    val = list(map(int, input().split()))
    arr.append(val)

#print(arr)
max_val = 0

for value in range (1, 4):
    # 처음 의 위치의 조약돌 -- 1, 2, 3
    count = 0 
    cur = value
    for i in range (n):
        a, b, c = arr[i]
        a, b = b, a
        #print(a, b, c)

        if(cur ==a ):
            cur = b
        elif(cur == b):
            cur = a

        if ( cur == c ):
            count +=1
             

    max_val = max(max_val, count)        

print(max_val)