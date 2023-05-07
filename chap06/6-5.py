# 출석 번호 1, 2.. 일 때 101, 102로 저장 후 출력
student = [1,2,3,4]
print(student)
student = [i+100 for i in student]
print(student)

# 각 이름을 길이로 변환
student = ["프로그래머", "사회선생님", "미용사", "간호사"]
print(student)
student = [len(i) for i in student]
print(student)

# 학생 이름을 대문자로 변환
student = ["aaA", "bBb", "Ccc"]
print(student)
student = [i.upper() for i in student]
print(student)