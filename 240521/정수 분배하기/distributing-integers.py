n, m = map(int, input().split())
# n 개의 정수를 분배해서 
# k 의 최대값 
arr = []

for i in range(n):
    val = int(input())
    arr.append (val)

start = 1
end = min(arr)
max_val = 0

# 만들 수 있는 k 값의 
def is_possible(target):

    count = 0
    #target 이 인제 k 이고 같은 크기의 정수를 m 개 이상 만들어야한다. 
    for elem in arr:

        # 아예 그 target 보다 작다면 해당 값은 false 입니다. 

        val = (int)(elem // target)
        count +=val
    
    return count >=m



while start<=end:
    mid = (start+end)//2

    #해당 부분이 가능한지, 그리고 그 답의 최대값을 저장
    if is_possible(mid):
        max_val = max(max_val, mid)
        start = mid+1
    else:
        end = mid-1

print(max_val)