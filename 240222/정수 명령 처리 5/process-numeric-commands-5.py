n = int(input())
arr= [] 
for i in range(n):
    command = input().split()
    if command[0] =='push_back':
        value = int(command[1])
        arr.append(value)
    elif command[0] == 'get':
        value = int(command[1])-1
        if 0 <= value < len(arr):
            print(arr[value])
    elif command[0] == 'size':
        print(len(arr))
    elif command[0] == 'pop_back':
        arr.pop();