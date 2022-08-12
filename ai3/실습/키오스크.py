from tkinter import *


#메뉴:가격 딕셔너리 생성
price_meal = {"김밥":3000,"라면":3500,"떡볶이":5000,"튀김":5000,"쫄면":7000}
price_drink = {"아메리카노":3000,"라떼":3500,"아이스티":4000,
               "레몬에이드":4500,"딸기스무디":5000}

price_meal['라면']

#주문할 메뉴를 저장해놓을 비어있는 딕셔너리
#메뉴:개수
order_meal = {}
order_drink = {}

#총 가격을 더해줄 변수
total_price = 0

#음식 버튼을 눌렀을 때
#음식 메뉴 버튼들이 보이도록
#hint - configure(bg 속성) 사용
#hint2 - pack_forget() 사용
def show_meal():
    btn_meal.configure(bg="yellow")
    btn_drink.configure(bg="white")
    frame4.pack_forget()
    frame3.pack_forget()
    frame2.pack(fill="both", expand=True)
    frame4.pack(fill="both", expand=True)


#음료 버튼을 눌렀을 때
#음료 메뉴 버튼이 보이도록
#hint - configure(bg 속성) 사용
#hint2 - pack_forget() 사용
def show_drink():
    btn_drink.configure(bg="yellow")
    btn_meal.configure(bg="white")
    frame4.pack_forget()
    frame2.pack_forget()
    frame3.pack(fill="both", expand=True)
    frame4.pack(fill="both", expand=True)


#주문할 메뉴와 개수 저장하기
#딕셔너리의 get() 이용하기
#글로벌 변수 이용하기
def meal_add(m):
    global price_meal, order_meal, total_price
    if m not in price_meal:
        print("입력한 메뉴가 존재하지 않습니다.")
    price = price_meal.get(m)
    total_price += price

    if m in order_meal:
        order_meal[m] = order_meal.get(m) + 1
    else:
        order_meal[m] = 1

    print_order()
    print_price()


def drink_add(m):
    global price_drink, order_drink, total_price
    if m not in price_drink:
        print("입력한 메뉴가 존재하지 않습니다.")
    price = price_drink.get(m)
    total_price += price

    if m in order_drink:
        order_drink[m] = order_drink.get(m) + 1
    else:
        order_drink[m] = 1

    print_order()
    print_price()

#주문서에 출력
#변수 하나에 문자열 계속 등록하는 형식
#for문 사용해서 딕셔너리 전체 가져오기
def print_order():
    global order_meal, order_drink

    tmp = ""

    for i in order_meal:
        tmp = tmp + i + " X " + str(order_meal.get(i)) + "\n"
    for i in order_drink:
        tmp = tmp + i + " X " + str(order_drink.get(i)) + "\n"

    text_1.delete('1.0', END)
    text_1.insert(INSERT, tmp)


#clear와 비슷한 버튼
#전체 내용 초기화 시키기
#주문 딕셔너리 삭제 및 초기화
#가격, 주문서 초기화
def order_end():
    global total_price, order_meal, order_drink
    total_price = 0
    del order_meal
    del order_drink

    order_meal = {}
    order_drink = {}
    print_price()
    print_order()
    show_meal()

#총 합산 가격 출력 함수
def print_price():
    global total_price
    label_price.configure(text=str(total_price)+" 원")



window = Tk()
window.title("주문 프로그램")
window.geometry("600x400+500+300")
window.resizable(False, False)

#음식, 음료, 주문 종료 버튼과 합산가격 레이블이 들어갈 프레임
frame1 = Frame(window, width="600", height="10")
frame1.pack(fill="both")

#음식 버튼들이 들어갈 프레임
frame2 = Frame(window, width="600")
frame2.pack(fill="both", expand=True)

#음료 버튼들이 들어갈 프레임
frame3 = Frame(window, width="600")
#frame3.pack(fill="both", expand=True)

#text(주문서)가 들어갈 프레임
frame4 = Frame(window, width="600", height="10")
frame4.pack(fill="both", expand=True)

btn_meal = Button(frame1, text="식사", padx="10", pady="10", bg="yellow", command=show_meal)
btn_meal.grid(row=0, column=0,padx=10, pady=10)

btn_drink = Button(frame1, text="음료", padx=10, pady=10, bg="white", command=show_drink)
btn_drink.grid(row=0, column=1, padx=10, pady=10)

btn_end = Button(frame1, text="주문종료", padx=10, pady=10, command=order_end)
btn_end.grid(row=0, column=2, padx=10, pady=10)

label_price = Label(frame1, text="0 원", width="20", padx=10, pady="10", fg="blue", font='Arial 15')
label_price.grid(row=0, column="3", padx="10", pady="10")

#음식 버튼
#프레임 2에 배치
#command 함수 -> lambda를 이용해 input 값에 음식 종류를 추가
#grid 방식으로 배치
btn_meal_1 = Button(frame2, text="김밥\n(3000원)", padx=10, pady=10, command=lambda: meal_add("김밥"))
btn_meal_1.grid(row=0, column=0, padx=10, pady=10)

btn_meal_2 = Button(frame2, text="라면\n(3500원)", padx=10, pady=10, command=lambda: meal_add("라면"))
btn_meal_2.grid(row=0, column=1, padx=10, pady=10)

btn_meal_3 = Button(frame2, text="떡볶이\n(5000원)", padx=10, pady=10, command=lambda: meal_add("떡볶이"))
btn_meal_3.grid(row=0, column=2, padx=10, pady=10)

btn_meal_4 = Button(frame2, text="튀김\n(5000원)", padx=10, pady=10, command=lambda: meal_add("튀김"))
btn_meal_4.grid(row=0, column=3, padx=10, pady=10)

btn_meal_5 = Button(frame2, text="쫄면\n(7000원)", padx=10, pady=10, command=lambda: meal_add("쫄면"))
btn_meal_5.grid(row=0, column=4, padx=10, pady=10)


# 음료
#프레임 3에 배치
#command 함수 -> lambda를 이용해 input 값에 음식 종류를 추가
#grid 방식으로 배치
btn_drink_1 = Button(frame3, text="아메리카노\n(3000원)", padx=10, pady=10, command=lambda: drink_add("아메리카노"))
btn_drink_1.grid(row=0, column=0, padx=10, pady=10)

btn_drink_2 =Button(frame3, text="라떼\n(3500원)", padx=10, pady=10, command=lambda: drink_add("라떼"))
btn_drink_2.grid(row=0, column=1, padx=10, pady=10)

btn_drink_3 =Button(frame3, text="아이스티\n(3000원)", padx=10, pady=10, command=lambda: drink_add("아이스티"))
btn_drink_3.grid(row=0, column=2, padx=10, pady=10)

btn_drink_4 =Button(frame3, text="레몬에이드\n(4000원)", padx=10, pady=10, command=lambda: drink_add("레몬에이드"))
btn_drink_4.grid(row=0, column=3, padx=10, pady=10)

btn_drink_5 =Button(frame3, text="딸기스무디\n(5000원)", padx=10, pady=10, command=lambda: drink_add("딸기스무디"))
btn_drink_5.grid(row=0, column=4, padx=10, pady=10)


# 주문 리스트
text_1 = Text(frame4, height="10")
text_1.pack()

window.mainloop()