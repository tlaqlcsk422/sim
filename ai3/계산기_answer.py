# # #global 변수 연습문제
# # # 사칙연산 함수 만들기
# #
# # def subtract(a,b):
# #     global answer
# #     answer = a - b
# #
# #
# # def multiply(a,b):
# #     global answer
# #     answer = a * b
# #
# #
# # def divide(a,b):
# #     global answer
# #     answer = a - b
# #
# # def add(a, b):
# #     global answer
# #     answer = a + b
# #
# #
# #
# # #lambda 연습문제
# # #def -> lambda로 변환하기
# # result2 = list(map((lambda x: x+2), [1,2,3,4,5]))
#
#
#
# #######################################
# #3. 계산기 만들기
# from tkinter import *
#
# root = Tk()
# root.title('계산기')
#
# #숫자가 입력될 entry창 만들기
# text = Entry(root, width=35)
# text.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#
#
# #버튼 클릭 command 함수 만들기
# def button_click(number):
#     current = text.get()
#     text.delete(0, END)
#     text.insert(0, str(current) + str(number))
#
# def button_clear():
#     text.delete(0, END)
#
# def button_add():
#     first_number = text.get()
#     global math
#     global f_num
#     f_num = []
#     math = []
#     math.append('더하기')
#     f_num.append(int(first_number))
#     text.delete(0, END)
#
# def button_equal():
#     f_num.append(text.get())
#     text.delete(0, END)
#     result = f_num[0]
#     for i in range(math.len):
#         if math[i] == '더하기':
#             result += f_num[i+1]
#         if math[i] == '빼기':
#             result -= f_num[i+1]
#         if math[i] == '곱하기':
#             result *= f_num[i+1]
#         if math[i] == '나누기':
#             result /= f_num[i+1]
#     text.insert(0,result)
#
#     # if math == '더하기':
#     #     text.insert(0, f_num + int(second_number))
#     # if math == '빼기':
#     #     text.insert(0, f_num - int(second_number))
#     # if math == '곱하기':
#     #     text.insert(0, f_num * int(second_number))
#     # if math == '나누기':
#     #     text.insert(0, f_num / int(second_number))
#
# def button_subtract():
#     first_number = text.get()
#     global f_num
#     global math
#     f_num = []
#     math = []
#     math.append('빼기')
#     f_num.append(int(first_number))
#     text.delete(0, END)
#
# def button_multiply():
#     first_number = text.get()
#     global f_num
#     global math
#     f_num = []
#     math = []
#     math.append('곱하기')
#     f_num.append(int(first_number))
#     text.delete(0, END)
#
# def button_divide():
#     first_number = text.get()
#     global f_num
#     global math
#     f_num = []
#     math = []
#     math.append('나누기')
#     f_num.append(int(first_number))
#     text.delete(0, END)
#
# button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
# button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
# button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
# button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
# button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
# button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
# button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
# button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
# button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
# button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
# button_add = Button(root, text='+', padx=40, pady=20, command=button_add)
# button_equal = Button(root, text='=', padx=87, pady=20, command=button_equal)
# button_clear = Button(root, text='Clear', padx=77, pady=20, command=button_clear)
#
# button_subtract = Button(root, text='-', padx=41, pady=20, command=button_subtract)
# button_multiply = Button(root, text='*', padx=40, pady=20, command=button_multiply)
# button_divide = Button(root, text='/', padx=40, pady=20, command=button_divide)
#
# button_1.grid(row=3, column=0)
# button_2.grid(row=3, column=1)
# button_3.grid(row=3, column=2)
#
# button_4.grid(row=2, column=0)
# button_5.grid(row=2, column=1)
# button_6.grid(row=2, column=2)
#
# button_7.grid(row=1, column=0)
# button_8.grid(row=1, column=1)
# button_9.grid(row=1, column=2)
#
# button_0.grid(row=4, column=0)
# button_clear.grid(row=4, column=1, columnspan=2)
# button_add.grid(row=5, column=0)
# button_equal.grid(row=5, column=1, columnspan=2)
#
# button_subtract.grid(row=6, column=0)
# button_multiply.grid(row=6, column=1)
# button_divide.grid(row=6, column=2)
#
# root.mainloop()


n = int(input())

result = 1
for i in range(1, n+1):
    result *= i

print(result)
