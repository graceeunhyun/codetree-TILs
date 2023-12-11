a, b, c = tuple(map(int, input().split()))

max_val = 0
for i in range(0, c//a+1):
    temp = 0 
    for j in range(0, c//b+1):
        a_val = i * a
        b_val = j * b
        #print(i, a, j, b, a_val, b_val, a_val+b_val)
        temp = a_val+b_val
        if (c >= temp):
            max_val = max(max_val, temp);

print(max_val)