n = int(input())
k = int(input())

start = 1
end = n*n

# 행렬을 :
# 1, 2, 3
# 2, 4, 6
# 3, 6, 9 

def less_than_k(target):
    count =0 
    # 우선 target 을 돌고 
    # row 와 col 을 돌면서 구할 수 있다 
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i*j <= target:
                count+=1      

    #print(target, count)
    return count

while start<end:
    #print("START", start, end)
    #오름차순으로 정렬하였을 때 k 번째로 오는 수를 구하는 프로그램 
    mid = (start+end)//2
    
    if less_than_k(mid) < k:
        start = mid+1
    else:
        end = mid

print(start)