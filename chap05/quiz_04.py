from random import*
users = range(1, 21) # 1부터 21까지 생성
# print(type(users))
users = list(users)
# print(type(users))

# print(users)
# shuffle(users)

winners = sample(users, 4) # 4명 중 한 명은 치킨, 나머지는 커피
print("---당첨자 발표---")
print("치킨 당첨자 : {0}" .format(winners[0]))
print("커피 당첨자 : {0}" .format(winners[1:]))
print("---축하합니다!---")