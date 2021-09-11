import pygame
import os
import random
from pygame import font
from pygame.constants import BUTTON_LEFT, KEYDOWN
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
ddong_count = 0

# 방어막 아이템 생성
cloaking = pygame.image.load(os.path.join(image_path,"venci.png"))
cloaking_size = cloaking.get_rect().size
cloaking_width = cloaking_size[0]
cloaking_height = cloaking_size[1]
cloaking_x_pos = random.randint(0,screen_width-cloaking_width)
cloaking_y_pos = 0
cloaking_speed = 10
cloaking_list = []
cloaking_occur = False

#신발 (이동속도 증가) 아이템 생성
jordany = pygame.image.load(os.path.join(image_path,"jordany1.png"))
jordany_size = jordany.get_rect().size
jordany_width = jordany_size[0]
jordany_height = jordany_size[1]
jordany_x_pos = random.randint(0,screen_width-jordany_width)
jordany_y_pos = -1 *jordany_height
jordany_speed = 1
# jordany_occur = False

# 캐릭터 이동 방향
to_x = 0

# 이동 속도
character_x_speed = 5

#폰트
game_font = pygame.font.Font(None,40)
gameover_font = pygame.font.SysFont('malgungothicsemilight', 35)

_running = True
running = True
while _running:
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
            ddong_count += 1

        cloaking_y_pos += cloaking_speed
        if cloaking_y_pos > screen_height-cloaking_height:
            cloaking_y_pos = screen_height-cloaking_height
        
        jordany_y_pos += jordany_speed
        if jordany_y_pos > screen_height -jordany_height:
            jordany_y_pos = screen_height -jordany_height
        # 4. 충돌 처리

        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        ddong_rect = ddong.get_rect()
        ddong_rect.left = ddong_x_pos
        ddong_rect.top = ddong_y_pos

        cloaking_rect = cloaking.get_rect()
        cloaking_rect.left = cloaking_x_pos
        cloaking_rect.top = cloaking_y_pos

        jordany_rect = jordany.get_rect()
        jordany_rect.left = jordany_x_pos
        jordany_rect.top = jordany_y_pos

        if character_rect.colliderect(cloaking_rect):
            cloaking_x_pos = character_x_pos
            cloaking_occur = True

        if character_rect.colliderect(ddong_rect):
            if cloaking_occur == True:
                ddong_y_pos = 0
                cloaking_occur = False
                cloaking_y_pos = 0
                cloaking_x_pos = random.randint(0,screen_width-cloaking_width)
            else:         
                running = False

        if character_rect.colliderect(jordany_rect):
            jordany_y_pos = 0
            character_x_speed += 5
        
        # 피한 똥 갯수
        ddong_number = game_font.render(str(ddong_count),True,(0,0,0))

        # 5. 화면에 그리기
        screen.blit(background,(0,0))
        screen.blit(character,(character_x_pos,character_y_pos))
        screen.blit(ddong,(ddong_x_pos,ddong_y_pos))
        screen.blit(ddong_number, (10,10))
        screen.blit(cloaking,(cloaking_x_pos,cloaking_y_pos))
        screen.blit(jordany,(jordany_x_pos,jordany_y_pos))
        pygame.display.update()
    
    
    game_over=gameover_font.render("게임 점수는 " +str(ddong_count) + "입니다." \
        , True , (0,0,0))
    game_over2 = gameover_font.render("다시 하시겠습니까?" , True,(0,0,0))
    screen.blit(background,(0,0))
    screen.blit(game_over,(80 , screen_height/2- 50))
    screen.blit(game_over2,(90,screen_height/2 - 10))
    
    pygame.display.update() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            _running = False
pygame.quit()

#준비물 

# background1.png -> 640x480
# ddong.png jordany1.png venci.png -> 40x40
# changyeop.png ->적당한 크기
# 위 준비물을 pygame1_image 폴더에 넣으면 사용할 수 있다.