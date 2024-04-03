n = int(input())
arr = [] 
for i in range(n):
    val = list(map(int,input().split()))
    arr.append(val)

#print(arr)

def getNumOfGold(row_s, row_e, col_s, col_e):
    num_of_gold = 0

    for i in range(row_s, row_e+1):
        for j in range(col_s, col_e+1):
            num_of_gold += arr[i][j]
    
    #print(num_of_gold)
    return num_of_gold

max_val = 0 
for i in range(n):
    for j in range(n):

        # n*n격자임 
        if i+2 >= n or j+2>=n:
            continue
        
        nm_of_gold = getNumOfGold(i, i+2, j, j+2)

        max_val = max(nm_of_gold, max_val)

print(max_val)