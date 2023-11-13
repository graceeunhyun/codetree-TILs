# 입력
n = int(input())
arr = []
for i in range(n):
    value = list(map(int, input().split()))
    arr.append(value)

count = 0

# 선분들을 순회하며 겹치지 않는 선분의 수 계산
for i in range(n):
    overlap = False
    for j in range(n):
        if j == i:
            continue
        
        if((arr[i][0]<= arr[j][0] and arr[i][1]>= arr[j][1]) or (arr[i][0] >= arr[j][0] and arr[i][1] <= arr[j][1])):
            overlap = True
            break
        
    if overlap == True:
        count+=1

print(count)