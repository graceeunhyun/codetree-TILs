n, m  = map(int, input().split())
arr= list(map(int, input().split()))
list = []

arr.sort()
def binarySearch(target):

    start = 0
    end = n-1
    idx = -1

    while start <= end:
        mid = (start+end)//2

        if arr[mid] == target:
            idx = mid
            break
        
        # 못 찾았을 경우 
        if arr[mid] > target:
            end = mid -1
        else:
            start = mid +1
    
    if idx != -1:
        print(idx+1)
    else:
        print(idx)



for i in range(m):
    val = int(input())
    binarySearch(val)


    #이분 탐색하는 로직 넣기