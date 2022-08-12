#리스트 복습문제
#1. movie_rank 이름의 리스트에 다음과 같은 내용을 저장해보기
# 닥터 스트레인지
# 스플릿
# 럭키
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]

#2. movie_rank 리스트에 배트맨을 추가하기
#append
movie_rank.append("배트맨")
print(movie_rank)

#3. movie_rank 리스트에서 "스플릿"과 "럭키" 사이에 "슈퍼맨"을 추가하기
movie_rank.insert(2, "슈퍼맨")
print(movie_rank)

movie_rank.insert(4,"탑건")
print(movie_rank)

#4. movie rank 리스트에서 "럭키" 삭제하기
del movie_rank[3]
print(movie_rank)

print("----------------------------------")
#5. num 리스트에서 최댓값과, 최솟값, 평균을 출력하기
num = [1,2,3,4,5,6,7,8,9,10]
#max
print("max: ", max(num))
#min
print("min: %d"%min(num))
#average = 총합 / 개수
#총합 sum
#개수 len
average = sum(num) / len(num)
print(f"avg: {average}")

#6. num 리스트 원소들의 합을 출력하라
print(sum(num))

#7. cook 리스트에 저장된 데이터의 개수를 출력하기
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자",
        "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전",
        "곱창", "햄버거", "떡볶이", "감자탕"]
print("cook 리스트의 길이: ",len(cook))

print("-------------------------------------")
#딕셔너리 복습문제
#1. 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하기
# 메로나 - 1000
# 폴라포 - 1200
# 빵빠레 - 1800
ice = {"메로나":1000, "폴라포":1200, "빵빠레":1800}

#2. ice 딕셔너리에 아래 정보를 추가하기
# 죠스바 - 1200
# 월드콘 - 1500
ice["죠스바"] = 1200
ice["월드콘"] = 1500
print(ice)

#3. ice 딕셔너리에서 메로나 가격만 출력하기
#출력 예시 -> 메로나 가격: 1000
print("메로나 가격: ", ice["메로나"])

#4. ice 딕셔너리에서 빵빠레의 가격을 2000원으로 수정하기
ice["빵빠레"] = 2000
print(ice)

#5. ice 딕셔너리에서 폴라포를 삭제하기
del ice["폴라포"]
print(ice)
