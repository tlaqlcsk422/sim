import itertools
from functools import reduce

def insert_operation(length, input_num, input_oper):
    #입력받은 값 list int형으로 변환
    input_num = input_num.split(' ')
    input_oper = input_oper.split(' ')
    input_num = list(map(int, input_num))
    input_oper = list(map(int, input_oper))
    #dict value -> lambda func
    ops = {"0": (lambda x,y: x+y), "1": (lambda x,y: x-y),
           "2":(lambda x,y: x*y),"3":(lambda x,y: x/y)}
    oper_permutation = []
    result = []
    #input_oper[index]의 value>0 면 oper_permutation에 'index'를 value개 만큼 추가
    list(oper_permutation.extend([str(index)]*value) for index, value in enumerate(input_oper) if value > 0)
    #경우의 수를 뽑아줌 itertools.permutations
    permutation = [list(x) for x in set(itertools.permutations(oper_permutation))]
    #경우의 수를 돌려

    for i in permutation:
        #print(permutation)
        #x ops[permutation value](연산자) y를 input_num을 대입해 쭉 계산해 result에 넣어줌
            #reduce(함수, 데이터): 여러개의 데이터를 대상으로 누적 집계
            #i.pop(): permutation의 마지막 값 취득 후 삭제
        result.append(reduce(lambda x,y: ops[i.pop()](x,y), input_num))
        #print('result: ',result)
    print(str(max(result))+"\n"+str(min(result)))

n = int(input('number의 개수: ' ))
numbers = input('number 입력: ')
arithmetics = input('사칙연산 입력: ')
insert_operation(n, numbers, arithmetics)


