# 주제: 튜플

## [튜플]
## : 간단하게 말해 "수정, 추가, 삭제가 불가능한 리스트" 라고 간주할 수 있다.
## 연습문제1: 튜플 만들기
## 2가지 방법으로 튜플을 선언해보고, 두 변수의 값과 자료형을 출력해보자.
'''
# numbers1 =  (1, 2, 3, 4)            # ()로 튜플 만들기
# numbers2 =   5, 6, 7, 8           # ()없이 튜플 만들기
# print(numbers1, type(numbers1))
# print(numbers2, type(numbers2))
'''
## 연습문제2: 원소가 하나인 튜플 만들기
## 선언시 ,(쉽표)를 넣지 않은 경우와 쉼표를 넣어 변수를 만들고, 변수들의 값과 자료형을 비교해보자.
## ※ 결과를 비교해보는 것이 중요!!

# num1 = (1)         # ()로 만든 경우
# num2 =  (1,)        # (,)로 만든 경우
# num3 =  1        # 숫자 1개만 넣어준 경우
# num4 =   1,       # 숫자, 로 만들어준 경우
# print("num1: ", num1, type(num1))
# print("num2: ", num2, type(num2))
# print("num3: ", num3, type(num3))
# print("num4: ", num4, type(num4))

## 연습문제3: 튜플 ↔ 리스트로 변환
## : tuple을 만들고 이를 list로 변환 후 값과 자료형을 출력한 후, 이를 다시 튜플로 바꾸어 같은 과정을 반복해보자.

# numbers = 1,3,5,7,9
# numbers =  list(numbers)                        # 튜플을 list로 변환하기
# print(numbers, type(numbers))
# numbers = tuple(numbers)                     # 다시 list를 tuple로 변환해주기
# print(numbers, type(numbers))
#
# a = "100"
# print(a,type(a))
# a = int(a)
# print(a, type(a))


## 연습문제4: 패킹과 언패킹 그리고 a, b 값 바꾸기
## 4-1) 패킹과 언패킹을 하여 자료형을 출력해보자.
## 4-2) 패킹 언패킹 개념을 활용하여 a, b의 값 바꾸어보자
## ※ 결과를 확인하는 것이 중요!!

# 패킹
# a = 1
# b = 2
# numbers = a, b     # numbers로 a,b를 패킹해주기
# print("numbers:", numbers, type(numbers))   # 결과확인(데이터 값, 자료형 확인)
#
# # 언패킹
# c, d = numbers      # numbers에 포함된 숫자를 c, d로 언패킹해주기
#
# print("c: ", c, type(c))
# print("d: ", d, type(d), end='\n\n')        # 결과확인(데이터 값, 자료형 확인)

# 응용: a, b의 값 바꿔주기
# print("a: ", a)
# print("b: ", b)
# a, b = b, a       # a와 b의 값을 바꿔주기 (패킹&언패킹 응용)
# print("a: ", a)     # 결과 확인
# print("b: ", b)


## 연습문제5: 튜플과 관련된 함수
## ※ 결과 확인이 중요!!

numbers = 100, 546, 896, 10, 777, 1, 2, 3
print(max(numbers))         # max(): 튜플에서 최댓값을 반환하는 함수
print(min(numbers))         # min(): 튜플에서 최솟값을 반환하는 함수
print(sum(numbers))         # sum(): 튜플에 포함된 원소들의 함을 반환하는 함수
print(numbers.count(546))         # .count(): 입력한 숫자가 튜플에 몇 개 있는지 세어주는 함수(메서드)
print()         # .index(): 입력한 숫자의 인덱스를 반환해주는 함수(메서드)







