n, m = tuple(map(int, input().split()))
grid = []
for i in range(n):
    val = list(map(int, input().split()))
    grid.append(val)

def find_thisIsPos(x1, x2, y1, y2):
    for i in range(x1, x2+1):
        for j in range(y2, y2+1):
            if(grid[i][j] <0 ):
                return False
    

    return True

max_val = 0

for i in range(n):
    for j in range(m):
        for i2 in range(i, n):
            for j2 in range(j, m):
                if find_thisIsPos(i, i2, j, j2):
                    max_val = max(max_val, ((i2-i+1)*(j2-j+1)))

print(max_val)