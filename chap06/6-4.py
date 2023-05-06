absent = [2,5] # 2번 5번은 결석
noBook = [7] # 책이 없음
blood = [8] # 상처나서 피 남
for student in range(1, 11):
    if student in absent:
        continue
    print("{0}번, 책 읽어봐".format(student))
    if student in noBook:
        print("제가 {0}번인데 책을 깜빡하고 안 가져왔습니다.".format(student))
        print("그럼 {0}번은 옆 사람 책 빌려서 읽어.".format(student))
    elif student in blood:
        print("선생님! {0}번 피 나요!".format(student))
        print("{0}번은 선생님이랑 보건실 가고 나머지는 자율수업 하고 있어.".format(student))
        break