score_file = open("score.txt", "w", encoding = "utf8")
print("수학: 0", file = score_file)
print("영어: 50", file = score_file)
score_file.close()

score_file = open("score.txt", "a", encoding = "utf8")
score_file.write("과학: 80\n코딩: 100")
score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.read())
score_file.close()

print("\n")

score_file = open("score.txt", "r", encoding = "utf8")
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄로 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄로 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄로 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="") # 줄별로 읽기, 한 줄로 읽고 커서는 다음 줄로 이동
score_file.close()

print("\n")

score_file = open("score.txt", "r", encoding = "utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()