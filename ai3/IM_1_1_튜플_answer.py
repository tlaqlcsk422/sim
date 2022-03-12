# 주제: 튜플

## [튜플]
## : 간단하게 말해 "수정, 추가, 삭제가 불가능한 리스트" 라고 간주할 수 있다.
## 연습문제1: 튜플 만들기
## 2가지 방법으로 튜플을 선언해보고, 두 변수의 값고 자료형을 출력해보자.
'''
numbers1 = (4, 5, 6, 7)
numbers2 = 1, 2, 3, 4
print(numbers1, type(numbers1))
print(numbers2, type(numbers2))
'''
## 연습문제2: 원소가 하나인 튜플 만들기
## 선언시 ,(쉽표)를 넣지 않은 경우와 쉼표를 넣어 변수를 만들고, 변수들의 값과 자료형을 비교해보자.
'''
num1 = (77)
num2 = (77,)
num3 = 77
num4 = 77,
print("num1: ", num1, type(num1))
print("num2: ", num2, type(num2))
print("num3: ", num3, type(num3))
print("num4: ", num4, type(num4))
'''
## 연습문제3: 튜플 ↔ 리스트로 변환
## : tuple을 만들고 이를 list로 변환 후 값과 자료형을 출력한 후, 이를 다시 튜플로 바꾸어 같은 과정을 반복해보자.
'''
numbers = (100, 110, 10)
numbers = list(numbers)
print(numbers, type(numbers))
numbers = tuple(numbers)
print(numbers, type(numbers))
'''
## 연습문제4: 패킹과 언패킹 그리고 a, b 값 바꾸기
## 4-1) 패킹과 언패킹을 하여 자료형을 출력해보자.
## 4-2) 패킹 언패킹 개념을 활용하여 a, b의 값 바꾸어보자
'''
a = 7
b = 8
numbers = a, b
print("numbers:", numbers, type(numbers))
c, d = numbers
print("c: ", c, type(c))
print("d: ", d, type(d), end='\n\n')

print("a: ", a)
print("b: ", b)
a, b = b, a         
print("a: ", a)
print("b: ", b)
'''
## 연습문제5: 튜플과 관련된 함수
'''
numbers = 100, 546, 896, 10, 777
print(max(numbers))         # max(): 튜플에서 최댓값을 반환하는 함수
print(min(numbers))         # min(): 튜플에서 최솟값을 반환하는 함수
print(sum(numbers))         # sum(): 튜플에 포함된 원소들의 함을 반환하는 함수
print(numbers.count(777))   # .count(): 입력한 숫자가 튜플에 몇 개 있는지 세어주는 함수(메서드)
print(numbers.index(246))   # .index(): 입력한 숫자의 인덱스를 반환해주는 함수(메서드)
'''
