A,B, x, y = tuple(map(int, input().split()))
#print(A,B,x,y)

count = float('inf')
planA = abs(B-A)
planB = abs(x-A)+abs(B-y)
planC = abs(A-y)+abs(B-x)

count = min(planA, planB, planC)
print(count)