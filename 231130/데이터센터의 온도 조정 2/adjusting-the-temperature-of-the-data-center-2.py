def calculate_max_workload(N, C, G, H, preferences):
    max_workload = 0
    
    for temperature in range(min(p[0] for p in preferences), max(p[1] for p in preferences) + 1):
        workload = 0
        
        for preference in preferences:
            Ta, Tb = preference
            
            # Scenario 1: 온도가 Ta 미만인 경우
            if temperature < Ta:
                workload += C
            
            # Scenario 2: 온도가 Ta 이상 Tb 이하인 경우
            elif Ta <= temperature <= Tb:
                workload += G
            
            # Scenario 3: 온도가 Tb 초과인 경우
            elif temperature > Tb:
                workload += H
        
        # 최대 작업량 갱신
        max_workload = max(max_workload, workload) 

    return max_workload

# 입력 받기
N, C, G, H = map(int, input().split())
preferences = [tuple(map(int, input().split())) for _ in range(N)]

# 결과 출력
result = calculate_max_workload(N, C, G, H, preferences)
print(result)