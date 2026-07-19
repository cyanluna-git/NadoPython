import pyautogui

# pyautogui.moveTo(100,100)
# pyautogui.moveTo(200,200, duration=1)
# pyautogui.moveTo(300,700, duration=1)

#상대 좌표로 이동
pyautogui.moveTo(100,100)
print(pyautogui.position())
pyautogui.move(100,100,duration=0.25)
print(pyautogui.position())
pyautogui.move(100,100, duration=0.25)

p = pyautogui.position()
print(p[0],p[1])
print(p.x, p.y)
