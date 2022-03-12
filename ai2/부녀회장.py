test = int(input())

for _ in range(test):
    floor = int(input())
    ho = int(input())
    f_n = list(range(1,ho+1))   #0층 인덱스 만들기

    for i in range(floor):
        for j in range(1, ho):
            f_n[j] += f_n[j-1]
        print(f_n)
    print(f_n[-1])  #인덱스의 맨 마지막 -> -1
