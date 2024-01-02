from itertools import permutations

arr = list(map(int, input().split()))
arr.sort()

def find_ABCD(values):
    for perm in permutations(values):
        A, B, C, D = perm[:4]
        if A <= B <= C <= D and A + B == perm[4] and B + C == perm[5] and C + D == perm[6] and D + A == perm[7] \
                and A + C == perm[8] and B + D == perm[9] and A + B + C == perm[10] and A + B + D == perm[11] \
                and A + C + D == perm[12] and B + C + D == perm[13] and A + B + C + D == perm[14]:
            return A, B, C, D

result = find_ABCD(arr)
print(*result)