K, N = tuple(map(int, input().split()))
arr_2d = [
    [0 for _ in range(N+1)]
    for _ in range(K)
]
for i in range(K):
    arr = list(map(int, input().split()))
    for j in range(len(arr)):
        arr_2d[i][arr[j]] = j

cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j: 
            continue
        boolean = True
        for k in range(K):
            if arr_2d[k][i] > arr_2d[k][j]:
                boolean = False
        if boolean:
            cnt += 1
print(cnt)