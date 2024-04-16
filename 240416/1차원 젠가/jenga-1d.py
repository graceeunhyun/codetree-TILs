n = int(input())
arr = [] 
for i in range(n):
    val = int(input())
    arr.append(val)

s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

def remove(s, e):
    temp = [0] * n
    count = 0 
    for i in range(n):
        realNumber = i + 1
        if s <= realNumber <= e:
            continue
        else:
            temp[count] = arr[i]
            count += 1
    
    for i in range(n):
        arr[i] = temp[i]

remove(s1, e1)
remove(s2, e2)

#count 
count = 0 
for i in range(n):
    if(arr[i] != 0):
        count+=1

print(count)
for i in range(n):
    if(arr[i]!= 0):
        print(arr[i])