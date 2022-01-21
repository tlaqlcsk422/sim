# 주제: 1. 문자열 입출력 / 2.자료형

# [문자열 입출력]
## 문자열 입출력 연습문제
'''
name = input("이름을 입력하세요: ")
print(f"{name}님 안녕하세요?")
'''

## 문자열 입출력 Mission
'''
name = input("이름을 입력하세요>>> ")
now_str = input("지금하고 싶은 말은?>>> ")
print(f"{name}은 {now_str}이라고 말했다.")
'''

# [자료형]
# ※ 참고: 모두의 파이썬 68p
## 숫자형 1) 정수형(integer, int)
## : 소수점이 없는 숫자의 형태
## mission>> 정수형인 숫자를 출력하고 type() 함수를 활용하여
## 자료형을 주석으로 적기
'''
print(9, 1, 6 ,2)
print(type(9))   # int
'''

## 숫자형 2) 실수형(float)
## : 소수점이 있는 숫자의 형태
## mission>> 실수형인 숫자를 출력하고 type() 함수를 활용하여 자료형을 주석으로 적기
'''
print(1.655757647645454563343)
print(type(1.655757647645454563343))    # float
'''

## 문자열
## : 문자를 나열한 형태의 자료형
## mission1>> ""와 ''를 활용하여 내가 지금 하고 싶은 말을 문자열로 출력하기
'''
print("선생님은")
print('빠른 퇴근을 원한다..!')
'''

## mission2>> 문자열로 인용구호('') 출력하기
'''
print('선생님이 "도연이, 태영이, 윤이, 종현이 하이~"이라고 말했다.')
print('"지금보다 더 적극적으로 아무것도 안하고 싶다"라고 말했다.')
'''

## mission3>> sep과 end를 활용하여 print() 용법 익히기
## sep: ,로 출력이 구분된 문자열 사이 출력 설정 // end: print문의 끝났을 때의 문자열 출력 설정
'''
print(1,2,3,4,6, sep='ㅋ',end='헤헷')
print(1,2,3,4,6, sep='냐옹',end='멍멍')
'''

## - 불린형(참/거짓)
## : 참(True)/거짓(False) 형태의 자료형
## mission>> 불린형의 True와 False를 출력하고 type() 함수를 활용하여
## 자료형을 주석으로 적기
'''
print(True)
print(False)
print(type(True))
'''

# ※ 변수와 연산자 참고: 모두의 파이썬 35p
# [변수]
## 변수란?: 데이터를 저장할 공간. 할당연산자(=)를 활용.
## 특징: "언제든지 데이터를 변경"할 수 있다.
## 문법: 변수이름 = 데이터

## mission>> 내가 좋아하는 게임의 캐릭터 혹은 재밋게 본 책의 정보, 하드웨어 스펙, 게임 정보 등 어떤것도 상관 없음.
## 변수로 저장하고 출력해보자.
## 예시) LOL 챔피언 정보: https://lol.inven.co.kr/dataninfo/champion/compare.php
'''
name = '리신'
attack = 68
speed = 345
reach = 125

print("어디로 가야하오.")
print(f"이름: {name}")
print(f"공격력: {attack}")
print(f"이동속도: {speed}")
print(f"사거리: {reach}")
'''

## 변수 Mission: input()응용하기, 속으로 10초를 세어 맞히는 프로그램
'''
import time

input("Enter를 누르고 속으로 10초를 세는 게임입니다. Enter를 누르면 시작합니다!")
start = time.time()

input("10초를 다 세셨다면 Enter를 눌러 stop!!")
end = time.time()

et = end-start
print(f"실제시간: {et}초")
print(f"차이: {abs(et-10)} 초")
'''
