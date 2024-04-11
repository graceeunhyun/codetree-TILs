n, t = tuple(map(int, input().split()))
arr = [] 
for i in range(3):
    row = list(map(int, input().split()))
    arr.append(row)

def rearrange():
    frLast = arr[0][n-1]
    srLast = arr[1][n-1]
    trLast = arr[2][n-1]

    for i in range(n-1, 0, -1):
        arr[0][i] = arr[0][i-1]
        arr[1][i] = arr[1][i-1]
        arr[2][i] = arr[2][i-1]
    

    arr[0][0] = trLast
    arr[1][0] = frLast
    arr[2][0] = srLast


for i in range(t):
    rearrange()


for i in range(3):
    for j in range(n):
        print(arr[i][j], end=" ")
    
    print("")