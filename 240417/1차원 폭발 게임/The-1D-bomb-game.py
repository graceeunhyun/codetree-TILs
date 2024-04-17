n, m = map(int, input().split())
arr = []
for i in range(n):
    val = int(input())
    arr.append(val)

#print(arr)
#m 개 이상이면 1차원 폭발 게임 

temp = [0]*n

def removeElem(index, count):
    for i in range(index, index+count+1):
        if(0<= i < n-1):
            arr[i] = 0

    count = 0 
    for i in range(0, n):
        if(arr[i] != 0 ):
            temp[count] = arr[i]
            count+=1

    return temp
    

while(True):
    count = 1
    val = 0 
    for i in range(1, n):
        if(arr[i] == arr[i-1]):
            count+=1
            val = arr[i]

        if(count >= m):
            arr = removeElem(i-1, count)  


    if(count < m) or all(elem ==0 for elem in arr):
        break


if all(elem ==0 for elem in arr):
    print(0)
else: 
    for i in (arr):
        if(arr[i] != 0):
            print(arr[i])