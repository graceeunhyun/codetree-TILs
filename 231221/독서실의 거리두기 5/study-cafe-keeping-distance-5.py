n = int(input("좌석의 개수를 입력하세요: "))
arr = list(map(int, input("현재 좌석 상태를 입력하세요 (0은 빈 자리, 1은 차있는 자리): ")))
max_val = 0

for i in range(n):
    if arr[i] == 0:
        new_arr = arr.copy()
        new_arr[i] = 1

        min_val = float('inf')
        for j in range(n):
            val = 0
            for k in range(j + 1, n):
                if j == k : 
                    continue
                if new_arr[j] == 1 and new_arr[k] == 1:
                    val = k - j
                    min_val = min(min_val, val)
                   

        max_val = max(max_val, min_val)

print(max_val)