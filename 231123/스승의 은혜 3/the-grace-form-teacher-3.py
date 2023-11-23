n, b = tuple(map(int, input().split()))
arr = [list(map(int, input().split())) for i in range(n)]

maxcount = 0
#최대명수니깐 sorted를 사용해서 이제 오름차순으로 정리한다. 
def custom_sort(item):
    # 특정 조건에 따라 정렬하는 함수를 정의
    return item[0]/2+item[1]

arr_sorted = sorted(arr, key=custom_sort)
#print(arr)

for i in range(n):
    amount = 0
    count = 0

    for j in range(n):
        if i == j:
            amount +=(arr_sorted[j][0]/2) + arr_sorted[j][1]
        
        else:
            amount += arr_sorted[j][0] + arr_sorted[j][1]
        
        if (b >= amount):
             count+=1
        else:
            break
    
    maxcount = max(maxcount, count)


print(maxcount)