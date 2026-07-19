import pyautogui as pag

# pag.mouseInfo() # 마우스가 위치한 곳의 정보를 얻을 때 사용


#fail-safe 기능 : 사용자에 의한 매크로 종료
# pag.FAILSAFE = False

pag.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용

for i in range(10):
    pag.move(100, 100)
    # pag.sleep(1)
