N = int(input())
num = N #앞으로 계속 변하게 될 변수
count = 0 #몇번째 사이클인지 저장

while True:
    a = num // 10   #10의 자리 숫자 구하기
    b = num % 10 #1의 자리 숫자
    c = (a + b) % 10
    num = b *10 + c
    count += 1
    if(num == N):
        break

print(count)
