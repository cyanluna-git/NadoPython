import pygame
pygame.init() # 초기화, 반드시 필요

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game") # 게임 이름

# 이벤트 루프
running = True # 게임 진행여부 확인
while(running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생여부 확인
            running = False


# pygame 종료
pygame.quit()
