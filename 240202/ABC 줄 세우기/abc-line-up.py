n = int(input())
arr = input().split()
#print(arr)
sorted_arr = sorted(arr)
#print(sorted_arr)

swap_count = 0
for i in range(n):
    if(arr[i] != sorted_arr):
        
        if(i < n-1): 
            j = i+1 
        else:
            j = i-1 
            
        arr[i], arr[j] == arr[j], arr[i]
        swap_count +=1

print(swap_count)