import pyautogui as pag

w = pag.getWindowsWithTitle("제목 없음")[0] # 메모장 1개 띄운 상태에서 가져옴
w.activate()

# pag.write("12345")
# pag.write("NadoCoding", interval=0.25)
# pag.write("나도코딩") # pyautogui 는 한글은 바로 입력 안됨, 별도 처리 필요

# pag.write(["t","e","s","t","left", "left", "right", "l", "a", "enter"], interval=0.25) # t e s t 순서대로 적고 왼쪽 방향키 2번, 오른쪽 방향키 1번, l a 순서대로 적고 enter 입력
# 사전 정의된 키는 Google 에서 automate the boring stuff 검색하면 찾을 수 있음 (keyboard attribute)


# 특수 문자
# shift 4 -> $ 입력
# pag.keyDown("shift") # shift 키를 누른 상태에서
# pag.press("4") # 숫자 4를 입력하고
# pag.keyUp("shift") # shift 키를 뗀다

# 조합키 (Hot Key)
# pag.keyDown("ctrl")
# pag.keyDown("a")
# pag.keyUp("a") # press("a")
# pag.keyUp("ctrl") # Ctrl + A
# pag.hotkey("ctrl", "alt", "shift", "a") # Ctrl 누르고 > Alt 누르고 > Shift 누르고 > A 누르고 > A 떼고 > Shift 떼고 > Alt 떼고 > Ctrl 떼고
# pag.hotkey("ctrl", "a")


# 한글 입력을 위해 클립보드에 내용 복사 후, 대상에 붙여넣기
import pyperclip
# pyperclip.copy("나도코딩") # "나도코딩" 글자를 클립보드에 저장
# pag.hotkey("ctrl", "v")

def my_write(text):
    pyperclip.copy(text)
    pag.hotkey("ctrl", "v")


my_write("나도코딩")

# 키보드 자동화 프로그램 종료
# win : ctrl + alt + del 키 입력