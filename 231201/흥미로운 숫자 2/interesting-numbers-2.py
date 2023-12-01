x, y = tuple(map(int, input().split()))

count = 0

def checkNum(num):
    str_num = str(num)
    count = 0
    for i in range(len(str_num)-1):
        if str_num[i] != str_num[i+1]:
            if count > 0:
                return False
            else:
                count+=1
    
    return True


for i in range(x, y+1):
    if checkNum(i):
        count+=1

print(count+1)