k, n = map(int, input().split())
arr = []
for i in range (k):
    value = list(map(int, input().split()))
    arr.append(value)

#print(arr)

count = 0

for a in range(n):
    for b in range (n):
        boolean = False
        for i in range (k):
            if(a!=b and arr[i][a] < arr[i][b]):
                boolean = True
        if boolean:
            count+=1
                
        
print(count//2)