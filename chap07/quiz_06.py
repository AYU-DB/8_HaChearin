averange = 0
def std_weight(height, gender):
    global averange
    if gender == "남":
        averange = height * height * 22
    if gender == "여":
        averange = height * height * 21
    return averange

height = 172
gender = "여"
weight = round(std_weight(height / 100, gender), 2)

print("키: {0}\n성별: {1}\n평균 몸무게: {2}\n" .format(height, gender, weight))