n, m, q = map(int, input().split())
arr = []
for i in range(n):
    val = list(map(int, input().split()))
    arr.append(val)

wind = []

visited=[False]*n

for i in range(q):
    val = list(input().split())
    wind.append(val)

def findSameNum(row, diff):
    if diff < 0 or diff >= n:
        return False

    for i in range(m):
        if arr[row][i] == arr[diff][i]:
            return True

    return False

def rearrangeLeft(row):
    if row < 0 or row >= n or visited[row]:
        return
    
    visited[row] = True

    temp = arr[row][m-1]
    for i in range(m-1, 0, -1):
        arr[row][i] = arr[row][i-1]
    
    arr[row][0] = temp
    
    if findSameNum(row, row-1):
        rearrangeRight(row-1)
    if findSameNum(row, row+1):
        rearrangeRight(row+1)

def rearrangeRight(row):
    if row < 0 or row >= n or visited[row]:
        return
    
    visited[row] = True
    
    temp = arr[row][0]
    for i in range(1, m):
        arr[row][i-1] = arr[row][i]
    
    arr[row][m-1] = temp

    if findSameNum(row, row-1):
        rearrangeLeft(row-1)
    if findSameNum(row, row+1):
        rearrangeLeft(row+1)

for i in range(q):
    row, direction = wind[i]
    if direction == 'L':
        rearrangeLeft(int(row)-1)
    else:
        rearrangeRight(int(row)-1)

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print(" ")