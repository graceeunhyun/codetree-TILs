# 자리 바꾸기 2
n, k = map(int, input().split())
arr = []
for i in range(n+1):
    arr.append(i)

move = []
for i in range(k):
    val = list(map(int, input().split()))
    move.append(val)

dic = {}
for i in range(n):
    dic[i+1] = [i+1]

#k 번의 자리바꿈이 있는 거 
for i in range(3):
    #3k 정도 돌아가서 이제 수행 해야 한다. 
    for i in range(k):
        a, b = move[i]
        #자리 바꿈
        arr[a], arr[b] = arr[b], arr[a]
        #print(arr)
        dic[arr[a]].append(b)
        dic[arr[b]].append(a)

for i in range(n):
    arr = dic[i+1]
    setA = set(arr)

    print(len(setA))
#print(dic)