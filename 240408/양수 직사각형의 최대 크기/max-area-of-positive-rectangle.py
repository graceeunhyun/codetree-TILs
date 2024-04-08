n, m = tuple(map(int, input().split()))
grid = []
for i in range(n):
    val = list(map(int, input().split()))
    grid.append(val)

def find_thisIsPos(x1, x2, y1, y2):
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            if grid[i][j] <= 0:
                return False
    return True

max_val = 0

for i in range(n):
    for j in range(m):
        for i2 in range(i, n):  # 수정: 변수 i1을 i로 수정
            for j2 in range(j, m):  # 수정: 변수 j2를 j로 수정
                if find_thisIsPos(i, i2, j, j2):
                    max_val = max(max_val, ((i2-i+1)*(j2-j+1)))  # 수정: 직사각형의 넓이 계산 수정

print(max_val)