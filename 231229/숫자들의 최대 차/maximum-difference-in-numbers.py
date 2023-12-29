n, k = tuple(map(int, input().split()))
arr = [int(input()) for _ in range(n)]

maxcount = 0 

#최대, 최소를 먼저 정하고 그다음에 고를 수 있는 원소의 개수 
for i in range(1, 10001):
    for j in range(i, 10001):
        if i==j or j -i > k:
            continue
        
        count = 0
        for elem in arr:
            if i<= elem <= j:
                count+=1
        
        maxcount = max(maxcount, count)

print(maxcount)