n, m = tuple(map(int, input().split()))
grid = []
for i in range(n):
    val = list(map(int, input().split()))
    grid.append(val)


max_val = -20000

def find_value(x1, x2, y1, y2):
    curVal = 0 
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            curVal += grid[i][j]
    return curVal

for x1 in range(n):
    for x2 in range(x1, n):
        for y1 in range(m):
            for y2 in range(y1, m):
                for a1 in range(n):
                    for a2 in range(a1, n):
                        for b1 in range(m):
                            for b2 in range(b1, m):
                                if x2 < a1 or a2 < x1 or y2 < b1 or b2 < y1:  # 겹치지 않는 경우
                                    max_val = max(max_val, find_value(x1, x2, y1, y2) + find_value(a1, a2, b1, b2))

print(max_val)