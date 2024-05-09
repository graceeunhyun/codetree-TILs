import sys 

n = int(input())
x, y = map(int, input().split())
x -= 1
y -= 1
arr = []
for _ in range(n):
    val = input()  
    arr.append(val)

visited = [[[False for _ in range(4)] for _ in range(n)] for _ in range(n)]
dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def wall_exist(x, y):
    return in_range(x, y) and arr[x][y] == '#'

count = 0
direction = 0

while in_range(x, y):

    if visited[x][y][direction]:
        print(-1)
        sys.exit(0)

    visited[x][y][direction] = True

    curX = x + dxs[direction]
    curY = y + dys[direction]

    if wall_exist(curX, curY):
        direction = (direction + 1) % 4

    elif not in_range(curX, curY):
        x, y = curX, curY 
        count += 1

    else:
        rx = curX + dxs[(direction - 1) % 4]
        ry = curY + dys[(direction - 1) % 4]

        if wall_exist(rx, ry):
            x, y = curX, curY
            count += 1
        else:
            x, y = rx, ry
            direction = (direction - 1) % 4
            count += 2

print(count)