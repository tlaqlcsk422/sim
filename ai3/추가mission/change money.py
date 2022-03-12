#자동 판매기 시뮬레이션 
#거스름돈 구하는 과정을 시뮬레이션한다.

money = int(input("지불한 돈을 입력: "))
drink = int(input("구입할 음료수 가격 입력: "))

change_money = money - drink #거스름돈
print(f"거스름돈은 {change_money}원 입니다.")

change_1000 = change_money // 1000
change_500 = (change_money % 1000) // 500
change_100 = (change_money % 500) // 100

print(f"1000원 지폐의 수 => {change_1000}")
print(f"500원 동전의 수 => {change_500}")
print(f"100원 동전의 수 => {change_100}")

