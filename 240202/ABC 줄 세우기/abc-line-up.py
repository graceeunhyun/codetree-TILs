def min_swaps_to_sort(arr):
    n = len(arr)
    swap_count = 0

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            swap_count += 1
        arr[j + 1] = key

    return swap_count

# 입력 받기
n = int(input())
arr = input().split()

# 정렬하기
result = min_swaps_to_sort(arr)

# 결과 출력
print(result-1)