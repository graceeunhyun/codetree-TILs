a, b, c= map(int, input().split())

positions = sorted([a, b, c])

#Case 1. 3 개의 숫자가 전부 연속한 경우 이 경우 이동할 필요가 없으므로 최소 이동 횟수는 0으로 됨
if (positions[0] + 1 == positions[1] and positions[1] +1 == positions[2]):
    print(0)

#Case 2. 2개의 숫자의 차이가 정확히 2가 나는 경우 
# 이 경우에는 남은 숫자를 두 숫자 사이에 바로 넣어주면 되므로 최소 이동 횟수는 1이 된다 .
elif positions[0] + 2 == positions[1] or positions[1]+2 == positions[2]:
    print(1)

#Case 3. 그렇지 않은 경우에는 항상 2번째 걸쳐 
else:
    print(2)