def find_min_x(n, ranges, x):

    first = x

    for i in range(n):
        a, b = ranges[i]

        x *= 2

        #현재 범위에 맞게 x 를 조정
        if x < a or x > b:
            return float('inf')

    return first


n = int(input())
ranges = []
for i in range (n):
    value = list(map(int, input().split()))
    ranges.append(value)

#print(ranges)

result = float('inf')

for j in range(10001):
    result = min(find_min_x(n, ranges, j), result)

print(result)