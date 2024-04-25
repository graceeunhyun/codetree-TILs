n, m, k = map(int, input().split())
arr = []

# Initialize the 2D array
for i in range(n):
    val = list(map(int, input().split()))
    arr.append(val)

# Function to insert a block of ones
def insert(row, col):
    for j in range(col, col + m):
        arr[row][j] = 1

# Check if indices are within valid range
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# Check if the cells in the specified range are all empty
def check(colStart, colEnd, row):
    for i in range(colStart, colEnd):
        if not in_range(row, i) or arr[row][i] == 1:
            return False
    return True

k=k-1
# Iterate over the rows and check if it's valid to insert the block
if n == 1:
    if check(k, k+m, 0):
        insert(0, k)


possibleIndex = 0

for i in range(n):
    if check(k, k + m, i):
        possibleIndex = i
    else:
        break

insert(possibleIndex, k)
        


# Print the updated array
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print("")