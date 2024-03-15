def heapify(arr, n, i):
    largest = i 
    l = 2*i + 1  # 왼쪽 자식 노드
    r = 2*i + 2  # 오른쪽 자식 노드

    if l < n and arr[l] > arr[largest]:
        largest = l
    
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr, n):
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# 입력을 받습니다.
n = int(input())
arr = list(map(int, input().split()))

# 힙 정렬을 수행하고 결과를 출력합니다.
heapsort(arr, n)
for elem in arr:
    print(elem, end=" ")