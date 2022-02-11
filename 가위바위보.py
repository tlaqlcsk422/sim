import random

count = 0

while True:
    all = ['가위','바위','보']
    computer = random.choice(all)

    player = input("가위, 바위, 보 중 하나를 입력하세요.")
    if player == '가위' or player == '보' or player == '바위':
        if (computer == '가위' and player == '보') or (computer == '바위' and player == '가위') or (computer == '보' and player == '바위'):
            print(f"computer = {computer}, player = {player}이기 때문에 computer 승리!!")

        elif (computer == '보' and player == '가위') or (computer == '가위' and player == '바위') or (computer == '바위' and player == '보'):
            print(f"computer = {computer}, player = {player}이기 때문에 player 승리!!")

        else:
            print(f"computer = {computer}, player = {player}이기 때문에 무승부입니다!")
    else:
        print("잘못 입력했습니다.")