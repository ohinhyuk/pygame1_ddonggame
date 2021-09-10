import pygame
import os
import random
# 기본 초기화
pygame.init()


# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기 게임")

# FPS
clock = pygame.time.Clock()

########################################################################

# 1.사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
# 배경 만들기
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path,"pygame1_image")
background = pygame.image.load(os.path.join(image_path,"background1.png"))

# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path,"changyeop.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width)/2 - character_width/2
character_y_pos = screen_height - character_height

#똥 만들기
ddong = pygame.image.load(os.path.join(image_path,"ddong.png"))
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = random.randint(0,screen_width - ddong_width)
ddong_y_pos = 0 
ddong_speed = 10

# 캐릭터 이동 방향
to_x = 0

# 이동 속도
character_x_speed = 5

running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드,마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_x_speed
            elif event.key ==pygame.K_RIGHT:
                to_x += character_x_speed
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
    # 3. 게임 캐릭터 위치 정의

    character_x_pos += to_x

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    ddong_y_pos += ddong_speed
    if ddong_y_pos >screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0,screen_width-ddong_width)
        #점점 빨라지게
        ddong_speed += 1
    # 4. 충돌 처리

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    if character_rect.colliderect(ddong_rect):
        print("충돌했어요")
        running = False
    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(ddong,(ddong_x_pos,ddong_y_pos))
    pygame.display.update()

pygame.quit()

#쉴드 추가하기