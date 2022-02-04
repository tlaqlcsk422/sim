import random

#랜덤 값 설정
x = random.randint(1,100)

#숫자 하나 입력받기
while True: #무한루프
    num = int(input("숫자를 입력하세요: "))
    if num == x:
        print("정답!!!")
        break   #무한루프 중지
    elif num > x:
        print("Down!!!")
    else:
        print("UP!!!")

