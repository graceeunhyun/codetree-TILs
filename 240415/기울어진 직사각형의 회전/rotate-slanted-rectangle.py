def rotate_diamond(x, y, m1, m2, m3, m4, clockwise, grid):
    temp = grid[x][y]
    n = len(grid)

    # 회전 방향에 따라 각 방향의 순서를 조정
    directions = [(1, -1), (-1,-1), (-1, +1), (+1, +1)] if clockwise else [(1, 1), (-1, 1), (-1, -1), (1, -1)]

    # 좌상
    for i in range(m1):
        dx, dy = directions[0]
        temp, grid[x+dx*i][y+dy*i] = grid[x+dx*i][y+dy*i], temp
    
    # 우상
    for i in range(m2):
        dx, dy = directions[1]
        temp, grid[x+dx*i][y+dy*i] = grid[x+dx*i][y+dy*i], temp
    
    # 우하
    for i in range(m3):
        dx, dy = directions[2]
        temp, grid[x+dx*i][y+dy*i] = grid[x+dx*i][y+dy*i], temp
    
    # 좌하
    for i in range(m4):
        dx, dy = directions[3]
        temp, grid[x+dx*i][y+dy*i] = grid[x+dx*i][y+dy*i], temp
    
    return grid

# 격자 크기 입력 받기
n = int(input())

# 격자 정보 입력 받기
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# 기울어진 직사각형 정보 입력 받기
r, c, m1, m2, m3, m4, direction = map(int, input().split())

# 회전 방향 설정
clockwise = True if direction == 0 else False

# 마름모 모양으로 회전
grid = rotate_diamond(r-1, c-1, m1, m2, m3, m4, clockwise, grid)

# 결과 출력
for row in grid:
    print(" ".join(map(str, row)))