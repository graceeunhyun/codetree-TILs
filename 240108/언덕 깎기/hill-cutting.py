n = int(input())
arr = [int(input()) for _ in range(n)]
k= 17

def findVal(i):
    
    cal = 0
    for j in range(n):
        if(arr[j] < i):
            cal += (i - arr[j]) * (i - arr[j])
        elif(arr[j] > i+k):
            cal += (arr[j] - (i+k)) * (arr[j] - (i+k))
        else:
            continue
        
       #print(j, i, arr[j], cal)

    return cal

ans = float('inf')
for i in range(1, 84):
    ans = min(ans, findVal(i))

print(ans);