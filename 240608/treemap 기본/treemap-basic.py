from sortedcontainers import SortedDict

sd = SortedDict()
n = int(input())
for i in range(n):
    val = list(input().split())

    if val[0]=="add":
        sd[int(val[1])] = int(val[2])
    
    elif val[0]=="find":

        if int(val[1]) in sd:
            print(sd[int(val[1])])
        else:
            print("None")
    
    elif val[0]=="remove":
        sd.pop(int(val[1]))
    
    else:
        # tree map 은 알아서 오름차순
        if not sd:
            print("None")
        else: 
            #이럴 경우 sorted_item 을 list가 
            sorted_item_desc = sorted(sd.items(), key=lambda item: item[0])
            for key, value in sorted_item_desc:
                #print(key, end=" ")
                print(value, end=" ")
            print("")