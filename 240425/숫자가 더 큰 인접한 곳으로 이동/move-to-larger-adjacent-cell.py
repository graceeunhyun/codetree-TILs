from collections import deque
n, r, c = map(int, input().split())
arr = []

for i in range(n):
    val = list(map(int, input().split()))
    arr.append(val)

r = r - 1
c = c - 1

visited = [[0 for _ in range(n)] for _ in range(n)]
dq = deque() 

max_x = r
max_y = c

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(x, y):
    global max_x, max_y, visited
    visited[x][y] = 1
    dq.append(arr[x][y])
    dxs, dys = [-1,1,0,0], [0,0,-1,1]
    priority = [4, 3, 2, 1]
    canMove = False

    for dx, dy, pr in zip(dxs, dys, priority):
        curx = x + dx
        cury = y + dy

        if in_range(curx, cury) and arr[curx][cury] > arr[max_x][max_y] and visited[curx][cury] == 0:
            #print(curx, cury, arr[curx][cury], arr[max_x][max_y])
            max_x, max_y = curx, cury
            canMove = True
            visited[curx][cury] = 1
            
            break

    if not canMove:
        return

    move(max_x, max_y)

# Start the DFS from the initial position (r, c)
move(r, c)

for item in dq:
    print(item, end=" ")