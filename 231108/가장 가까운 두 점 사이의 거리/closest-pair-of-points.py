n = int(input())
arr = []
for i in range (n):
    value = list(map(int, input().split()))
    arr.append(value)

#print(arr)
ans = float('inf')
for i in range(n):
    for j in range(n):
        if(i==j):
            continue;
        x1, y1 = arr[i]
        x2, y2 = arr[j]

        height = (x1- x2)* (x1 -x2) + (y1 - y2)* (y1 -y2)

        ans = min(height, ans)

print(ans)