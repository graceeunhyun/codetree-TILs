arr = list(map(int, input().split()))

def find_minVal(i, j, k, s):
    sum1 = arr[i]+arr[j]
    sum2 = arr[k]+arr[s]
    sum3 = sum(arr) - (sum1+sum2)

    #능력이 가장 큰팀과 작은 팀의 차이
    min_val = float('inf')
    max_val = 0 


    min_val = min(sum1, sum2)
    min_val = min(min_val, sum3)

    max_val = max(sum1, sum2)
    max_val = max(max_val, sum3)

    #print(max_val - min_val , i, j, k, s)

    return (max_val - min_val)
    

min_val = float('inf')
for i in range(6):
    for j in range(i+1, 6):
        for k in range(0, 6):
            for s in range(k+1, 6):
                if(i != k and j!= k and s!= i and s!= j):
                    min_val = min(min_val, find_minVal(i, j, k, s))

print(min_val)