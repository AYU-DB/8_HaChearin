# 리스트[]

# 지하철 칸별로 10명, 20명, 30명
'''
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "박명수", "정준하"]
print(subway)

print("박명수가 탑승한 열차칸 번호: " + str(subway.index("박명수") + 1))

# 하하가 다음 정류장에서 다음 칸에 탑승함
# (하하를 subway에 추가함)
subway.append("하하")
print(subway)

# 정형돈은 유재석, 박명수 사이에 탑승
# (정형돈을 유재석, 박명수 사이에 집어 넣음)
subway.insert(1, "정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# (뒤에서 부터 pop 시킴)

print("하차한 사람: " + str(subway.pop()))
print("남은 사람  : " + str(subway))

print("하차한 사람: " + str(subway.pop()))
print("남은 사람  : " + str(subway))

print("하차한 사람: " + str(subway.pop()))
print("남은 사람  : " + str(subway))

print("하차한 사람: " + str(subway.pop()))
print("남은 사람  : " + str(subway))

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print("같은 이름의 사람 수: " + str(subway.count("유재석")))
'''
'''
# 작은 순으로 정렬하기
num_list = [5,4,3,2,1]
num_list.sort()
print(num_list)

# 큰 순으로 정렬하기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)
'''
# 다양한 자료형 함께 사용
mix_list = ["유재석", 20, True]
print(mix_list)

# 리스트 확장 
num_list = [5,4,3,2,1]
num_list.extend(mix_list)
print(num_list)