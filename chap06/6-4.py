absent = [2,5] # 2번 5번은 결석
noBook = [7] # 책이 없음
for student in range(1, 11):
    if student in absent:
        continue
    print("{0}, 책을 읽어봐".format(student))
    if student in noBook:
        print("제가 {0}번 책을 깜빡하고 안 가져왔습니다.".format(student))
        print("그럼 {0}번은 옆 사람 책 빌려서 읽어.".format(student))
