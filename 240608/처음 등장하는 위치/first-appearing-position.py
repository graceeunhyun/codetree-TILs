from sortedcontainers import SortedDict
n = int(input())
sd = SortedDict()

arr = list(map(int, input().split()))
for i in range(n):
    if not int(arr[i]) in sd:
        sd[int(arr[i])] = i+1


for key, value in sd.items():
    print(key, value)