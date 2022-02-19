##14주차
## problem1. 가위바위보 문제
## 주석 처리된 부분에 올바른 코드를 작성합시다~~
import random

player_win = 0
computer_win = 0

while player_win < 2 and computer_win < 2:
    RSP = ['가위','바위','보']
    computer = random.choice(RSP)

    player = input("가위, 바위, 보 중 하나를 입력하세요.")
    if player == '가위' or player == '보' or player == '바위':
        if ######computer가 이긴 경우###########
            print(f"computer = {computer}, player = {player}이기 때문에 computer 승리!!")
            ######???뭘해야할까???

        elif ############player가 이긴 경우############
            print(f"computer = {computer}, player = {player}이기 때문에 player 승리!!")
            ####???뭘해야할까???

        else:
            print(f"computer = {computer}, player = {player}이기 때문에 무승부입니다!")
    else:
        print("잘못 입력했습니다.")

print(f"player가 {player_win}회, computer가 {computer_win}회 승리했습니다.")

##-----------------------------------------------------------
## problem3. 보물
## 주석 처리된 부분에 올바른 코드를 작성합시다~~

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
##???????

answer = 0
for i in range(0,N):
    ##??????

print(answer)