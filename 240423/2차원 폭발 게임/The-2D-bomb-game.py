#입력 받기, 
n, m, k = map(int, input().split())
arr = []
for i in range(n):
    val = list(map(int, input().split()))
    arr.append(val)


def get_end_index(startIdx, j, curr_num):
    for i in range(startIdx+1, len(arr)):
        if arr[i][j] != curr_num:
            return i-1
        
    return n-1

# m개 이상이면 폭탄 떨어지기
# 중력 작용 받기

def explode():
    while(True):
        did_explode = False
        for j in range(n):
            
            for i in range(n):
                #각 위치마다 그 뒤로 폭탄이 M 개 이상 있는지 확

                if arr[i][j] == 0:
                    continue

                end_idx = get_end_index(i, j, arr[i][j])
                #print(end_idx, i, arr[i][j])
                if end_idx-i+1>=m:
                    
                    for s in range(i, end_idx+1):
                        arr[s][j] =0
                    
                    did_explode = True 

        temp = [[0] * n for _ in range(n)]
    
        for j in range(n):
            count = n-1
            for i in range(n-1, -1, -1):
                if(arr[i][j] != 0):
                    temp[count][j] = arr[i][j]
                    count -=1
        
        # print(temp)

        if not did_explode:
            break
        

    return temp

# 상자를 시계 방향으로 90도 회전 
# 뒤에서 부터 일거야할 것 가틈
# x 맨 아래 index -- y 맨위 columa

def gravitiy(arr):
    new_temp = [[0] * n for _ in range(n)]
    for j in range(n):
        count = n-1
        for i in range(n-1, -1, -1):
            if(arr[i][j] != 0):
                new_temp[count][j] = arr[i][j]
                count -=1
    
    return new_temp

def rotate():
    temp = [[0] * n for _ in range(n)]

    
    for i in range(n):
        for j in range(n):
            temp[i][j] = arr[n-j-1][i]
    
    temp = gravitiy(temp)

    # print("rotate", temp)


    return temp

arr = explode()
for _ in range(k):

    arr = rotate()
    arr = explode()


count = 0
for i in range(n):
    for j in range(n):

        if(arr[i][j] !=0):
            count +=1

print(count)