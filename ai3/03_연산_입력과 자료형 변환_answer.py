# 주제: 1.연산 / 2. 입력과 자료형 변환

# [연산(1)]
## 연산이란?: 수나 식을 일정한 '규칙'에 따라 계산하는 것
## 대입연산: 할당연산자(=)를 활용하여 데이터를 변수에 대입하는 연산자
'''
Oh = 123456
'''

## 산술연산: + - * / 와 같은 수의 계산에 대한 연산자
## mission>> 7과 3에 대해서 + - * / // % **의 결과를 출력하기
'''
print(7+3)  # 10
print(7-3)  #4
print(7*3)  #21
print(7/3)  # 2.3333333333333335
print(7//3) # 2
print(7%3)  # 1
print(7**3) # 343
'''

## 문자열연산: + *
## mission1>> 해시태그1,2,3를 변수로 받고 +연산을 사용하여 이를 한 문장으로 만들어
## 출력해보자
'''
tag1 = '#오늘부터1일'
tag2 = '#내꺼하자'
tag = tag1 + tag2
print(tag)
'''
## mission2>> *연산을 활용하여 같은 문장이 반복되는 문자열을 출력해보자
'''
string = '정신나갈꺼같아'
print(string*10)
'''

## mission>> 복함할당연산자를 연산을 하고, 그 연산이 무엇을 줄인 식인지 주석으로 적어보자.
'''
attack = 100
attack += 10       # attack = attack + 10
print(attack)
attack -= 10
print(attack)
attack *= 10
print(attack)
attack /= 10
print(attack)
'''

# [연산(2)]
## 비교연산: 2개 이상의 수를 비교하는 연산, 결과는 True or False(교재 74p 참고)
## mission>> <, > <=, >=, ==, != 연산을 하고 그 결과 예측(주석)하고 결과 확인하기
'''
print(5>8)      # False
print(3<8)      # True
print(10>=7)    # True
print(200>=751) # False
print(5==11)    # False
print(5!=5)     # False
print("3.141592653589793" == "3.141592653589783")           # Flase
print("illIIilil|IIIIIilllllIIIlilil" != "illIIilil|IIIIIilllllIIIIlilil")  # Flase
'''

## 논리연산: and, or, not 연산, 결과는 True or False
## mission>>and, or, not 연산을 활용하여 결과를 예측(주석)하고 결과 학인하기
'''
print((4<6) and (10 >= 10))     # True and True -> True
print("LoskArk" != "LostArk" or "" == "")   # True or False -> True
print(not 5==5)     # not True -> False
'''
## 멤버십 연산: 포함관계를 나타내는 연산(in, not in), 결과는 True or False
## mission>> 멤버십 연산자를 활용하여 결과를 주석으로 달기
'''
print("Z" in "The Legend of Zelda")             # True
print("l" not in "A Dance of Fire and Ice")     # True
'''

# [입력과 자료형 변환]
## 연습문제>> input()함수 활용하여 변수 x,y에 숫자를 입력하고
## 이 숫자를 더하여 정수들의 합에 대한 결과를 출력해보자
'''
x = input("x를 입력하세요>> ")
y = input("y를 입력하세요>> ")
print(x+y)
'''


## mission>> 출생년도를 입력하고 나이를 출력해보자.
'''
year = int(input('출생년도를 입력하세요 >> '))
age = 2021-year+1

print(f"당신의 나이는 {age}입니다.")
'''