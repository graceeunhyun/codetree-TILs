n, m, q = map(int, input().split())
arr = []
for i in range(n):
    val = list(map(int, input().split()))
    arr.append(val)

wind = [] 
for i in range(q):
    val = list(map(int, input().split()))
    wind.append(val)

def changeInverse(r1, c1, r2, c2):
    firstFirst = arr[r1][c1]
    firstLast = arr[r1][c2]
    secondFirst = arr[r2][c1]
    secondLast = arr[r2][c2]

    # Shift top row to the right
    for i in range(c2, c1, -1):
        arr[r1][i] = arr[r1][i - 1]

    # Shift rightmost column upwards
    for i in range(r2, r1, -1):
        arr[i][c2] = arr[i - 1][c2]

    arr[r1 + 1][c1] = firstFirst
    for i in range(c1, c2):
        arr[r1][i] = arr[r1][i + 1]

    for i in range(r1, r2):
        arr[i][c2] = arr[i + 1][c2]
    arr[r2][c1] = secondLast

def rearrange(r1, c1, r2, c2):
    # Shift according to wind effects
    changeInverse(r1, c1, r2, c2)

for i in range(q):
    r1, c1, r2, c2 = wind[i]
    rearrange(r1 - 1, c1 - 1, r2 - 1, c2 - 1)

# Print the resulting array
for row in arr:
    print(' '.join(map(str, row)))