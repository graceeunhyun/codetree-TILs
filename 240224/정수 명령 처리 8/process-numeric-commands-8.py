class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def push_front(self, new_data):
        #a 는 정수
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head != None:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.count +=1

        else:
            self.head = new_node
            self.tail = new_node
            self.count +=1     

    def push_back(self, new_data):
        new_node = Node(new_data)
        new_node.prev = self.tail
        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
            self.count +=1
        else:
            self.head = new_node
            self.tail = new_node
            self.count +=1
    
    def pop_front(self):
        if self.head == None:
            print("Empty")
        elif self.head.next == None:
            temp = self.head
            self.head = None
            self.tail = None
            self.count = 0
            print(temp.data)
        else:
            temp = self.head
            temp.next.prev = None
            self.head = self.head.next
            self.count -=1
            print(temp.data)

    def pop_back(self):
        if self.tail == None:
            print("Empty")
        
        #node : 1
        elif self.tail.prev == None:
            temp = self.tail
            self.tail = None
            self.head = None
            self.count = 0
            print(temp.data)
        # node : 여러개 
        else:
            temp = self.tail
            temp.prev.next = None
            self.tail = self.tail.prev
            self.count -=1
            print(temp.data)
    
    def size(self):
        print(self.count)
    
    def empty(self):
        if self.count >0:
            print(0)
        else:
            print(1)
    
    def front(self):
        print(self.head.data)
    
    def back(self):
        print(self.tail.data)

        

n = int(input())
list = DoublyLinkedList()
for i in range(n):
    command = input().split()
    if(command[0] == "push_back"):
        list.push_back(int(command[1]))
    elif(command[0] == 'push_front'):
        list.push_front(int(command[1]))
    
    elif command[0] == 'pop_front':
        list.pop_front()
    elif command[0] == 'pop_back':
        list.pop_back()
    elif command[0] == 'size':
        list.size()
    elif command[0] == 'front':
        list.front()
    elif command[0] == 'back':
        list.back()
    elif command[0] == 'empty':
        list.empty()