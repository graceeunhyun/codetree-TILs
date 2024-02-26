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
        next_node = node.next

        if node == self.begin():           # 만약 head가 삭제되어야 한다면
            temp = self.head
            temp.next.prev = None          # 새로 head가 될 노드의 prev값을 지워줍니다.
            self.head = temp.next          # head값을 새로 갱신해주고
            temp.next = None               # 이전 head의 next 값을 지워줍니다.

        else:                              # head가 삭제되는 것이 아니라면
            node.prev.next = node.next     # 바로 전 노드의 next값을 바꿔주고
            node.next.prev = node.prev     # 바로 다음 노드의 prev값을 바꿔주고
            node.prev = None               # 해당 노드의 prev 와
            node.next = None               # 해당 노드의 next 값을 모두 지워줍니다.

        return next_node

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
        if(it != l.begin()):
            it = it.prev
    elif command[0] == 'R':
        if(it != l.end()):
            it = it.next
    elif command[0] == 'D':
        if(it != l.end()):
            l.erase(it)
    elif command[0] == 'P':
        l.insert(it, command[1])

it = l.begin()
while it != l.end():
    print(it.data, end="")
    it =it.next