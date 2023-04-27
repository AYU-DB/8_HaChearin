# 집합(set)
# 중복 안 됨, 순서 없음

mySet = {1, 2, 3, 3, 3}
print(mySet)

# 자바 할 수 있는 사람
java = {"a", "b", "c"}
# 파이썬 할 수 있는 사람
python = set(["a", "d"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합
print(python - java)
print(java - python)
print(java.difference(python))

# python에 사람 추가
python.add("b")
print(python)

# java에 사람 제거
java.remove("b")
print(java)