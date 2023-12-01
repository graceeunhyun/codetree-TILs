x, y = map(int, input().split())

count = 0

def are_elements_equal(arr, index):
    other = [arr[i] for i in range(len(arr)) if i != index]
    return all(element == other[0] for element in other)

def checkNum(num):
    str_num = str(num)
    change_count = 0  # Track the number of changes in digits

    for i in range(len(str_num) - 1):
        if str_num[i] != str_num[i + 1]:
            if are_elements_equal(str_num, i) or are_elements_equal(str_num, i + 1):
                return True
            else:
                return False

    return change_count == 1  # Only one change is allowed

for i in range(x, y + 1):
    if checkNum(i):
        #print(i)
        count += 1

print(count)