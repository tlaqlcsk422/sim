## for문/while문 복습
#
# print("-----------------1번------------------------")
# ########### 1번 ##############
# ## 출력결과를 예상하세요
# print(list(range(1,10)))
#
#
# print("-----------------2번------------------------")
# ########## 2번 ##############
# ## 출력결과를 예상하세요
# for i in range(5,15,2):
#     print(i)
#
#
# print("-----------------3번------------------------")
# ########## 3번 ##############
# ## 출력결과를 예상하세요
# A = [[0, 1, 2, 3],
#      [4, 5, 6, 7],
#      [8, 9, 10, 11]]
#
# for i in range(2):
#     for j in range(3):
#         print(A[i][j])
#
# print("-----------------4번------------------------")
# ########## 4번 ###########
# ##출력결과
# a = 10
# while a < 50:
#     a += 10
#     print(a)
#
#
# ###########연습1번###########
#






for i in range(10):
    print("오늘 수업이 너무 기네요")


print(list(range(10)))
print(list(range(2,11,2)))
print(list(range(10,1,-1)))
#
# for char in "안녕하세요":
#     print(char, end="")


# i = 1
# while i < 4:
#     print(i,"꼬마", sep="")
#     i = i + 1
# print("인디언!")

# i = 0
# while i < 10:
#     i = i + 1
#     if i % 2 == 0:
#         continue
#     print(i,end=' ')

num = int(input("구구단 단 수를 입력: "))

for i in range(1,10):
    print(f"{num} * {i} = {num * i}")
















