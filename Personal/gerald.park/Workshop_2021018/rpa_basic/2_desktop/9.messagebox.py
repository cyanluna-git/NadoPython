import pyautogui

# print("곧 시작합니다..")
# pyautogui.countdown(3)
# print("자동화시작")

# # pyautogui.alert("자동화 수행에 실패하였습니다.","경고") #확인버튼만 있음 
# result = pyautogui.confirm("계속 진행 하시겠습니까?", "확인")
# print(result)

# #사용자 입력 받기
# result = pyautogui.prompt("파일명을 뭐?", "입력")
# print(result)

result = pyautogui.password("암호입력")
print(result)