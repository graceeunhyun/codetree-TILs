n = int(input())
x, y = map(int, input().split())

arr = [] 
for i in range(n):
    val = list(input().split())
    arr.append(val)

visited = [[0 for _ in range(n)] for _ in range(n)]

dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]


def in_range(x,y):
    return 0<=x<n and 0<=y<n

def checkCell(x, y, d):
    curX = x + dxs[d]
    curY = y + dys[d]
    
    print(curX, curY)
    if not in_range(curX, curY):
        return False

    if arr[curX][curY] == '#':
        return True
    
    return False


count = 0 
direction = 0 # 0은 오른, 1은 상 , 2는 왼, 3은 다운 
#아 오른쪽에 벽이 있을 경우만 이동 가능~ 
x= x-1
y = y-1
while True:
    if not in_range(x, y) or visited[x][y] == 1:
        break
    
    visited[x][y] = 1

    if checkCell(x, y, direction):
        direction = (direction + 1) % 4
    else:
        x += dxs[direction]
        y += dys[direction]
        count += 1



print(count)