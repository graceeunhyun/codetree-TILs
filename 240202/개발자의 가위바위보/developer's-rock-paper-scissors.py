n = int(input())
arr = []
for i in range(n):
    val = list(map(int, input().split()))
    arr.append(val)
#print(arr)
# 1: 가위 2: 주먹 3: 보
# 1: 가위 2: 보 3: 주먹
# 1: 주먹 2: 가위 3: 보
# 1: 주먹 2:보 3: 가위 
# 1: 보 2: 가위 3: 주먹
# 1: 보 2: 주먹 3: 가위
# 주먹  > 가위 && 보 > 주먹 && 가위 > 주먹 

def whoIsWinner(a, b):
    if(a == "S" and b=="R"):
        return 'b'
    elif(a == "S" and b=="N"):
        return 'a'
    elif(a == "R" and b =="N"):
        return 'b'
    elif(a == "R" and b =="S"):
        return 'a'
    elif(a =="N" and b =="S"):
        return 'b'
    elif(a =="N" and b =="R"):
        return 'a'
    else:
        return "Draw"

ans = 0
rcp = [["S", "R", "N"], ["S", "N", "R"], 
["R", "S", "N"], ["R", "N", "S"],
["N", "S", "R"], ["N", "R", "S"]]
for i in range(6):

        count = 0
        for k in range(n):

            if "a" == whoIsWinner(rcp[i][arr[k][0]-1], rcp[i][arr[k][1]-1]):
                count+=1
                #print(count, i, j, rcp[i], rcp[j])
    

       
        ans = max(ans, count)

print(ans)