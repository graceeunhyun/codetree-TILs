n, m, p = map(int, input().split())

# 초기에 모든 사람이 해당 메세지를 안 읽었다고 가정
arr = []

# 메세지 정보를 처리하여 읽지 않은 사람의 수를 업데이트
for _ in range(m):
    person, unread = input().split()
    arr.append([ord(person) - ord('A'), int(unread)])

#A,B,C,D,E,F 이 순서가 0,1,2, 이런식으로 


answer = []
val = False
for j in range(m):
    if(j == p-1):
        if(arr[j][1] == 0):
            print("")
            val = True
            break;
        else:
            answer.append(arr[j][0])
            if(j >=1 and arr[j][1] == arr[j-1][1]):
                    
                    answer.append(arr[j-1][0])

    elif(j > p-1):
        answer.append(arr[j][0])

    # elif(j < p-1):
    #     if(j >=1 and arr[j][1] == arr[j-1][1]):
    #         print(arr[j], j)
    #         answer.append(arr[j-1][0])

if(val == False): 
    #해당 answer 빼고 다 저장하기
    realAnswer = []
    for i in range(n):
        if i not in answer:
            realAnswer.append(chr(ord('A')+i))

    print(" ".join(realAnswer))