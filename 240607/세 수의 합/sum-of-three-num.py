n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 세 수의 합
# n 
# m
# k-n-m
find = {}
ans = 0 

# 이게 합쳐져서 세수의 합이 된다.. 
for i in range(n):

    for j in range(i+1,n):

        diff = k-arr[i]-arr[j]

        if diff in find:
            ans += find[diff]

    elem = arr[i]
    if elem in find:
        find[elem] +=1
    else:
        find[elem] = 1


print(ans)