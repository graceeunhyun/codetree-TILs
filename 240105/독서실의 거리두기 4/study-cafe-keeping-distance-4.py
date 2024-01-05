n = int(input())
seats = list(map(int, input()))

def find_min():
    dist = n
    for i in range(n):
        for j in range(i+1, n):
            if seats[i] == 1 and seats[j] == 1:
                dist = min(dist, j - i)

    return dist

ans = 0
for i in range(n):
    for j in range(i+1, n):
        if seats[i] == 0 and seats[j] == 0:
            seats[i] = 1
            seats[j] = 1

            ans = max(ans, find_min())

            seats[i] = 0
            seats[j] = 0

print(ans)