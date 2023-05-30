averange = 0
def std_weight(height, gender):
    global averange
    if gender == '남':
        averange = height * height * 22
    if gender == '여':
        averange = height * height * 21

print    