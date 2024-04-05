n, m = map(int, input().split())

grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

def count_happy_sequences(arr, m):
    count = 0
    for row in arr:
        consecutive = 1
        for i in range(1, len(row)):
            if row[i] == row[i - 1]:
                consecutive += 1
            
        if consecutive >= m:
            count += 1
    return count

count = count_happy_sequences(grid, m)

# 열의 수열을 행렬로 변환하여 다시 계산
transposed_grid = list(zip(*grid))
count += count_happy_sequences(transposed_grid, m)

print(count)