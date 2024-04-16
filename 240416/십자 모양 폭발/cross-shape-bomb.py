n = int(input())
arr = [] 
for i in range(n):
    val = list(map(int, input().split()))
    arr.append(val)

r, c = map(int, input().split())

# 우선 터지게 만들고
number = arr[r-1][c-1]

def explode(x, y, number):
    dxs, dys = [0, 0, 1, -1], [-1, 1, 0, 0]
    movenum = number
    arr[x][y] = 0
    for dx, dy in zip(dxs, dys):
        for i in range(movenum):
            nx = x + dx*i
            ny = y + dy*i
            if 0 <= nx < n and 0 <= ny < n:
                arr[nx][ny] = 0
    
    # 배열 재정렬
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        count = n - 1
        for i in range(n - 1, -1, -1):
            if arr[i][j] != 0:
                temp[count][j] = arr[i][j]
                count -= 1
    return temp

# 배열 재정렬된 결과를 출력
result = explode(r - 1, c - 1, number)
for row in result:
    print(' '.join(map(str, row)))