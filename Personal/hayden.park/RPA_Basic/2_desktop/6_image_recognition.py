from PIL.ImageOps import grayscale
import pyautogui as pag

# # 이미지 위치를 찾아서 정보를 반환
# file_menu = pag.locateOnScreen("file_menu.png")
# print(file_menu)
# pag.click(file_menu)


# trash_icon = pag.locateOnScreen("trash.png")
# pag.moveTo(trash_icon)


# for i in pag.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pag.click(i)


# checkbox = pag.locateOnScreen("checkbox.png")
# pag.click(checkbox)


# 속도 개선
# 1. GrayScale
# trash_icon = pag.locateOnScreen("trash.png", grayscale=True)
# pag.moveTo(trash_icon)

# 2. 범위 지정
# trash_icon = pag.locateOnScreen("trash.png", region=(1818, 704, 1878-818, 783-704))
# pag.moveTo(trash_icon)

# # 3. 정확도 조정
# run_btn = pag.locateOnScreen("run_button.png", confidence=0.7)
# pag.moveTo(run_btn)

# 자동화 대상이 바로 보여지지 않는 경우