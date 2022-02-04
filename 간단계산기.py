num1 = int(input("정수1 입력>> "))
num2 = int(input("정수2 입력>> "))
oper = input("연산자(+, -, *, /)를 입력>> ")

if oper == "+":
    print(num1, oper, num2, "=", num1 + num2)
elif oper == "-":
    print(num1, oper, num2, "=", num1 - num2)
elif oper == "*":
    print(num1, oper, num2, "=", num1 * num2)
else:
    print(num1, oper, num2, "=", num1 / num2)

