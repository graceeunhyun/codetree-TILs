x1, x2, x3, x4 = (map(int, input().split()))
#print(arr)

if((x2< x3 and x1< x3) or (x4< x1 and x3 < x1)):
    print("nonintersecting")
else:
    print("intersecting")