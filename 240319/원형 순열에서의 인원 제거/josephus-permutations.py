from collections import deque;
n, k = tuple(map(int, input().split()))

dq = deque()
def solution(n, k):
    for i in range(n):
        dq.append(i+1)

    while(len(dq) !=1):
        for i in range(k-1):
            dq.append(dq[0]) 
            dq.popleft()
        
        #k번째에서는 POP
        print(dq.popleft(), end=" ");

    print(dq[0], end=" ")

solution(n,k)