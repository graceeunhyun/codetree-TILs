from collections import deque

def bfs(arr, start, end):
    arr_dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    visited = [[False] * 10 for _ in range(10)]
    queue = deque([(start[0], start[1], 0)])  # (x, y, distance)

    while queue:
        x, y, dist = queue.popleft()

        if (x, y) == end:
            return dist-1

        for i, j in arr_dir:
            new_x, new_y = x + i, y + j

            if 0 <= new_x < 10 and 0 <= new_y < 10 and not visited[new_x][new_y] and arr[new_x][new_y] != 'R':
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, dist + 1))

    return -1

def find_shortest_distance(arr):
    loc_L = loc_B = None

    for i in range(10):
        for j in range(10):
            if arr[i][j] == 'L':
                loc_L = (i, j)
            elif arr[i][j] == 'B':
                loc_B = (i, j)

    distance_to_B = bfs(arr, loc_L, loc_B)

    return distance_to_B

# 입력 받기
arr = [list(input()) for _ in range(10)]

# 결과 출력
result = find_shortest_distance(arr)
print(result)