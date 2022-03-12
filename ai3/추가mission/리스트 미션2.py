import random

#문자열을 띄어쓰기대로 잘라서 리스트에 저장
item = list(input("리스트에 무엇을 넣을까요? ").split())
# itme 리스트에서 랜덤으로 하나 선택
get_item = random.choice(item)

player = input("무슨 아이템이 뽑힐까요? ")

if get_item == player:
    print(f"뽑힌 아이템은 {get_item}입니다. 맞췄어요!")
else:
    print(f"뽑힌 아이템은 {get_item}입니다. 틀렸어요ㅜㅜ")