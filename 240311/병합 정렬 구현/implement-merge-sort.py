# Function to perform merge sort
def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2  # Use integer division to get the midpoint
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

# Function to merge two halves of an array
def merge(arr, low, mid, high):
    i = low
    j = mid + 1
    k = low

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            merged_arr[k] = arr[i]
            i += 1
        else:
            merged_arr[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        merged_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= high:
        merged_arr[k] = arr[j]
        j += 1
        k += 1
    
    for k in range(low, high+1):
        arr[k] = merged_arr[k]
    

# Input
n = int(input())
arr = list(map(int, input().split()))

# Initialize merged_arr as an empty list
merged_arr = [0] * n

# Perform merge sort
merge_sort(arr, 0, n - 1)

# Print the sorted array
for i in range(n):
    print(merged_arr[i], end=" ")