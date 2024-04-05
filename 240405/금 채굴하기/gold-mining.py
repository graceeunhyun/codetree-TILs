n, m = map(int, input().split())
arr = []

for _ in range(n):
    val = list(map(int, input().split()))
    arr.append(val)

def get_cost(k):
    return k*k + (k+1)*(k+1)

def gold_count_fun(x, y, k):
    gold_count = 0
    for i in range(x - k, x + k + 1):
        for j in range(y - k, y + k + 1):
            if 0 <= i < n and 0 <= j < n:
                gold_count += arr[i][j]
    return gold_count

max_gold = 0
for i in range(n):
    for j in range(n):
        for k in range(int(n / 2) + 1):
            gold_count = gold_count_fun(i, j, k)
            mining_cost = get_cost(k)

            if mining_cost <= m:
                max_gold = max(max_gold, gold_count)

print(max_gold)