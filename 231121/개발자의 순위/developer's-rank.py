k, n = map(int, input().split())
arr = []
for i in range (k):
    value = list(map(int, input().split()))
    arr.append(value)

#print(arr)

count = 0
for i in range (k):
    for a in range(k):
        for b in range (k):
            if(a!=b and arr[i][a] < arr[i][b]):
                count +=1
        
print(count//2)