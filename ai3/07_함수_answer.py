# 주제: 함수

# [함수]
##: 여러개의 명령어들을 묶어서 한꺼번에 처리할 수 있도록 만든 하나의 명령어 묶음에 이름을 붙인 것.
## 문법: def 함수이름(매개변수1, 매개변수2, ...):
##         명령어 블럭
##         return 반환값


## 연습문제1: 입력X, 출력X인 함수
## >> 함수를 호출하면 별모양을 그리는 DrawStar_100()
'''
import turtle
def DrawStar_100():
    """한 변의 길이가 100인 별모양 그리기 함수"""
    for i in range(4):
        turtle.forward(100)
        turtle.right(144)
        turtle.forward(100)
        turtle.left(72)

win = turtle.Screen()
DrawStar_100()
win.mainloop()
'''

## 연습문제2: 입력O, 출력X인 함수
## >> 한 변의 길이를 입력하면, 그 한변의 길이를 가지는 별을 그리는 DrawStar()
'''
import turtle
def DrawStar(length):
    for i in range(5):
        turtle.forward(length)
        turtle.right(144)
        turtle.forward(length)
        turtle.left(72)

win = turtle.Screen()
DrawStar(5)
win.mainloop()
'''

## 연습문제3: 입력X, 출력O인 함수
## >> 1~100까지 랜덤한 정수 1개를 반환하는 getRandomNum()
'''
import random
def getRandomNum():
    return random.randint(1, 100)

num = getRandomNum()
print(num)
'''

## 연습문제4: 입력O, 출력O인 함수
## >> a,b를 입력하면 두 수의 합을 반환하는 add()
'''
def add(x, y):
    return x+y

X = add(55, 78)
print(X)
'''

## 함수 Mission: 앞서 반복문 Mission4에서 그린 무지개를 "함수"로 만들어보자
## 조건은 ppt 16p참고

# draw_rainbow() 함수 정의하기
def draw_rainbow(t, rainbow_size, pen_size, x, y):
    """
    입력한 t가 rainbow_size크기의 지름과 pen_size 두께의 색상띠를 가지는 무지개를 (x,y)에 그리는 함수
    :param t: 그림을 그릴 turtle 객체
    :param rainbow_size: 무지개의 지름
    :param pen_size: 무지개를 그릴 펜의 두께
    :param x: 무지개가 그려질 x좌표
    :param y: 무지개가 그려질 y좌표
    :return:
    """
    # 설정
    rainbow_color = ['red', 'orange', 'yellow', 'green', 'blue', 'navy', 'purple']
    t.pensize(pen_size)

    # 그리기
    for i in range(7):
        t.setheading(90)
        t.penup()
        t.setpos(x+(rainbow_size / 2 - i * pen_size), y)
        t.pencolor(rainbow_color[i])
        t.pendown()
        t.speed(10)
        t.circle((rainbow_size / 2 - i * pen_size), 180)

import turtle

win = turtle.Screen()
win.screensize(1000,1000)
t = turtle.Turtle('turtle')
t.speed(0)

draw_rainbow(t, 500, 30, 200, 200)
draw_rainbow(t, 500, 30, -100, -150)
draw_rainbow(t, 100, 8, 100, 100)
draw_rainbow(t, 200, 10, -20, -300)
draw_rainbow(t, 180, 15, 200, -40)
draw_rainbow(t, 100, 5, -50, 70)
draw_rainbow(t, 80, 3, -200, -100)
draw_rainbow(t, 50, 3, -100, -100)
draw_rainbow(t, 50, 3, 70, -30)
turtle.done()
turtle.mainloop()
