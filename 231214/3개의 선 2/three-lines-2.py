n = int(input())
points = [ list(map(int, input().split())) for _ in range(n)] 

max_val = 10
ans = 0
for i in range(max_val+1):

    for j in range(max_val+1):
        for k in range(max_val+1):

            #x 축에 평행한 직선 3개로 모든 점 지나가게 되는 경우 
            success = True
            for x, y in points:
                if x ==i or x ==j or x ==k:
                    continue
                
                success = False
            
            if success:
                ans = 1
            
            # x 축 평행한 직선 2개, y축 평행한 직선 1개
            success = True
            for x,y in points:
                if x ==i or y ==j or y==k:
                    continue
                success = False
            
            if success:
                ans = 1 


            # x축 평행 직선 1개, y축 평행한 직선 2개
            success = True
            for x, y in points:
                if x ==i or y ==j or y ==k:
                    continue

                success = False
            if success:
                ans = 1
            
              
            # y축에 평행한 직선 3개로
            # 모든 점을 지나게 할 수 있는 경우
            success = True
            for x, y in points:
                # 해당 점이 직선에 닿으면 넘어갑니다
                if y == i or y == j or y == k:
                    continue
                
                success = False
            if success:
                ans = 1


print(ans)