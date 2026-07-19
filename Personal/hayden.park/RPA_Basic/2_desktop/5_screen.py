import pyautogui as pag

# 스크린 샷 찍기
# img = pag.screenshot()
# img.save("screenshot.png") # 파일로 저장

# pag.mouseInfo()
# 22,14 60,169,242 #3CA9F2
pixel = pag.pixel(22, 14)
# print(pixel)

print(pag.pixelMatchesColor(22, 14, (60, 169, 242)))
# print(pag.pixelMatchesColor(22, 14, pixel))
# print(pag.pixelMatchesColor(22, 14, (60, 169, 243)))
