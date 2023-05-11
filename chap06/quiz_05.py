# 택시 기사가 승객을 받을 때
from random import *
count = 0
for i in range(1, 51): # 1~50 승객 번호
    time = randrange(5, 51) # 5~51분 소요 시간
    if 5 <= time <=15: # 5~15분 이내의 손님, 탑승 승객 수 +1
       print("[O] {0}번 째 손님 (소요시간: {1}분)".format(i, time))
       count += 1
    else: # 매칭 실패한 경우
        print("[X] {0}번 째 손님 (소요시간: {1}분)".format(i, time))

print("총 탑승 승객: {0} 분 입니다.".format(count))