n= int(input())
arr = list(map(int, input().split()))
#print(arr)
min_diff = float('inf')
for i in range(n):
    arr[i] *=2

    for j in range (n):
        remain_arr = []
        for k in range(n):
            if k!=j:
                remain_arr.append(arr[k])

        sum_diff = 0
        for k in range(n - 2):
            sum_diff += abs(remain_arr[k + 1] - remain_arr[k])

        min_diff = min(min_diff, sum_diff)


    arr[i] //=2


print(min_diff)