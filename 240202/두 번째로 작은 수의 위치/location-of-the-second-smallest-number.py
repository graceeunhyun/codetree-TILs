n = int(input())
arr= list(map(int, input().split()))
sorted_arr = sorted(arr)

answer = -1
smallValue = sorted_arr[0]
for i in sorted_arr:
    if(i > smallValue):
        smallValue = i
        break;

#print(smallValue)

count = 0
for j in range(n):
    if(arr[j] == smallValue):
        answer = j 

        if(count >=1):
            answer = -1
            break
        
        count = 1
        #print(answer)
    

if(answer != -1):
    print(answer+1)
else:
    print(answer)