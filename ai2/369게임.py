############ 369 게임 #################

start, end = map(int, input().split())
clap = 0

for i in range(start, end+1):
    i_1000 = i // 1000
    i_100 = (i % 1000) // 100
    i_10 = (i % 100) // 10
    i_1 = i % 10
    if i % 3 == 0:
        clap += 1
    elif i_1000 == 3 or i_1000 == 6 or i_1000 == 9:
        clap += 1
    elif i_100 == 3 or i_100 == 6 or i_100 == 9:
        clap += 1
    elif i_10 == 3 or i_10 == 6 or i_10 == 9:
        clap += 1
    elif i_1 == 3 or i_1 == 6 or i_1 == 9:
        clap += 1

print(clap)

