n, m = map(int, input().split())
# n 개의 숫자가 
arr = list(map(int, input().split()))
question = list(map(int, input().split()))

def lower_bound(target):
    left = 0
    right = n-1
    min_idx = n

    while left<=right:
        mid= (left+right)//2
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
        mid = (left+right)//2
        if arr[mid] > target:
            min_idx = min(min_idx, mid)
            right = mid-1
        else:
            left = mid +1
    
    return min_idx


for i in range(m):
    val = question[i]
    #upper bound 에서 lower bound 를 빼서 구하고 그런 숫자가 등장한 적이 없으면 -1 를 출력
    upperVal = upper_bound(val)
    lowerVal = lower_bound(val)
    # upper bound - lower bound 뺀 값이 같으면 -1 출력한다. 
    if upperVal - lowerVal == 0:
        print(-1)
    else:
        print(lowerVal+1)