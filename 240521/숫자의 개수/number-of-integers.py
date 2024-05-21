n, m = map(int, input().split())
arr = list(map(int, input().split()))

def findBinary(val):
    start = 0 
    end = n-1
    idx = 0
    max_idx = 0
    min_idx = n

    while start <=end:
        mid = (left + right)//2
        if arr[mid] >= val:
            max_idx = max(max_idx, mid)
            right = mid-1
        else:
            left = mid+1
            



for i in range(m):
    val = int(input())
    findBinary(val)