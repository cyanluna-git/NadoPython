import pickle
# profile_file = open("profile.pickle", "wb") # 피클을 쓰기위해서는 항상 바이너리로 정의 해줘야한다. 
# profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # 프로필에 있는 정보를 file에 저장
# profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()
