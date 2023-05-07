# 출석 번호 1, 2.. 일 때 101, 102로 저장 후 출력
student = [1,2,3,4]
print(student)
student = [i+100 for i in student]
print(student)

# 학생 이름을 길이로 변환
student = ["프로그래머" "사회 선생님" "미용사" "간호사"]
student = [len(i) for i in student]
print(student)
