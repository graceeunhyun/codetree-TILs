n, k = map(int, input().split())
# n 개의 정수가 입력으로 주어지고 이중 서로 다른 위치에 있는 두 개의 수를 뽑아 더했을 때 

arr = list(map(int, input().split()))
arr.sort()
find = {}

# 두 개의 수를 골랐을 때 : 두 수의 합이 : k 
# 4 --- 5
# 6 --- 3
# n ---- k-n

# 빈도수를 딕셔너리에 저장
for i in range(n):
    elem = arr[i]
    find[elem] = find.get(elem,0)+1

# 각 정수에 대해 조합을 확인해서 목표값과 일치하는 수를 누적 
count = 0
for num in arr:
    complement = k -num
    if complement in find:
        count+=find[complement]
    
    if complement == num:
        count-=1

print(count //2)