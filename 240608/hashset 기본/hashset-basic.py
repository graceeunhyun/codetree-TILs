n = int(input())
# set 자료형 선언 

s = set()

for i in range(n):
    val = list(input().split())

    if val[0]=="add":
        s.add(int(val[1]))
    
    elif val[0]=="find":
        if int(val[1]) in s:
            print("true")
        else:
            print("false")
    else:
        s.remove(int(val[1]))