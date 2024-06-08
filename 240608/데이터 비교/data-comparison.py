# 같은 원소를 가지고 있는지 판단하는 프로그램 

n = int(input())
arr1 = list(map(int, input().split()))
set1 = set(arr1)
m = int(input())
arr2= list(map(int, input().split()))
set2= set(arr2)
not_exist = False

#arr2 에 있는 원소들이 arr1 에 존재하는지 확인
for elem2 in arr2:
    if elem2 not in set1:
        print(0, end=" ")
    else:
        print(1, end=" ")