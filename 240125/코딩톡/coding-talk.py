n, m, p = map(int, input().split())

# 초기에 모든 사람이 해당 메세지를 안 읽었다고 가정
unread_count = [n] * n

# 메세지 정보를 처리하여 읽지 않은 사람의 수를 업데이트
for _ in range(m):
    sender, unread = input().split()
    sender_idx = ord(sender) - ord('A')-1
    unread_count[sender_idx] = int(unread)

# p번째 메세지를 읽지 않은 사람들의 이름 찾기
unread_people = [chr(ord('A') + i) for i in range(n) if unread_count[i] > p]

# 결과 출력
print(" ".join(unread_people))