'''
# key, value 순으로.
cabinet = {3:"박서현", 100:"허수진"}
print(cabinet[3])
print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet[5]) << 오류남

# 얘는 오류가 나는 게 아니라 None을 출력함
print(cabinet.get(5))
# get을 쓸 경우, 비어있는 index에도 값을 넣어서 출력 가능함
print(cabinet.get(6, "사용가능"))

print(3 in cabinet) # True
print(5 in cabinet) # False
'''
# key 값은 숫자말고 문자열도 가능함.
cabinet = {"A-3":"박서현", "C-100":"허수진"}
print(cabinet["A-3"])
print(cabinet["C-100"])

# 추가
cabinet["A-3"] = "최수빈"
cabinet["C-20"] = "박서현"
print(cabinet)

# 삭제
del cabinet["C-100"]
print(cabinet)

# key만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())

# key, value 같이 출력
print(cabinet.items())

# 모든 값 삭제
cabinet.clear()
print(cabinet)