import pyautogui
# print(pyautogui.position())

# pyautogui.click(64, 17, duration=1) # 1초 동안 (64, 17) 좌표로 마우스 이동 후  클릭
# pyautogui.click()
# pyautogui.mouseDown() # Drag & Drop 시 mouseDown & Up 활용
# pyautogui.mouseUp()

# pyautogui.doubleClick()
# pyautogui.click(clicks=500)

# 그림판과 같이 띄워서 선 그리기
# pyautogui.moveTo(200, 200)
# pyautogui.mouseDown()
# pyautogui.moveTo(300, 300)
# pyautogui.mouseUp()


# pyautogui.rightClick()
# pyautogui.middleClick()

# 마우스 드래그
# print(pyautogui.position())
# pyautogui.moveTo(987, 125)
# pyautogui.drag(100, 0) # 현재 위치 기준으로 x 100 만큼, y 0만큼 이동
# pyautogui.drag(100, 0, duration=0.25) # 너무 빨라서 동작이 안될때는 duration 지정
# pyautogui.dragTo(1087, 225, duration=0.25)

pyautogui.sleep(3) # 3초 대기
pyautogui.scroll(300) # 마우스 스크롤