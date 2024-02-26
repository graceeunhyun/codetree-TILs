class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.END = Node(-1)
        self.head = self.END
        self.tail = self.END
    
    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        self.head.prev = new_node
        self.head = new_node
        new_node.prev = None 

    def push_back(self, new_data):
        ##중요. 앞에 비어있다면 맨 앞에 원소 넣어줌
        if self.begin() == self.end():
            self.push_front(new_data)

        else:
            new_node = Node(new_data)
            new_node.prev = self.tail.prev

            self.tail.prev.next = new_node
            new_node.next = self.tail
            self.tail.prev = new_node

    def erase(self, node):
        if node == self.begin():
            self.head = node.next
            if node.next:
                node.next.prev = None
        elif node == self.end():
            self.tail = node.prev
            if node.prev:
                node.prev.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def insert(self, node, new_data):
        if node == self.end():
            self.push_back(new_data)
        elif node == self.begin():
            self.push_front(new_data)
        else:
            new_node = Node(new_data)
            new_node.prev = node.prev
            new_node.next = node
            node.prev.next = new_node
            node.prev = new_node

    def begin(self):
        return self.head

    def end(self):
        return self.tail

n, m = map(int, input().split())
arr = list(input())
l = DoubleLinkedList()

for i in range(n):
    l.push_back(arr[i])



index = n
it = l.tail
for j in range(m):
    command = input().split()

    if command[0] == 'L':
        it = it.prev
    elif command[0] == 'R':
        it = it.next
    elif command[0] == 'D':
        l.erase(it)
    elif command[0] == 'P':
        l.insert(it, command[1])

it = l.begin()
while it != l.end():
    print(it.data, end="")
    it =it.next