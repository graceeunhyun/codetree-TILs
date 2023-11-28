x, y= tuple(map(int, input().split()))

def find_val(n):
    _sum = 0
    while(n >10):
        _sum += (int)(n%10)
        n = (int)(n/10)
    
    _sum += n

    return _sum;

max_val = 0 
for i in range(x, y+1):
    val = find_val(i)
    max_val = max(val, max_val)

print(max_val)