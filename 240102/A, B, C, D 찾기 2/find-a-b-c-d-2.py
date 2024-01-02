arr = list(map(int, input().split()))
arr.sort()

def is_equal_array(arr1, arr2):
    arr1.sort();

    if len(arr1) != len(arr2):
        return Fasle

    for elem1, elem2 in zip(arr1, arr2):
        if elem1 != elem2:
            return False 
    
    return True
    


for a in range(1, 41):
    for b in range(a, 41):
        for c in range(b, 41):
            for d in range(c, 41):
                if is_equal_array([a, b, c, d, a+b, b+c, c+d, d+a, a+c, b+d, a+b+c, a+b+d, a+c+d, b+c+d, a+b+c+d], arr):
                    print(a, b, c, d)