# 주제: 리스트

# [리스트 자료형]
## 리스트를 사용하는 이유?: 여러개의 데이터를 한 번에 저장하기 위해서
## 문법: 리스트이름 = [데이터, 데이터, ... ,데이터]

## 연습문제>> 내가 자주보는 유투버 이름 각자 1개씩 카톡방(혹은 채팅방)에 올리고
## 이 이름들을 list로 만들기

youtuber = ['10월 악토', "로빈하르트", "우왁굳", "T1 Faker", "논리왕전기", "나무늘보"]
print(youtuber)

## 리스트 제어하기1: 데이터 추가
## 방법: 리스트이름.append('추가할문자열')
## 연습문제>> 문자열에 수진썜이 좋아하는 유튜버 "승우아빠"를 추가해보자.
youtuber.append("승우아빠")
print(youtuber)

## 리스트 제어하기2: 인덱싱
## 방법: 리스트이름[인덱스 번호], 여기서 인덱스 번호는 0부터 시작에 주의!
## python의 순서를 가진 것들은 기본 0부터 시작!!
## 연습문제>> 만들어진 유투버 리스트에서 내가 가장 좋아하는 유튜버만 출력해보자
print(youtuber[6])

## 리스트 제어하기3: 데이터 수정하기
## 방법: 리스트이름[인덱스 번호] = '새로넣을 문자열'
## 연습문제>> 내가 가장 좋아하는 유투버의 이름을 2번째로 좋아하는 유튜버의 이름으로 바꿔보자
youtuber[6] = '녹두로'
print(youtuber)

## 리스트 제어하기4: 데이터 삭제하기
## 방법: del 리스트이름[삭제할인덱스번호]
## 연습문제>> 아쉽지만(ㅎㅎ) 선생님이 추가한 유투버를 리스트에서 삭제해보자.
del youtuber[6]
print(youtuber)

## 리스트 제어하기5: 리스트 슬라이싱
## 방법: 리스트이름[처음:끝+1]
## 연습문제>> 처음~3번쨰, 2번째~끝, 3번째~4번째에 위치한 유투버들만, 그리고(':'를 활용하여) 리스트 전체을 출력해보자.
print(youtuber[:6])
'''
## 리스트 제어하기6: 리스트 길이 구하기
## 방법: len(리스트이름)
## 연습문제>> 현재 리스트에 포함된 데이터의 개수를 구해보자
print(len(youtuber))

## 리스트 제어하기7: 리스트 정렬하기
## 방법1: 리스트이름.sort()  <- 오름차순 정렬
## 방법2: 리스트이름.sort(reverse=True)  <- 내림차순 정렬
## 연습문제>> 유투버들을 오름차순과 내림차순으로 정렬한 결과를 각각 출력해보자
youtuber.sort()
print(youtuber)
youtuber.sort(reverse=True)
print(youtuber)
'''

## 리스트 mission1
## :RGB 색상(red, green,blue)을 리스트에 저장하고
##  turtle 모듈을 활용하여 색상이 서로 다른 직선을 그려보자
##  (설정: 굵기(30), 선 길이(200))

import turtle

color = ['red', 'green', 'blue']
win = turtle.Screen()
win.setup(600, 600)
t = turtle.Turtle('turtle')
t.pensize(30)

t.penup()
t.pencolor(color[0])
t.pendown()
t.fd(200)

t.penup()
t.setpos(0, 30)
t.pencolor(color[1])
t.pendown()
t.fd(200)

t.penup()
t.setpos(0, 60)
t.pencolor(color[2])
t.pendown()
t.fd(200)

win.mainloop()


## 리스트 mission2
## 다음은 1번~5번 학생의 1분간 턱걸이 개수이다

pull_up = [3, 16, 2, 5, 10, 7]
## 1번 문제: 7번째 학생의 턱걸이 개수가 9라고 할 때, 이를 리스트에 추가해보자
pull_up.append(9)
print(pull_up)
## 2번 문제: 2번 학생의 재측정 결과 20개의 턱걸이를 하였다. 리스트에 데이터를 수정해보자
pull_up[1] = 20
print(pull_up)
## 3번 문제: 3~7번까지의 학생의 턱걸이 갯수만을 뽑아 temp 변수에 저장하고 출력해보자
temp = pull_up[2:]
print(temp)
## 4번 문제: 학생들의 턱걸이 횟수 데이터를 오름차순으로 정렬
pull_up.sort()
print(pull_up)
