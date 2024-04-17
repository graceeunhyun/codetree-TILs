n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Function to explode sequences
def explode(arr, m):
    stack = []
    for num in arr:
        if stack and stack[-1][0] == num:
            stack[-1][1] += 1
            if stack[-1][1] >= m:
                for _ in range(stack[-1][1]):
                    stack.pop()
        else:
            stack.append([num, 1])
    return stack

result = explode(arr, m)

if result:
    remaining_count = sum(count for _, count in result)
    print(remaining_count)
    for num, count in result:
        print('\n'.join(str(num) for _ in range(count)))
else:
    print(0)