import pickle
profile_file = open("profile.pickle", "wb")
profile = {"이름":"a", "나이":"22", "취미":["운동", "노래듣기", "게임"]}
print(profile)

# profile 에 있는 정보를 file 에 저장
pickle.dump(profile, profile_file)
profile_file.close()


profile_file = open("profile.pickle", "rb")

# file 에 있는 정보를 profile 에 불러오기
profile = pickle.load(profile_file)
print(profile)
profile_file.close()