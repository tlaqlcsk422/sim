# 주제: 조건문

# [조건문]
## 조건문이란?: 조건에 따라 명령이 달라지는 제어문,
## 제어문 및 함수의 주요 특징!: 제어문에 포함된 문장은 "띄어쓰기"로 구분한다.
## if문: 조건의 시작. if에 걸린 조건이 참일 경우, 포함된 문장들 실행
## else문: 조건이 거짓(False)인 경우, 포함된 문장을 실행
## elif문: if문의 조건이 거짓인 경우 중에서 elif문의 조건이 참일 때, 포함된 문장 실행


# 연습문제: if 판단문과 if-else로 판단하는 프로그램


## mission1>> 구독자수를 입력받고 수익창출이 되는지 여부를 판단해보자
num = int(input("구독자수를 입력하세요: "))

if num > 1000:
    print("수익창출을 할 수 있습니다.")
else: ##elif num < 1000:
    print("수익창출 불가능")


## mission2>> 현재 가진 금액을 통해 최대로 먹을 수 있는 음식을 출력하는 프로그램
## 20000원 이상: 오늘 저녁은 치킨이닭!
## 10000원 이상: 이제는 고오급 음식인 떡볶이 ㅎㅎ
## 2000원 이상: 그래도 굶지는 않는 편의점 삼각김밥!
## 2000원 미만: 없다고 못먹는건 아니다. 친구에게 "한입만!"을 외쳐보자

a = int(input("오늘 가진 금액은?: "))

if a >= 20000:
    print("오늘 저녁은 치킨")
elif a >= 10000:
    print("떡볶이")
elif a >= 2000:
    print("삼각김밥")
else:
    print("한입만 줘~~")


## mission3>> 국어, 영어, 수학 점수를 입력받고 합계와 평균를 출력한 뒤.
## - 평균이 60점이 넘을 경우: "보충 대상자가 아닙니다. 즐거운 방학보내세요"
## - 퍙균이 60점이 넘지 않을 경우: "보충 대상자입니다. 당신의 방학은 이제 제껍니다 ㅎㅎ"
## 를 출력하는 프로그램을 만들어 보자

k = int(input("국어점수 입력: "))
e = int(input("영어점수 입력: "))
m = int(input("수학점수 입력: "))
p = (k + e + m)/3

if p >= 60 :
    print("보충대상자가 아닙니다. 즐거운 방학")
else:
    print("보충대상자입니다.")


