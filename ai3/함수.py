#연습문제 1번 별 그리기(길이가 100)
# import turtle
# def DrawStar_100():
#     for i in range(5):
#         turtle.forward(100)
#         turtle.right(144)
#         turtle.forward(100)
#         turtle.left(72)
#
# win = turtle.Screen()
# DrawStar_100()
# win.mainloop()


#연습문제 2번. 별그리기(길이를 우리가 입력으로 넣음)

# def DrawStar(len):
#     for i in range(5):
#         turtle.forward(len)
#         turtle.right(144)
#         turtle.forward(len)
#         turtle.left(72)

#연습문제 3번. 1~100 중에 랜덤한 정수 1개 반환
import random

#힌트
# def getRandom():
#     return random.randint(1,100)
# #
# # print(getRandom())
# # num = getRandom()
# # DrawStar(num)
#
# #연습문제 4번. a,b를 더하면 합을 반환
# def add(a,b):
#     return a+b
#
# print(add(15,20))
#
#
# #튜플 연습문제
# #1번
# # numbers1 = (1,2,3,4)
# # numbers2 = 5,6,7,8
# # print(numbers1, type(numbers1))
# #
# # #2번
# # num1 = (10)
# # num2 = (10,)
# # num3 = "0"
# # num4 = 10,
# # print("num1: ", num1, type(num1))
# # print("num2: ", num2, type(num2))
# # print("num3: ", num3, type(num3))
# # print("num4: ", num4, type(num4))
# #
# # #3번
# # numbers = (100,110,10)
# # numbers = list(numbers)
# # print(numbers, type(numbers))
# # numbers = tuple(numbers)
# # print(numbers, type(numbers))
#
# #4번
# ## 연습문제4: 패킹과 언패킹 그리고 a, b 값 바꾸기
# ## 4-1) 패킹과 언패킹을 하여 자료형을 출력해보자.
# a = 1
# b = 2
# c = 3
# d = (a,b,c)
# a,b,c = d
# print(a,type(a))
# print(d, type(d))
# ## 4-2) 패킹 언패킹 개념을 활용하여 a, b의 값 바꾸어보자
#
# ## 연습문제5: 튜플과 관련된 함수
# numbers = 100, 546,895,10, 777
# print(numbers.index(895))
# print(min(numbers))
# print(sum(numbers))
# print(numbers.count(777))
# print(max(numbers))
#
# #딕셔너리
# ## 연습문제1: 딕셔너리 만들기
# ## : 자신이 좋아하는 youtuber 3~5명의 채널이름(key)과 구독자 수(value)로 dictionary 자료형을 만들어보자
# youtuber = {
#     "최케빈":200000,
#     "PAKA":1000000,
#     "오킹TV":1500000
# }
#
# ## 연습문제2: 딕셔너리 제어1-값에 접근하기
# ## : 자신이 가장 좋아하는 youtuber의 구독자 수를 출력해보자
# print(youtuber["오킹TV"])
#
# ## 연습문제3: 딕셔너리 제어2-값 할당(or 수정)하기
# ## : 자신이 가장 좋아하는 유투버의 구독자 수에 1000이 더 큰 숫자를 넣고 이를 출력해보자
# youtuber["오킹TV"] = 2000000
#
# ## 연습문제3: 딕셔너리 제어3-삭제하기
# ## : 자신이 두번째로 좋아하는 youtuber를 딕셔너리에서 삭제해보자
#
# del youtuber["최케빈"]
# print(youtuber)
#
# ## 연습문제4: 딕셔너리 관련 함수
# ## .items(), .keys(), .values()의 결과와 데이터 타입을 출력해보자
#
# print(youtuber.items())
# print(youtuber.keys())
# print(youtuber.values())


#클래스 만들기 예제

class Student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade

    def Study(self):
        print(f"{self.name}은 열심히 공부중입니다.")

class Jam_Student(Student):
    def __init__(self,name,age,grade):
        super().__init__(name,age,grade)
    def Study(self):
        print(f"{self.grade}학년인 {self.name}은 사칙연산을 공부합니다.")

class Middle_Student(Student):
    def __init__(self,name,age,grade):
        super().__init__(name,age,grade)
    def Study(self):
        print(f"{self.grade}학년인 {self.name}은 방정식을 공부합니다.")


leejunseo = Jam_Student("이준서",13,6)
leejunseo.Study()

parkjungbeom = Middle_Student("박정범",16,4)
parkjungbeom.Study()



