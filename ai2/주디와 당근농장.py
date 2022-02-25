#16433번 주디와 당근농장

N,R,C = map(int,input().split())
field = [[0 for j in range(N)] for i in range(N)]

if (R + C) % 2 == 0:
    for i in range(1,N+1):
        for j in range(1,N+1):
            if (i + j) % 2 == 0:
                field[i-1][j-1] = 'v'
            else:
                field[i-1][j-1] = '.'
else:
    for i in range(1,N+1):
        for j in range(1,N+1):
            if (i + j) % 2 == 0:
                field[i-1][j-1] = '.'
            else:
                field[i-1][j-1] = 'v'

for i in field:
    print(i)


'''
if (R + C) % 2 == 0:
    for i in range(N):
        if i % 2 == 0:
            print("v." * (N // 2) + 'v' * (N % 2))
        else:
            print(".v" * (N // 2) + '.' * (N % 2))

else:
    for i in range(N):
        if i % 2 == 1:
            print("v." * (N // 2) + 'v' * (N % 2))
        else:
            print(".v" * (N // 2) + '.' * (N % 2))
'''

