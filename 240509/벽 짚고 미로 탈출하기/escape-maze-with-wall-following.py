import sys 
n = int(input())
x, y = map(int, input().split())
x = x - 1
y = y - 1
arr = []
for _ in range(n):
    val = input()  # split()만 사용하여 리스트 생성
    arr.append(val)

# 미로 탈출이 불가능한지 여부를 판단하기 위해
# 동일한 위치에 동일한 방향으로 진행했던 적이 있는지를
# 표시해주는 배열입니다.

visited = [
    [
        [False for _ in range(4)]
        for _ in range(n + 1)
    ]
    for _ in range(n + 1)
]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

#벽이 있으면 이동이 불가하다
def wall_exist(x, y):
    return in_range(x,y) and arr[x][y] == '#'


count = 0
direction = 0


def checkCell(x, y, d):
    curX = x + dxs[d]
    curY = y + dys[d]

    if in_range(curX, curY) and arr[curX][curY] == '#':
        return True
    else:
        return False


while in_range(x,y):

    if visited[x][y][direction]:
        print(-1)
        sys.exit(0)

    visited[x][y][direction] = 1

    # 바라보고 있는 방향으로 이동이 가능한 경우
    curX = x+dxs[direction]
    curY = y+dys[direction]

    # 바라보고 있는 방향으로 이동하는 것이 불가능한 경우에는
    # 반 시계 방향으로 90' 방향을 바꿉니다.
    if wall_exist(curX, curY):
        direction = (direction -1+4)%4

    # Step2
    
    # Case1
    # 바라보고 있는 방향으로 이동하는 것이 가능한 경우 중
    # 바로 앞이 격자 밖이라면 탈출합니다.
    elif not in_range(curX, curY):
        x, y = curX, curY 
        count +=1

    # Case 2 & Case 3
    # 바로 앞이 격자 안에서 이동할 수 있는 곳이라면
    else:

        # 그 방향으로 이동했다 가정헀을 때 바로 오른쪽에 짚을 벽이 있는지 봅니다.
        rx = curX + dxs[(direction + 1) % 4]
        ry = curY + dys[(direction + 1) % 4]

        # Case2
        # 그대로 이동해도 바로 오른쪽에 짚을 벽이 있다면
        # 해당 방향으로 한 칸 이동합니다.
        if wall_exist(rx, ry):
            x, y = curX, curY
            count += 1
          # Case3
        # 그렇지 않다면 2칸 이동후 방향을 시계방향으로 90' 방향을 바꿉니다.
        else:
            x, y = rx, ry
            direction = (direction + 1) % 4
            count += 2
        

        


print(count)