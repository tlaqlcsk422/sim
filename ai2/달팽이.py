#백준 2869번 달팽이

A, B, V = map(int, input().split())
now = 0     #현재 올라가 있는 높이
days = 0   #며칠 지났는지 세어주는 변수

while True:
    days += 1
    now += A
    if now >= V:
        break
    else:
        now -= B

print(days)
