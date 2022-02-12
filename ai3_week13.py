##연습문제- 구구단 출력하기
# 2 * 1 = 2

    # for i in range(1,10):
    #     print(f"2 * {i}= ",2 * i)
    #     print("2 * %d = %d"%(i,i*2))
    #     print("2 * ",i," = ", i*2)

##소수 찾기
# x = int(input())
# number = list(map(int, input().split()))
# sosu = 0
#
# for num in number:
#     is_prime = True
#     if num > 1:
#         for i in range(2,num):
#             if num % i == 0:
#                 is_prime = False
#         if is_prime == True:
#             sosu += 1
# print(sosu)


#팩토리얼

num = int(input())
fac = 1
for i in range(1,num+1):
    fac *= i
print(fac)

