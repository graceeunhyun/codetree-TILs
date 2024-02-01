import sys
int_max = sys.maxsize

n = int(input())
seats = list(input())

#Step1. 최적의 위치 찾기
# 인접한 쌍들 중 가장 먼 1간의 쌍을 찾습니다
max_dist = 0
max_i, max_j = -1, -1
for i in range(n):
    if seats[i] == '1':
        for j in range(i+1, n):
            if seats[j] =='1':

                #가장 먼 값이다 
                if j-i>max_dist:
                    max_dist = j-i
                    max_i=i
                    max_j=j
                break;


#Step2. 최적의 위치의 1을 놓습니다
seats[(max_i+max_j)//2] ='1'

#Step3. 인접한 쌍들 중 가장 가까운 1간의 쌍을 찾아야한다
ans = int_max
for i in range(n):
    if seats[i] == '1':
        for j in range(i+1, n):
            if seats[j] == '1':
                ans = min(ans, j-i)
                break;

print(ans)