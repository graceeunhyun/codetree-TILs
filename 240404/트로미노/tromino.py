n, m = tuple(map(int, input().split()))
arr = [] 
for i in range(n):
    val = list(map(int, input().split()))
    arr.append(val)
#print(arr)

max_val = 0 
for i in range(n):
    for j in range(m):
        val = 0 
        if(i+1<n and i+2<n):
            val = arr[i][j] +arr[i+1][j] + arr[i+2][j]
            max_val = max(val, max_val)
            
        if(j+1<m and j+2<m):
            val = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            max_val = max(val, max_val)
        
        if(j+1 < m and i+1<n):
            val = arr[i][j] + arr[i][j+1] + arr[i+1][j]
            max_val = max(val, max_val)
        
        if(j-1 >= 0 and j-1<m and i+1 >=0 and i+1 <n ):
            val = arr[i][j] + arr[i][j-1] + arr[i-1][j]
            max_val = max(val, max_val)

print(max_val)