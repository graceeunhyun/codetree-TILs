n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    min = i
    for j in range(n):
        if(arr[j] > arr[min]):
            tmp = arr[min]
            arr[min] = arr[j]
            arr[j] = tmp


for i in range(n):
    print(arr[i], end=" ")