#변수 선언 및 입력
n = int(input())
arr = [0] + list(input().split())
ans = 0

for i in range(1, n+1):
    x = chr(ord('A') + i-1)

    idx = 0
    #i번째 알파벳을 찾아 idx 에 저장
    for j in range(1, n+1):
        if arr[j] == x:
            idx = j
    
    
    #idx 번째 알파벳을 i 번째까지 수합
    for j in range(idx -1, i-1, -1):
        arr[j], arr[j+1] = arr[j+1], arr[j]
        ans+=1
    

print(ans)