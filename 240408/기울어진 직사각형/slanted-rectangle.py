n = int(input())
arr = []
for i in range(n):
    val = list(map(int, input().split()))
    arr.append(val)

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n

max_sum = 0
grid = [(1, -1), (-1, -1), (-1, 1), (1, 1)]

def find_score(x, y, k, l):
    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    move_nums = [k, l, k, l]
    sum_of_nums = 0
    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            x = x+dx
            y = y+dy

            if not is_valid(x, y):
             return 0
            sum_of_nums +=arr[x][y]
    
    return sum_of_nums



for i in range(n):
    for j in range(n):
        
        for width in range(1, n+1):
            for height in range(1, n+1):
                max_sum = max(max_sum, find_score(i, j, width, height))

            

print(max_sum)  # Printing