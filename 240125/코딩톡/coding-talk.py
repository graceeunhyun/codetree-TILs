n, m, p = map(int, input().split())

# 초기에 모든 사람이 해당 메세지를 안 읽었다고 가정
unread_count = []

# 메세지 정보를 처리하여 읽지 않은 사람의 수를 업데이트
for _ in range(m):
    person, unread = input().split()
    unread_count.append([ord(person) - ord('A'), int(unread)])

#A,B,C,D,E,F 이 순서가 0,1,2, 이런식으로 
sorted_data = sorted(unread_count, key=lambda x:x[1])

answer = []
for j in range(m):
    if(j >= p-1):
        answer.append(sorted_data[j][0])


#해당 answer 빼고 다 저장하기
realAnswer = []
for i in range(n):
   if i not in answer:
    realAnswer.append(chr(ord('A')+i))

print(" ".join(realAnswer))