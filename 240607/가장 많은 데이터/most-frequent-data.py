n = int(input())
arr = []
string_dict = {}

for i in range(n):
    val = input()
    string_dict[val] = string_dict.get(val,0)+1

max_val = 0
for elem in string_dict:
    max_val = max(max_val,string_dict.get(elem,0))

print(max_val)