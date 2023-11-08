arr = list(map(int, input().split()))

def findMin(i,j,k):
    sum1 = arr[i] + arr[j] + arr[k]
    sum2 = sum(arr) - sum1
    return abs(sum1 - sum2)

min_val = float('inf')
for i in range (6):
    for j in range(i+1,6):
        for k in range (j+1,6):
            min_val = min(findMin(i,j,k), min_val)

print(min_val)