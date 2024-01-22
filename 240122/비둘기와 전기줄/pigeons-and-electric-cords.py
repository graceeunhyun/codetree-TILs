n = int(input())
arr = []
#1번부터 10번까지의 비둘기 번호 
num = [-1]*11
for i in range(n):
    val = list(map(int, input().split()))
    arr.append(val)
    
count = 0
for i in range(n):
    pigeon, loc = arr[i]
    if(num[pigeon] != loc):
        if(num[pigeon] != -1):
            count+=1
        
        num[pigeon] = loc

print(count)