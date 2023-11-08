n = int(input())
b = []

for i in range(n):
    info = input().split()
    b.append(list(map(int, info)))


a = []
count = 0
successed = True

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            #같은 수가 있는지 확인
            if i== j or j ==k or k ==i:
                continue;
            

            #정직하게 자리와 같이 같으면 해당 숫자가 정답일 때, 모든 입력에 대한 올바른 값이 나왔는지 확인
            successed = True;
            for a, num_cnt1, num_cnt2 in b:
                x = a // 100
                y = a // 10 % 10 
                z = a % 10 

                # cnt : 1 번 count, cnt2: 2번 카운트 
                cnt1 = 0
                cnt2 = 0
                if x == i:
                    cnt1+=1
                if y == j:
                    cnt1+=1
                if z == k:
                    cnt1+=1
                
                # 다른 자리를 아래와 같이 다른 변수를 비교해서 맞으면 올리는 식으로 
                if x == j or x ==k:
                    cnt2+=1
                if y ==i or y ==k:
                    cnt2+=1
                if z== j or z ==i:
                    cnt2+=1
                
                if(cnt1 != num_cnt1 or cnt2 != num_cnt2):
                    successed = False
                    break

        
            if successed == True:
                count+=1

print(count)