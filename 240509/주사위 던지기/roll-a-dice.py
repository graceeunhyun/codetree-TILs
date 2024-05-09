n, m, r, c = map(int, input().split())
direction = list(input().split())
# 주사위 문제로 해당 문자가 돌아간 순서대로 된다.
dice=[1,2,3,4,5,6]
sum = 0
def roll_dice(dice, dir):
    if dir == 'L':
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    elif dir =='R':
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif dir =='U':
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]


for i in range(m):
    roll_dice(dice, direction[i])
    sum+=dice[5]

print(sum)