from sortedcontainers import SortedDict
# 단어장 
n = int(input())
sd = SortedDict()
for i in range(n):
    val = input()
    if val in sd:
        sd[val] +=1
    else:
        sd[val] = 1

for key, value in sd.items():
    print(key,value)