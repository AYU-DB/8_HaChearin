with open("study.txt", "w", encoding="utf-8") as study_file:
    study_file.write("파이썬 하는 중")

with open("study.txt", "r", encoding="utf-8") as study_file:
    print(study_file.read())