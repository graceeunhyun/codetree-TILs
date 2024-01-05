n = int(input())
seats = list(map(int, input()))
#print(arr)

def find_min():
    dist = n
    for i in range(n):
        for j in range(i+1, n):
            if(seats[i] == 1 and seats[j]==1):
                dist = min(dist, j-i+1)
    
    return dist

ans = 0
for i in range(n):
    for j in range(i+1, n):
        if seats[i] == 0 and seats[j] == 0:
            seats[i] = 1
            seats[j] = 1

            ans = max(ans, find_min())
            seats[i] = 1 
            seats[j] = 1
    

print(ans)