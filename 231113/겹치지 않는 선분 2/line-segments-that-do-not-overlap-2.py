n = int(input())
arr = []
for i in range (n):
    value = list(map(int, input().split()))
    arr.append(value)

#print(arr)
#선분을 x2 값으로 정렬
arr.sort(key=lambda value:value[1])

count = 0
current_end = -float('inf')

for a in arr:
    x1, x2 = a
    if x1 > current_end:
        count +=1
        current_end = x2


print(count)