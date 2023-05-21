def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {0}\t나이 : {1}\t" .format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)

profile("a", 21, "Python", "Java", "C", "C++", "C#")
profile("b", 22, "Kotlin", "Swift", "", "", "")