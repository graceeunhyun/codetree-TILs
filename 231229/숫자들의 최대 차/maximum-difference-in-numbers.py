n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()  # Sort the array for efficient range checking

left, right = 0, 0
maxcount = 0

while left < n:
    while right < n and arr[right] - arr[left] <= k:
        right += 1

    maxcount = max(maxcount, right - left)
    left += 1

print(maxcount)