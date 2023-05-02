weather = input("오늘 날씨는? ")

if weather == "비" or weather == "눈":
    print("우산을 챙기세요.")
     
elif weather == "맑음":
    print("빨래하기 좋은 날씨예요! :)")

elif weather == "미세먼지":
    print("마스크를 챙기세요.")  

else:
    print("준비물 필요 없어요.")

temp = int(input("기온은? "))
if 25 <= temp:
    print("너무 더워요. 야외활동을 자제해주세요.")
elif 5 >= temp:
    print("추워요. 밖에 나가지 마세요.")