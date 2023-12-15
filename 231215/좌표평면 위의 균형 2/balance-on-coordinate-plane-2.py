n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n)]
#print(arr)

min_count = float('inf') 
for i in range (101):
    for j in range (101):
        
        if(i % 2 != 0 or j %2 != 0 ):
            continue

        #i 가 x 이고, j 가 y 라고 가정  
        sub_0, sub_1, sub_2, sub_3 = 0,0,0,0 
        for x, y in (arr):
            #4 구역을 나눠보자 
            if ( x< i and y <j):
                sub_0 += 1
            
            elif(x > i and y <j):
                sub_1 +=1
            
            elif(x < i and y > j):
                sub_2 +=1
            
            elif(x > i and y > j):
                sub_3 +=1
            
        m = max(sub_0, sub_1, sub_2, sub_3)
        min_count = min(m, min_count)


print(min_count)