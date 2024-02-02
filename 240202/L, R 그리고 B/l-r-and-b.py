from queue import Queue

def bfs(arr, start, end):
    n = len(arr)
    visited = [[False] * n for _ in range(n)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = Queue()
    queue.put((start, 0))  # Distance is included in the tuple

    while not queue.empty():
        current, dist = queue.get()
        i, j = current

        if (i, j) == end:
            return dist

        for di, dj in directions:
            ni, nj = i + di, j + dj

            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and arr[ni][nj] == '.' and arr[ni][nj] != 'R':
                visited[ni][nj] = True
                queue.put(((ni, nj), dist + 1))

    return float('inf')  # If there is no path

def find_shortest_distance(arr):
    n = len(arr)

    loc_L = None
    loc_R = None
    loc_B = None

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'L':
                loc_L = (i, j)
            elif arr[i][j] == 'R':
                loc_R = (i, j)
            elif arr[i][j] == 'B':
                loc_B = (i, j)

    if loc_L is None or loc_R is None or loc_B is None:
        return -1  # Invalid input

    distance_to_B = bfs(arr, loc_L, loc_B)


    if distance_to_B == float('inf'):
        return -1  # No valid path

    return distance_to_B

# 입력 받기
arr = [input() for _ in range(10)]

# 결과 출력
result = find_shortest_distance(arr)
print(result)