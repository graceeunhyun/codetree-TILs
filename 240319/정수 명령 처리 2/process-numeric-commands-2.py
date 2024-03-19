from collections import deque;

class Queue:
    def __init__(self):
        self.dq = deque();
    
    def push(self, item):
        self.dq.append(item)
    
    def empty(self):
        if(not self.dq):
            return 1
        else:
            return 0

    
    def size(self):
        print(len(self.dq));
    
    def front(self):
        
        return self.dq[0]
    
    def pop(self):
        
        return self.dq.popleft();


n = int(input())
arr = [] 
queue = Queue();
for i in range(n):
    command = input().split()
    
    if(command[0]=="push"):
        queue.push(command[1])
    elif(command[0]=="pop"):
        print(queue.pop())
    elif(command[0] =="size"):
        queue.size()
    elif(command[0] =="empty"):
        print(queue.empty())
    elif(command[0]=="front"):
        print(queue.front())