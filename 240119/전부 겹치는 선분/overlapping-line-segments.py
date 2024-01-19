n = int(input())
arr = []
for i in range (n):
    value = list(map(int, input().split()))
    arr.append(value)

arr.sort()
for i in range(1, n):
    if arr[i][0] >= arr[i-1][1]:
        print("No")
        break
    else:
        print("Yes")
        break