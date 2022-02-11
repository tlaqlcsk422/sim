x = int(input())
number = list(map(int, input().split()))
sosu = 0

for num in number:
    is_prime = True
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime == True:
            sosu += 1

print(sosu)
