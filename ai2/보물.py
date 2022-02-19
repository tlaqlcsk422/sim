#백준 1026번 보물

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

#######
answer = 0
for i in range(0,N):
    answer += A[i] * B[i]

print(answer)
######
#앞의 4줄을
#print(sum([A[i]*B[i] for i in range(N)]))
#으로 간결하게 쓸 수 있음