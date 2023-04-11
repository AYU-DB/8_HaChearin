python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "C"))

index = python.index("n")
print(index)
# 첫 번째 n 말고 두 번째 n의 위치
index = python.index("n", index + 1)
print(index)

# 없는 단어를 찾을 때 find와 index의 차이

# find는 결과가 -1 이지만
# index는 오류가 뜨면서 프로그램을 종료함
print(python.find("Java"))
# print(python.index("Java"))

# n이 몇 번 나왔는지 셈
print(python.count("n"))