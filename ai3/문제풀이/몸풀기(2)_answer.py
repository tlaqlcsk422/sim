#비교, 조건연산자 복습
#1. 아래 코드의 출력 결과를 예상해보기
#(1)
print(3 == 5)   #False

#(2)
print(3 < 5)    #True

#(3)
x = 4
print(1 < x < 5)    #True

#(4)
print((3 == 3) and (4 != 3))    #True

#(5)
if 4 < 3:
    print("A")
else:
    print("B")  #False

#(6)    1 2 4
if True:
    print("1")
    print("2")
else:
    print("3")
print("4")

#2. 사용자로부터 값을 입력받은 후 짝수인지 홀수인지 판별하기
#hint -> input, int
#hint2 -> %(나머지 연산자)
user = input("")
if int(user) % 2 == 0:
    print("짝수")
else:
    print("홀수")


#3. 사용자로부터 입력받은 단어가 fruit 리스트에 포함되어있는지 확인하고,
#   포함되어있다면 '정답', 아니라면 '오답'을 출력하기
#hint -> list의 포함관계 in 사용
fruit = ["사과", "포도", "복숭아"]
user = input("좋아하는 과일은?")
if user in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")


#4. 사용자로부터 3개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하기
#hint -> and, >= 사용자
num1 = input("input number1: ")
num2 = input("input number2: ")
num3 = input("input number3: ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)
