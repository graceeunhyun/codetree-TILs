n, m = tuple(map(int, input().split()))

arr = []
for i in range(m):
    value = list(map(int, input().split()))
    arr.append(value)

# 1이상 n 이하의 자연수니 거기서 이제 뽑혀진 count 를 셀 수 있도록 
# 경우의 수를 센다 
maxcount = 0
for i in range (1, n+1):
    for j in range (i+1, n+1):
        count = 0
        
        if i==j:
            continue

        for a, b in (arr):
            if (a == i and b == j) or (a == j and b ==i):
                #print(a, b, i, j)
                count+=1
        
        maxcount = max(maxcount, count)

print(maxcount)