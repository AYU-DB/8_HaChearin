gun = 10

def checkpoint(soldiers): #경계근무
    global gun #전역 변수의 gun을 함수에서 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))

print("전체 총: {0}".format(gun))
checkpoint(2) # 2명이 경계근무 나감
print("남은 총: {0}".format(gun))