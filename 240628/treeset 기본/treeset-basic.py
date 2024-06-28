from sortedcontainers import SortedSet

s = SortedSet()


n = int(input())
for i in range(n):
    val = list(input().split())
    if val[0] =="add":
        s.add(int(val[1]))
    
    elif val[0] =="remove":
        s.remove(int(val[1]))

    elif val[0] =="find":
        if int(val[1]) in s:
            print("true")
        else:
            print("false")

    elif val[0] =="lower_bound":
        index =s.bisect_left(int(val[1]))
        if index < len(s):
            print(s[index])
        else:
            print("None")

    elif val[0] =="upper_bound":
        index =s.bisect_right(int(val[1]))
        
        if index < len(s):
            print(s[index])
        else:
            print("None")

    elif val[0] =="largest":
        # 가장 마지막 위치에 들어있음 
        if s:
            print(s[-1])
        else:
            print("None")

    else:
        # 가장 앞에 달려잇음 
        if s:
            print(s[0])
        else:
            print("None")