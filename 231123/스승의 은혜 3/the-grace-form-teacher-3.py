n, b = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for i in range(n)]

maxcount = 0
#최대명수니깐 sorted를 사용해서 이제 오름차순으로 정리한다. 
sorted(arr)
#print(arr)

for i in range(n):
    amount = 0
    count = 0

    for j in range(n):
        if i == j:
            amount +=(arr[j][0]/2) + arr[j][1]
        
        else:
            amount += arr[j][0] + arr[j][1]
        
        if (b >= amount):
             count+=1
        else:
            break
    
    maxcount = max(maxcount, count)


print(maxcount)