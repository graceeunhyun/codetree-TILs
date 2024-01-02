n, k = map(int, input().split())
numbers = list(map(int, input().split()))

#print(numbers)
def min_max_jump_stones(n, k, numbers):
    result = float('inf')  # 결과를 저장할 변수를 무한대로 초기화

    # 가능한 모든 시작점에 대해 반복
    for start in range(1, n + 1):
        current_max = max(numbers[start - 1 : start - 1 + k])  # 현재 위치에서 가능한 점프 범위 내의 최댓값 계산
        result = min(result, current_max)  # 결과 갱신

    return result

print(min_max_jump_stones(n, k, numbers))