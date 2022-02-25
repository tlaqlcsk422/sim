## 백준 1924번 2007년
day_of_week = ['일','월','화','수','목','금','토']
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m, d = map(int, input().split())
Day = 0

for i in range(0, m-1):
    Day += month[i]

Day = (Day + d) % 7

print(day_of_week[Day])