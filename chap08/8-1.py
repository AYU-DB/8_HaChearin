# 프린트 사이사이에 명령어 sep을 이용해서 단어 삽입하기

print("Python" + "Java")
print("Python", "Java", sep=", ")
print("Python", "Java", "JavaScript", sep=" vs ")
print("이 문장 마지막에는 물음표가 붙습니다", end = "?")

# ljust(숫자) <<< 왼쪽 정렬 후 (글자수 - 숫자)만큼 왼쪾으로 띄어쓰기
# rjust(숫자) <<< 오른쪽 정렬 후 (글자수 - 숫자)만큼 오른쪽으로 띄어쓰기

print("\n")
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject, str(score).rjust(4))

print("\n")
for subject, score in scores.items():
    print(subject.ljust(8), str(score))

# 은행 대기순번표

print("\n")
answer = 10
print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")