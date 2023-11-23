k, n = tuple(map(int, input().split()))
arr = []

for i in range(k):
    value = list(map(int, input().split()))
    arr.append(value)

count = 0

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            continue
        correct = True
        for lists in arr:
            index_a = lists.index(a)
            index_b = lists.index(b)

            if index_a > index_b:
                correct = False;
        
        if correct:
            count+=1

print(count)