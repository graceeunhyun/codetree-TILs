n, m = map(int, input().split())

#해당 값들은 정렬된 상태로 주어져서 sort() 의 동작이 필요하지 않음. 
arr = list(map(int, input().split()))

def lower_bound(target):
    left = 0
    right = n-1
    min_idx = n

    while left<=right:
        mid = (left+right)//2
        if arr[mid] >=target:
            min_idx = min(min_idx, mid)
            right = mid -1
        else:
            left = mid + 1
    return min_idx

def upper_bound(target):
    left = 0
    right = n-1
    min_idx = n

    while left<=right:
        mid = (left + right)//2
        if arr[mid] > target:
            min_idx = min(min_idx, mid)
            right = mid -1
        else:
            left = mid +1
   
    return min_idx

for i in range(m):
    val = int(input())
    print(upper_bound(val)-lower_bound(val))