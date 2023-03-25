from random import *

'''
print(random()) # 0.0 ~ 1.0 미만의 랜덤 수 print 함
print(random() * 10) # 1.0 ~ 10.0 미만 랜덤
'''
print(int(random() * 10)) # 0 ~ 10 이상 랜덤
print(int(random() * 10) + 1) # 1 ~ 10 이상 랜덤
print(int(random() * 45) + 1) # 1 ~ 45 이상 랜덤
print(randrange(1, 46)) # 1 ~ 46 미만 랜덤
print(randint(1, 45)) # 1 ~ 45 이하 랜덤