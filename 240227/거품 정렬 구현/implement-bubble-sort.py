n = int(input())
arr= list(map(int, input().split()))

sorted_val = False
while not sorted_val: 
    sorted_val = True
    for i in range(n-1):
        if (arr[i] > arr[i+1]):
            tmp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1] = tmp
            sorted_val = False

for i in range(n):
    print(arr[i], end=" ")