n = int(input())
x, y = map(int, input().split())
x = x-1
y = y-1
arr = [] 
for _ in range(n):
    val = input()  # split()만 사용하여 리스트 생성
    arr.append(val)


visited = [[0 for _ in range(n)] for _ in range(n)]

dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]

def in_range(x, y):

    return 0 <= x < n and 0 <= y < n

count = 0 
direction = 0

def checkCell(x, y, d):
    global count
    curX = x + dxs[d]
    curY = y + dys[d]

    if not in_range(curX, curY):
        return False
    if arr[curX][curY] == '#':

        return True
    else:
        count+=1
        return False



while True:
    if not in_range(x, y) or visited[x][y] == 1:
        break
    
    visited[x][y] = 1

    if checkCell(x, y, direction):
        direction = (direction + 1) % 4
        
    x += dxs[direction]
    y += dys[direction]
    count += 1

print(count)