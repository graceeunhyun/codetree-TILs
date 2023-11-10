n = int(input())
arr = []

for i in range(n):
    value = list(map(int, input().split()))
    arr.append(value)

max_val = 0

for i in range(n):
    new_arr = arr[:i] + arr[i+1:]
    count = [0] * 1000
    
    for j in range(n-1):   
        a, b = new_arr[j]
        for k in range(a, b):
            count[k] = 1
            
    sum_val = sum(count)
    max_val = max(sum_val, max_val)

print(max_val)