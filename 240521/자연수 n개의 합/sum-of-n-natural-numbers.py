s = int(input())

# 하나하나 더해서 구하면 메모리적 이슈가 발생하므로
# 이를 이진탐색으로 구한다

start = 1
end = s
max_num = 1


while start <= end:
    mid = (start+end)//2

    if mid*(mid+1)//2 <= s:
        start = mid+1
        max_num = max(max_num, mid)
    else:
        end = mid -1


print(max_num)