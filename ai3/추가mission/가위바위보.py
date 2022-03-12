# import random
#
# player_win = 0
# computer_win = 0
#
# while player_win < 2 and computer_win < 2:
#     RSP = ['가위','바위','보']
#     computer = random.choice(RSP)
#
#     player = input("가위, 바위, 보 중 하나를 입력하세요.")
#     if RSP:
#         if (computer == '가위' and player == '보') or (computer == '바위' and player == '가위') or (computer == '보' and player == '바위'):
#             print(f"computer = {computer}, player = {player}이기 때문에 computer 승리!!")
#             computer_win +=1
#
#         elif (computer == '보' and player == '가위') or (computer == '가위' and player == '바위') or (computer == '바위' and player == '보'):
#             print(f"computer = {computer}, player = {player}이기 때문에 player 승리!!")
#             player_win += 1
#
#         else:
#             print(f"computer = {computer}, player = {player}이기 때문에 무승부입니다!")
#     else:
#         print("잘못 입력했습니다.")
#
# print(f"player가 {player_win}회, computer가 {computer_win}회 승리했습니다.")


A, B, V = map(int, input().split())
now = 0
days = 0

while True:
    days += 1
    now += A
    if now >= V:
