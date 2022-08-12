# #global 변수 연습문제
# # 사칙연산 함수 만들기
answer = 0

def subtract(a,b):
    global answer
    answer = a - b

subtract(5, 3)
print(answer)

def add(a,b):
    global answer
    answer = a + b

def divide(a,b):
    global answer
    answer = a / b

def multiply(a,b):
    global answer
    answer = a * b




# #lambda 연습문제
# #def -> lambda로 변환하기
# print("람다함수: ",(lambda x,y,z:x * y - z)(10,2,3))
#
# def a1(x,y,z):
#     return x * y - z
#
# print("def함수: ", a1(10,2,3))

def plus_two(x):
    return x + 2

result1 = list(map(plus_two,[1,2,3,4,5]))
print(result1)

#람다함수로 변경하기
# result2 = list(map((lambda x:x+2),[1,2,3,4,5]))
print(list(map((lambda x:x+2),[1,2,3,4,5])))

x =input("숫자를 입력하세요: ")

#######################################
# 3. 계산기 만들기
from tkinter import *

root = Tk()
root.title('계산기')

#숫자가 입력될 entry창 만들기
text = Entry(root, width=35)
text.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


#버튼 클릭 command 함수 만들기
#entry 창에 해당 버튼 text의 숫자를 띄워주는 함수
def button_click(number):


#entry 창에 있는 내용 삭제
def button_clear():


#사칙연산 함수
#global 변수 math와 f_num 사용

def button_add():


def button_subtract():


def button_multiply():


def button_divide():


# = 버튼을 누르면 연산시작하는 함수
def button_equal():

##버튼 생성하기

#숫자 0~9 버튼
button_1 = Button(root, text='1',padx=40, pady=20, command= )
button_2 = Button(root, text='2',padx=40, pady=20, command= )
button_3 = Button(root, text='3',padx=40, pady=20, command= )
button_4 = Button(root, text='4',padx=40, pady=20, command= )
button_5 = Button(root, text='5',padx=40, pady=20, command= )
button_6 = Button(root, text='6',padx=40, pady=20, command= )
button_7 = Button(root, text='7',padx=40, pady=20, command= )
button_8 = Button(root, text='8',padx=40, pady=20, command= )
button_9 = Button(root, text='9',padx=40, pady=20, command= )
button_0 = Button(root, text='0',padx=40, pady=20, command= )

#사칙연산, = 버튼
button_add = Button(root, text='+', padx=40,pady=20,command=)
button_subtract = Button(root, text='-', padx=40, pady=20, command=)
button_multiply = Button(root, text='x', padx=40, pady=20, command=)
button_divide = Button(root, text='/',padx=40, pady=20, command=)
button_equal = Button(root,text='=',padx=87, pady=20, command=)

#clear 버튼
button_clear = Button(root, text='Clear',padx=77, pady=20,command=)

#Button 붙이기
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_clear.grid(row=4,column=1,columnspan=2)
button_equal.grid(row=5,column=1,columnspan=2)


root.mainloop()
