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
<DrawStar_100 함수 정의>

win = turtle.Screen()
<DrawStart_100 함소 호출>
win.mainloop()
'''
import turtle

win = turtle.Screen()

def DrawStar_200():
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)
        turtle.forward(100)
        turtle.left(72)

# DrawStar_200()
# turtle.setpos(-400,0)
# DrawStar_200()
# turtle.setpos(400,0)
# DrawStar_200()





## 연습문제2: 입력O, 출력X인 함수
## >> 한 변의 길이를 입력하면, 그 한변의 길이를 가지는 별을 그리는 DrawStar()
'''
import turtle
<DrawStar() 함수 정의해주기> 

win = turtle.Screen()
DrawStar(200)
win.mainloop()
'''

def DrawStar(size):
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
        turtle.forward(size)
        turtle.left(72)

# DrawStar(100)
# DrawStar(200)
# DrawStar(50)
# turtle.done()

## 연습문제3: 입력X, 출력O인 함수
## >> 1~100까지 랜덤한 정수 1개를 반환하는 getRandomNum()
'''
import random
<getRandomNum() 함수 정의해주기>

<getRandomNum() 함수를 호출하여 반환값을 num 변수에 할당하기>
print(num)
'''
import random

def r_num():
    return random.randint(1, 100)

print(r_num())


## 연습문제4: 입력O, 출력O인 함수
## >> a,b를 입력하면 두 수의 합을 반환하는 add()
'''
<add() 함수 정의해주기>

<add() 함수를 호출하여 반환값을 X 에 할당하기 >
print(X)
'''


# def add(a,b):
#     return a+b
#
# print(add(100,50))
# print(add(3,5))


## 함수 Mission: 앞서 반복문 Mission4에서 그린 무지개를 "함수"로 만들어보자
## 조건은 ppt 30p - 함수 Mission 참고

# Mission: draw_rainbow() 함수 정의하기
def draw_rainbow(t, rainbow_size, pen_size, x, y):

    rainbow_color=['red','orange','yellow','green','blue','navy','purple']
    t.pensize(pen_size)

    for i in range(7):
        # 그리기
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

# 이제 draw_rainbow 함수를 활용하여 무지개를 마음껏 그려보자
draw_rainbow(t, 500, 30, 0, 0)
draw_rainbow(t, 100, 10, 200, 200)


turtle.mainloop()





###연습문제
##문자열 a, b, c를 입력받아서 두개를 합쳐서 print해라

def add(a, b, c):
    print(a,b,c,sep="****",end=" ")
    # return a+b+c

add("사과","바나나","망고")
add("딸기","포도","메론")