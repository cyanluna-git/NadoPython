import pyautogui

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

# pyautogui.write("12345")
# pyautogui.write("NadoCoding", interval=0.25)

# pyautogui.write(["t","e","s","t","left","left","right","l","a","enter"],interval=0.25)

# 특수문자 
# shift 4 -> $
# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")

#조합키 (핫키)
# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("c")
# pyautogui.keyUp("c")
# pyautogui.keyUp("ctrl")

# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("v")
# pyautogui.keyUp("v")
# pyautogui.keyUp("ctrl")

# pyautogui.hotkey("ctrl", "alt", "shift", "a")
# pyautogui.hotkey("ctrl","a")

import pyperclip
# pyperclip.copy("나도코딩")
# pyautogui.hotkey("ctrl","v")

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

my_write("나머링ㅁㄹ")
