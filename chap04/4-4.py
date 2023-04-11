'''print("a" + "b")
print("a", "b")'''

# 방법 1
print("나는 만 %d살입니다." %20)
print("나는 만 %s살입니다." %20)
print("%s를 좋아합니다" %"고양이")
print("Apple은 %c로 시작합니다." %"A")

print("나는 %s색과 %s색을 좋아합니다." %("파란", "흰"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아합니다.".format("파란", "흰"))
print("나는 {0}색과 {1}색을 좋아합니다.".format("파란", "흰"))
print("나는 {1}색과 {0}색을 좋아합니다.".format("파란", "흰"))

# 방법 3
print("나는 만 {age}살이며, {color}색을 좋아합니다.".format(age = 20, color = "파란"))
print("나는 만 {age}살이며, {color}색을 좋아합니다.".format(color = "파란", age = 20))

# 방법 4
age = 20
color = "파란"
# 앞에 f를 쓰면 문장 밖에 있는 변수를 쓸 수 있다.
print(f"나는 만 {age}살이며, {color}색을 좋아합니다.")