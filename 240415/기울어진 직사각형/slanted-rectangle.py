n = int(input())
grid = []
for i in range(n):
    val = list(map(int, input().split()))
    grid.append(val)

max_val = 0

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

def findMaxVal(x, y, k, l):
    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    move_nums = [k, l, k, l]

    val = 0
    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):  # k 또는 l 번 이동
            x = dx+x
            y = dy+y
            if not in_range(x,y):
                return 0
            
            val+=grid[x][y]
            
    return val

for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                max_val = max(max_val, findMaxVal(i, j, k, l))

print(max_val)