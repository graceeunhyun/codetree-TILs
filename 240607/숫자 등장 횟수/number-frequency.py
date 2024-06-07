n, m= map(int, input().split())
arr = list(map(int, input().split()))
num_to_index = {}

for elem in (arr):
    #print(elem)
    num_to_index[elem] = num_to_index.get(elem,0)+1


b_map = list(map(int, input().split()))
for i in b_map:
    print(num_to_index.get(i,0), end=" ")