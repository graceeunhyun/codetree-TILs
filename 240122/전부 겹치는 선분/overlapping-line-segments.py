n = int(input())
arr = []
max_x1 = 0
min_x2 = float('inf')
for i in range (n):
    x1, x2 = tuple(map(int, input().split()))
    max_x1 = max(max_x1, x1)
    min_x2 = min(min_x2, x2)

if min_x2 > = max_x1:
    print("Yes")
else:
    print("No")