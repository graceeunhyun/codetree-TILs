n = int(input())
arr = list(map(int, input()))

#아래는 어떻게 이제 minDist를 구할 수 있는지 
def min_dist():
    dist = n

    for i in range(n):
        for j in range(i+1, n):
            if(arr[i] == 1 and arr[j] == 1):
                dist = min(dist, j-i)
    
    return dist

ans = 0 
for i in range(n):
    if arr[i] == 0:
        arr[i] = 1
        ans = max(min_dist(), ans)
        arr[i] = 0

print(ans)