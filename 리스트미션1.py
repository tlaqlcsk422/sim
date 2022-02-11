menu = ['파스타','피자','햄버거','콜라']
price = [8500,10000,5000,1500]

order = input("주문할 메뉴를 말하세요: ")
num = int(input("개수를 말하세요: "))

if menu[0] == order:
    money = price[0] * num
elif menu[1] == order:
    money = price[1] * num
elif menu[2] == order:
    money = price[2] * num
elif menu[3] == order:
    money = price[3] * num

print(f"가격은 {money}원 입니다.")