n, m = map(int, input().split())
arr = [] 
for i in range(n):
    val = list(map(int, input().split()))
    arr.append(val)

#폭탄을 터트릴 위치
bomb = []
for i in range(m):
    val = int(input())
    bomb.append(val)




def explode(col, index):
    val = arr[index][col]
    x = index
    y = col
    dxs, dys = [-1, 1, 0,0], [0,0,1,-1 ]
    arr[x][y] = 0
    for dx, dy in zip(dxs, dys):
        for i in range (val):
           nx = x + dx*i
           ny = y + dy*i
           
           if(0<=nx<n and 0<=ny<n):
              arr[nx][ny] = 0

    #중력 작용 받기 
    temp = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(n):
        count = n-1
        for i in range(n-1, -1, -1):
            if(arr[i][j]!=0):
                temp[count][j] = arr[i][j]
                count -=1
    
    for i in range(n):
        for j in range(n):
            arr[i][j] = temp[i][j]


#m 번째 폭탄이 터저야함. 
for i in range(m):

    explode(bomb[i]-1 , i)
    #중력이 내리는 로직 


for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print("")