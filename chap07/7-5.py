'''def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {0}\t나이 : {1}\t" .format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)
    '''
def profile(name, age, *language):
    print("이름: {0}\t나이 : {1}\t" .format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("a", 21, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("b", 22, "Kotlin", "Swift")