n = int(input())
arr = list(map(int, input().split()))

for pos in range(6):
    arr_new = [[] for i in range(10)]
    for i in range (n):
        digit = (int)((arr[i]/(10**pos)) % 10)
        arr_new[digit].append(arr[i])

        store_arr = []
        for i in range (10):
            for j in range(len(arr_new[i])):
                store_arr.append(arr_new[i][j])
        
    arr =store_arr

for i in arr:
    print(i, end=" ")