import heapq
n, m = map(int, input().split())
heap = []
arr = list(map(int, input().split()))


for i in range(n):
    heapq.heappush(heap, -arr[i])


for i in range(m):
    val = heap[0]
    heapq.heappop(heap)
    heapq.heappush(heap, val+1)

print(-heap[0])