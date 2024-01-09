n, m  = tuple(map(int, input().split()))
#print(n, m)
arr = list(map(int, input().split()))

def max_min_partition(nums, n, m):
    left, right = max(nums), sum(nums)
    while left < right:
        mid = (left + right) // 2
        partitions, current_sum = 1, 0
        
        for num in nums:
            current_sum += num
            if current_sum > mid:
                partitions += 1
                current_sum = num
        
        if partitions > m:
            left = mid + 1
        else:
            right = mid

    return left

# 결과 출력
result = max_min_partition(arr, n, m)
print(result)