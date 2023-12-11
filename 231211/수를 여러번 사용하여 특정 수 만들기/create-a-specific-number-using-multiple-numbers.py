a, b, c = tuple(map(int, input().split()))

max_val = 0
for i in range(1, int(c/a)+1):
    for j in range(1, int(c/b)+1):
        a_val = i * a
        b_val = j * b

        if (c >= (a_val+b_val)):
            max_val = max(max_val, a_val + b_val);

print(max_val)