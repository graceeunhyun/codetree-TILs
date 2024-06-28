from sortedcontainers import SortedSet

T = int(input())
for i in range(T):
    k = int(input())
    s = SortedSet()
    for i in range(k):
        val = input().split()
        if val[0] =='I':
            s.add(int(val[1]))

        elif val[0] == 'D':

            if val[1] =='1':
                if s:
                    s.remove(s[-1])

            else:
                if s:
                  s.remove(s[0])
    
    if s:
        print(s[-1], s[0])
    else:
        print("EMPTY")