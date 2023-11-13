# 입력
N = int(input())
segments = []
for _ in range(N):
    x1, x2 = map(int, input().split())
    segments.append((x1, x2))

# 선분을 x2 값을 기준으로 정렬
segments.sort(key=lambda segment: segment[1])

# 겹치지 않는 선분의 수 초기화
non_overlapping_count = 0
current_end = -float('inf')

# 선분들을 순회하며 겹치지 않는 선분의 수 계산
for segment in segments:
    x1, x2 = segment
    if x1 > current_end:
        non_overlapping_count += 1
        current_end = x2

# 결과 출력
print(non_overlapping_count)