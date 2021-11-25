import pyautogui

# file_menu = pyautogui.locateOnScreen("add_terminal.png")
# print(file_menu)
# pyautogui.click(file_menu)


# screen = pyautogui.locateOnScreen("add_terminal.png")
# print(screen)

for i in pyautogui.locateAllOnScreen("chec_kbox.png"):
    print(i)
    pyautogui.click(i)


# 속도 개선 
# 1.Gray Scale
# trash_icon = pyautogui.locationOnScreen("trash_icon.pgn", grayscae=True)
# pyautogui.MoveTo(trash_icon)
# # 2.범위 지정 
# trash_icon = pyautogui.locationOnScreen("trash_icon", region(1488,623,1881,600))
# 3. 정확도 조정 
# open cv 설치하고 confidence 옵션을 준다. 
# run_btn = pyautogui.locationOnScreen("run_btn.png", confidence= 0.9) # 90% 
# pyautogui.MoveTo(run_btn)