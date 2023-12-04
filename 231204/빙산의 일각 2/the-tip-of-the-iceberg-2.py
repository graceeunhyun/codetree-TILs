n = int(input())
arr = []

for i in range (n):
    arr.append(int(input()))


#print(arr)
result = 0 
for j in range(min(arr), max(arr)):
    height = 0 
    for i in range (n):
        if ( arr[i] - j > 0):
            if(i+1 < n and arr[i+1] -j >0):
                continue
            else :
                height +=1
        
        #print(height)
    
    result = max(result, height)
                


print(result)