n = int(input())
a = list(map(int, input().split()))
m = int(input())
b= list(map(int, input().split()))
setA = set(a)

#b의 각 원소가 수열 a 에 포함되는지 확인
for elem in b:
    if elem in setA:
        print("1")
    else:
        print("0")