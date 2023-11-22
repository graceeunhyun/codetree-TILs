k, n = tuple(map(int, input().split()))
arr = []
for i in range (k):
    value = list(map(int, input().split()))
    arr.append(value)

#print(arr)

count = 0

for a in range(n):
    for b in range (n):
        if(a == b):
            continue
        boolean = True
        for i in range (k):
            if(arr[i][a] >= arr[i][b]):
                boolean = False
                break;

        if boolean:
            count+=1
                
        
print(count)