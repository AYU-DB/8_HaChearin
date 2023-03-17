# 참, 거짓
print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not False)
print(not (5 < 10)) # False

print("\n")

# 애완동물을 소개해보자
animal = "고양이"
nameK = "쿵이"
nameM = "몽이"
ageM = 1
num = 2
is_adult = ageM >= 3

print("저는 " + animal + " " + str(num) + "마리를 키우고 있습니다.")
print("한 마리는 " + nameK + ", 한 마리는 " + nameM + "입니다.")
print(nameM, "는 ", ageM, "살 입니다.")
# , 로 연결하면 띄어쓰기가 자동으로 들어감
print(nameM + "은 어른일까요? " + str(is_adult))
