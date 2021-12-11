import pygame
pygame.init() # 초기화, 반드시 필요

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load(r"C:\Projects\NadoPython\Personal\hayden.park\NadoCoding\pygame_basic\background.png")

# 이벤트 루프
running = True # 게임 진행여부 확인
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생여부 확인
            running = False
    screen.blit(background, (0,0)) # 배경 그리기
    # screen.fill((0,0,255)) # 화면을 RGB 값으로 채우기
    pygame.display.update() # 게임화면을 다시 그리기

# pygame 종료
pygame.quit()
