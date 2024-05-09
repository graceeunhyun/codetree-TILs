n = int(input())
x, y = map(int, input().split())
x -= 1
y -= 1
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
    curX = x + dxs[d]
    curY = y + dys[d]

    if in_range(curX, curY) and arr[curX][curY] == '#':
        return True
    else:
        return False


while True:
    if not in_range(x, y) or visited[x][y] == 1:
        break

    visited[x][y] = 1

    # 바라보고 있는 방향으로 이동이 가능한 경우
    if checkCell(x, y, direction):
        x += dxs[direction]
        y += dys[direction]
        count += 1
    else:
        # 현재 방향으로 이동이 불가능할 때, 왼쪽으로 회전하여 시도
        direction = (direction - 1) % 4
        x += dxs[direction]
        y += dys[direction]
        count += 1

print(count)