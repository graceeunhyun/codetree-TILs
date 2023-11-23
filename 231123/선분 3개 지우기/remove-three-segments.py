n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
#print(arr)

count = 0
for i in range (n):
    for j in range(i+1, n):
        for k in range(j+1, n):

            if (i == j or j == k or i == k):
                continue
            
            boolean = True;
            visit = [0]*101
            for s in range(n):
                if(s == i or s==j or s ==k ):
                    continue

                a,b = arr[s]
                for m in range(a, b+1):
                    if(visit[m] ==1):
                        boolean = False;
                        break;
                        
                    visit[m] = 1
                
            if boolean == True:
                count +=1

print(count)