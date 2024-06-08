n = int(input())
arr = list(map(int, input().split()))
set1 = set(arr)
count = 0
for i in set1:
    count+=1
print(count)