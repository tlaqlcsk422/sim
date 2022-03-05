#
# import random
# '''
# RSP =['가위','바위','보']
#
# #wihle문 사용해서 이긴 횟수가 2회 이상일 때 탈출(break)
# com_win = 0
# play_win = 0
#
# while com_win <=2 and play_win <= 2:
#     # 사용자로부터 입력받기   #computer 랜덤값 가져오기
#     computer = random.choice(RSP)
#     player = input("가위, 바위, 보 중 입력해라: ")
#     #사용자가 입력한게 가위, 바위, 보가 아닐 때 if, else
#     #if문으로 이겼는지 졌는지
#     if (player == '가위' and computer == '보') or (player =='바위' and computer == '가위')######:
#         print("player가 승리!")
# '''
# # RSP = ['가위', '바위', '보']
# #
# # com_win = 0
# # play_win = 0
# #
# # while com_win <= 2 and play_win <=2:    #True
# #     player = input("가위, 바위, 보 중 입력하시오 :  ")
# #     computer = random.choice(RSP)
# #     if #사용자가 입력한게 가위, 바위, 보:
# #         if(player == '가위' and computer == '보') or (player == '바위' and computer == '가위') or (player == '보' and computer == '바위')
# #             print("player가 승리!")
# #
# #         elif ###
# #             #computer가 이김
# #         else:
# #             #비김
# #     else: #가위,바위,보가 아닌 다른 문자열을 입력하면
# #         #잘못했다 다시해라.
# #     # if com_win >= 2 and play_win >=2:
# #     #     break
#
#
# ##########################윤#################################
# RSP = ['가위', '바위', '보']
# computer = random.choice(RSP)
#
# comwin = 0
# plwin = 0
#
# while comwin < 2 and plwin < 2:
#     player = input('가위 바위 보!! ')
#     computer = random.choice(RSP)
#     if RSP:
#         if (player == '가위' and computer == '보' ) or (player == '바위' and computer == '가위' ) or (player == '보' and computer == '바위' ):
#             print('니가 이김')
#             comwin +=1
#
#         elif (player == '가위' and computer == '바위' ) or (player == '바위' and computer == '보' ) or (player == '보' and computer == '가위' ):
#             print('컴퓨터도 못 이기냐')
#             plwin +=1
#
#         else:
#             print('비김')
#     else:
#         print('다시해')
#
# print(comwin, plwin)
# #
# # while comwin >= 2 and plwin >= 2:
# #    break
#
#
# ######################################태영##################################################
# import random
#
#
# RSP = ['가위', '바위', '보']
#
# com_win = 0
# player_win = 0
# while com_win < 2 and player_win < 2:
#     computer = random.choice(RSP)
#     print(f"computer: {com_win} / player: {player_win}")
#     player = input("입력하세요 >>")
#     if (player == '가위' or player == '바위' or player == '보') :
#         print(f"computer : {computer}")
#         if (player == '가위' and computer == '보') or (player == '바위' and computer == '가위') or (player == '보' and computer == '바위') :
#             print("player 승")
#             player_win = player_win + 1
#         elif (player == '가위' and computer == '바위') or (player == '바위' and computer == '보') or (player == '보' and computer == '가위'):
#             print("computer 승")
#             com_win = com_win + 1
#         else :
#             print("비김")
#     else :
#         print("잘못 입력하셨습니다")
#

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B,reverse=True)
c = 0

##정렬
for i in range(N):
    c += A[i] * B[i]

while True:
    player = int(input("숫자를 입력하세요: "))
    if player == 1:
        print("끝!")
        break