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
        x1, y1 = arr[i]
        x2, y2 = arr[j]
        if((x1<=x2 and y1>= y2) or (x1 >= x2 and y1 <= y2)):
            overlap = True
            break
        
    if overlap == False:
        count+=1

print(count)