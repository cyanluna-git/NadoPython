# import pickle
# # pickle 사용하여 이진 파일 만들기
# profile_file = open("profile.pickle", "wb") # pickle 쓸 때는 항상 binary type 사용을 위해 wb 로 설정
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile,profile_file) #profile 에 있는 정보를 profile_file 에 저장
# profile_file.close()

# # 이진 파일 가져오기
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file) # 파일에 있는 정보를 profile 에 불러오기
# print(profile)
# profile_file.close()