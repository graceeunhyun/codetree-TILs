n, m = map(int, input().split())
dict_m = dict()
dict_n = dict()

for i in range(n):
    elem = input()
    dict_m[elem] = i+1
    dict_n[i+1] = elem

for i in range(m):
    val = input()
    
    if val.isdigit():
        
        print(dict_n.get(int(val), 0))
    else:
        print(dict_m.get(val,0))