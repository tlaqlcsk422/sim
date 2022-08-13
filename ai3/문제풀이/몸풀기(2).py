#비교, 조건연산자 복습
#1. 아래 코드의 출력 결과를 예상해보기
#(1)
print(3 == 5)
#False

#(2)
print(3 < 5)
#True

#(3)
x = 4
print(1 < x < 5)
#True

#(4)
print((3 == 3) and (4 != 3))
#True


#(5)
if 4 < 3:
    print("A")
else:
    print("B")

#(6)
if True:
    print("1")
    print("2")
else:
    print("3")
print("4")

print("---------------------------------")
#2. 사용자로부터 값을 입력받은 후 짝수인지 홀수인지 판별하기
#hint -> input, int
#hint2 -> %(나머지 연산자)
user = int(input("값을 입력하세요: "))

if user % 2 == 0:
    print("짝수")
else:
    print("홀수")

print("--------------------------------")
#3. 사용자로부터 입력받은 단어가 fruit 리스트에 포함되어있는지 확인하고,
#   포함되어있다면 '정답', 아니라면 '오답'을 출력하기
#hint -> list의 포함관계 in 사용
fruit = ["사과","포도","멜론"]
user = input("과일을 입력하세요: ")
if user in fruit:
    print("정답")
else:
    print("오답")

print("---------------------------")
#4. 사용자로부터 3개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하기
#hint -> and, >= 사용자
num1 = int(input("값1을 입력하세요: "))
num2 = int(input("값2을 입력하세요: "))
num3 = int(input("값3을 입력하세요: "))

if num1 > num2 and num1 > num3:
    print(num1)

elif num2 > num1 and num2 > num3:
    print(num2)

else:
    print(num3)


