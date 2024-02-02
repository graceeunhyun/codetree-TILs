n = int(input())
arr = input().split()
#print(arr)
sorted_arr = sorted(arr)
#print(sorted_arr)

swap_count = 0
for i in range(n):
    while arr[i]!=sorted_arr[i]:
        j = arr.index(sorted_arr[i])
        if( abs(i-j) == 1):
            arr[i], arr[j] = arr[j], arr[i]
            swap_count+=1

print(swap_count)