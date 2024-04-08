n = int(input())
arr = []
for i in range(n):
    val = list(map(int, input().split()))
    arr.append(val)

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n

max_sum = 0
grid = [(1, -1), (-1, -1), (-1, 1), (1, 1)]
for i in range(n):
    for j in range(n):
        for dx, dy in grid:
            x, y = i, j 
            cur_sum = arr[x][y]

            for k in range(1, n):
                for step in range(k):
                    x += dx
                    y += dy  # Fixing typo here

                    # 격자 내에 있는 것 확인
                    if is_valid(x, y):
                        cur_sum += arr[x][y]
                        print(arr[x][y], x, y, cur_sum)
                    else:
                        break

                max_sum = max(max_sum, cur_sum) 

print(max_sum)  # Printing max_sum instead of cur_sum