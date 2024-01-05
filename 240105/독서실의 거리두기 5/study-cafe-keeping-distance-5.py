n = int(input())
seat = list(map(int, input()))


def min_val():
    dist = n
    for i in range(n):
        for j in range(i+1, n):
            if seat[i] == 1 and seat[j] ==1:
                dist= min(dist, j-i)
    
    
    return dist

max_val = 0
for i in range(n):
    #들어갈 위치를 일일히 정해보며 그 상황에서 가장 가까운 사람의 거리를 구해 최대값을 계산
    if seat[i] == 0:
        seat[i] = 1

        #가장 가까운 사람 간의 거리를 구해 최대값을 갱신
        max_val = max(max_val, min_val())
        seat[i] = 0

print(max_val)