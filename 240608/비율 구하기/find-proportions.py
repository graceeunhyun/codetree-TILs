#알파벳 전체 문자열 중 어느 정도 비율을 차지하는지
from sortedcontainers import SortedDict

n = int(input())
sd = SortedDict()
for i in range(n):
    val = input()
    if val in sd:
        sd[val] +=1
    
    else:
        sd[val] =1

total=0
for key, value in sd.items():
    total+=value

for key, value in sd.items():
    print(key,format((value/total)*100, ".4f"))