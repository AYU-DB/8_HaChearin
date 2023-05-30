# 프린트 사이사이에 명령어 sep을 이용해서 단어 삽입하기

print("Python" + "Java")
print("Python", "Java", sep=", ")
print("Python", "Java", "JavaScript", sep=" vs ")
print("이 문장 마지막에는 물음표가 붙습니다", end = "?")

# ljust(숫자) <<< 얘는 글자 뒤에 프린트 되는 공백 개수
print("\n")
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(3), score)