url = "http://naver.com"
Str = url.replace("http://" , "")
print(Str)
Str = Str[:Str.index(".")]
print(Str)
pw = Str[:3] + str(len(Str)) + str(Str.count("e")) + "!"
print("{0}의 비밀번호는 {1} 입니다.".format(url, pw))