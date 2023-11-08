n = int(input())
arr = []
minWidth = float('inf')
for i in range (n):
    xyinfo = list(map(int, input().split()))
    arr.append(xyinfo)

#print(arr)
for i in range(n):
   
   min_x, max_x = float('inf'), 1
   min_y, max_y = float('inf'), 1

   for j, (x,y) in enumerate(arr):
        if j==i:
            continue
        
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

   minWidth = min(minWidth, (max_x - min_x)*(max_y - min_y))

    

print(minWidth)