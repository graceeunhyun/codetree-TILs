n = int(input())
arr = [int(input()) for _ in range(n)]

def findVal(i):
    
    cal = 0
    for j in range(n):
        if(arr[j] < i):
            cal += (i - arr[j]) * (i - arr[j])
        elif(arr[j] > i+17):
            cal += (arr[j] - (i+17)) * (arr[j] - (i+17))
        else:
            continue
        
       #print(j, i, arr[j], cal)

    return cal

max_cal = float('inf')
for i in range(1, 84):
    max_cal = min(max_cal, findVal(i))

print(max_cal);