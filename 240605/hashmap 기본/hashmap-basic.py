n = int(input())
d = dict()
for i in range(n):
    val = list(input().split())

    if val[0] == "add":
        # add 에 대한 부분을 넣을 때 
        # key value 로 넣는다
        d[val[1]] = val[2]
    
    elif val[0] == "remove":
        # remove 일 경우 key 가 k 인 상을 찾아 hash map 에서 제거합니다 

        # 특정 key 일 경우 제거합니다
        d.pop(val[1])
    
    else:
        #find 일 경우 

        if val[1] in d:
            print(d[val[1]])
        else:
            print("None")