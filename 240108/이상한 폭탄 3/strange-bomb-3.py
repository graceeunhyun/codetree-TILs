n, k = tuple(map(int, input().split()))
arr = []
for i in range (n):
    value = int(input())
    arr.append(value)

max_count = 0
max_num = 0

def findVal(i):
    curCount = 0
    num = i
    for j in range(i, n):
        if(arr[i] == arr[j] and j-i <= k ):
            curCount+=1
    
    #print(curCount, arr[i], max_count, max_num)
    if(curCount == 1):
        return 0, 0

    return curCount, arr[i];


for i in range (n):
    cur_count, cur_num = findVal(i)

    if cur_count > max_count:
        max_count = cur_count
        max_num = cur_num
    elif cur_count == max_count:
        max_num = max(max_num, cur_num)

print(max_num)