n, t = map(int, input().split())
arr = []
for i in range(2):
    row = list(map(int, input().split()))
    arr.append(row)
#print(arr)

def rearrange():
    first = arr[0][0]
    middle = arr[1][0]
    secondLast = arr[0][n-1]
    last = arr[1][n-1]


    for i in range(n-1, 0, -1):
        arr[0][i] = arr[0][i-1]
    

    for i in range(n-1, 0, -1):
        arr[1][i] = arr[1][i-1]
    

    arr[0][0] = last
    arr[1][0] = secondLast




for i in range(t):
    rearrange()

for i in range(2):
    for j in range(n):
        print(arr[i][j], end=" ")
    print("")