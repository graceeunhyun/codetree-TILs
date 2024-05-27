import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        heapq.heappush(self.items, -item)
    
    def empty(self):
        return not self.items
    
    def size(self):
        return len(self.items)
    
    def pop(self):
        if self.empty():
            raise Exception("PriorityQueue is empty")
        
        return -heapq.heappop(self.items)
    
    def top(self):
        if self.empty():
            raise Exception("PriorityQueue is empty")
        return -self.items[0]


n = int(input())
heap = PriorityQueue()
for i in range(n):
    val = list(input().split())

    if val[0] == "push":
        heap.push(int(val[1]))
    
    elif val[0] =="size":
        print(heap.size())
    
    elif val[0]  =="empty":
        if heap.empty():
            print(1)
        else:
            print(0)
    
    elif val[0] =="pop":
        print(heap.pop())
    
    elif val[0]=="top":
        print(heap.top())