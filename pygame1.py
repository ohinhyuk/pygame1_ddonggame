import pygame
import os
import random
from pygame import font
from pygame import image
from pygame.constants import BUTTON_LEFT, KEYDOWN
import time

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
ddong_width = ddong_size[0] *2
ddong_height = ddong_size[1] *2
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

#스킬
#1)마법+메테오

magic = pygame.image.load(os.path.join(image_path,"magic.png"))
magic_size = magic.get_rect().size
magic_width = magic_size[0]
magic_height = magic_size[1]
magic_x_pos = random.randint(0,screen_width-magic_width)
magic_y_pos = screen_height - magic_height


metteo = pygame.image.load(os.path.join(image_path,"metteo.png"))
metteo_size = metteo.get_rect().size
metteo_width = metteo_size[0]
metteo_height = metteo_size[1]
metteo_x_pos = character_x_pos +character_width/2 -metteo_width/2
metteo_y_pos = -3000
metteo_speed = 0
metteo_on = False

#2) 표창

phochang = pygame.image.load(os.path.join(image_path,"phochang.png"))
phochang_size = phochang.get_rect().size
phochang_width = phochang_size[0]
phochang_height = phochang_size[1]
phochang_x_pos = random.randint(0,screen_width-phochang_width)
phochang_y_pos = screen_height - phochang_height
phochang_speed = 0
phochang_on = False

#3) 부메랑

bumerang = pygame.image.load(os.path.join(image_path,"bumerang.png"))
bumerang_size = bumerang.get_rect().size
bumerang_width = bumerang_size[0]
bumerang_height = bumerang_size[1]
bumerang_x_pos = -1 * bumerang_width -100
bumerang_y_pos = screen_height/2 -bumerang_height/2
bumerang_speed = -30
bumerang_dir = 1
bumerang_on = False

bumerang_get = pygame.image.load(os.path.join(image_path,"bumerang_get.png"))
bumerang_get_size = bumerang_get.get_rect().size
bumerang_get_width = bumerang_get_size[0]
bumerang_get_height = bumerang_get_size[1]
bumerang_get_x_pos = random.randint(0,screen_width-bumerang_get_width)
bumerang_get_y_pos = screen_height - bumerang_get_height
bumerang_get_on = False
# 캐릭터 이동 방향
to_x = 0

# 이동 속도
character_x_speed = 5

#폰트
game_font = pygame.font.Font(None,40)
gameover_font = pygame.font.SysFont('malgungothicsemilight', 35)

print("1. 메테오 2. 표창 3. 부메랑")
number=input("어떤 무기를 선택하시겠습니까? 숫자를 입력하세요 :")

if number == "1":
    _running = True
    running = True
elif number == "2":
    _running = True
    running = True
elif number == "3":
    _running = True
    running = True
else :
    _running = False
    running = False


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
                elif event.key ==pygame.K_SPACE:
                    
                        
                        #1) 메테오 + 마법
                    if number =="1":    
                        if metteo_on ==True:    
                            metteo_x_pos = character_x_pos +character_width/2 -metteo_width/2
                            metteo_speed = 200
                            metteo_on = False
                            #2) 표창
                    elif number =="2":
                        if phochang_on ==True:
                            phochang_speed = -200
                            phochang_on = False
                            #3 부메랑
                    elif number =="3":
                        if bumerang_on ==True and bumerang_get_on ==True:
                            bumerang_speed = 30 * bumerang_dir
                            bumerang_on = False
                        pass
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
        #1#메테오
        if number =="1":
            metteo_y_pos += metteo_speed
            if metteo_y_pos > screen_height:
                metteo_y_pos = -3000
                metteo_on = True
                metteo_speed = 0
            
        #2 표창
        elif number =="2":
            phochang_y_pos += phochang_speed
            if phochang_y_pos <-500:
                phochang_y_pos = screen_height - phochang_height
                phochang_x_pos = character_x_pos + character_width/2 -phochang_width/2
                phochang_on = True
                phochang_speed = 0
        #3부메랑
        elif number =="3":
            bumerang_x_pos += bumerang_speed
            if bumerang_x_pos > screen_width +100 :
                bumerang_x_pos = screen_width + 98
                bumerang_speed = 0
                bumerang_dir = -1
                bumerang_on =True

            elif bumerang_x_pos < (-1 * bumerang_width) -100:
                bumerang_x_pos = (-1 * bumerang_width) -98
                bumerang_speed = 0
                bumerang_dir = 1
                bumerang_on =True

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
        #1)메테오 +마법
        if number =="1":
            metteo_rect = metteo.get_rect()
            metteo_rect.left = metteo_x_pos
            metteo_rect.top = metteo_y_pos

            magic_rect = magic.get_rect()
            magic_rect.left = magic_x_pos
            magic_rect.top = magic_y_pos

        # #2표창
        elif number =="2":
            phochang_rect = phochang.get_rect()
            phochang_rect.left = phochang_x_pos
            phochang_rect.top = phochang_y_pos

        #3부메랑
        elif number =="3":
            bumerang_rect = bumerang.get_rect()
            bumerang_rect.left = bumerang_x_pos
            bumerang_rect.top = bumerang_y_pos

            bumerang_get_rect = bumerang_get.get_rect()
            bumerang_get_rect.left = bumerang_get_x_pos
            bumerang_get_rect.top = bumerang_get_y_pos

        if character_rect.colliderect(cloaking_rect):
            cloaking_x_pos = 10
            cloaking_y_pos = 50
            cloaking_speed = 0
            cloaking_occur = True

        if character_rect.colliderect(ddong_rect):
            if cloaking_occur == True:
                ddong_x_pos = random.randint(0,screen_width-ddong_width)
                ddong_y_pos = 0
                cloaking_occur = False
                cloaking_y_pos = 0
                cloaking_x_pos = random.randint(0,screen_width-cloaking_width)
                cloaking_speed = 10
            else:         
                running = False

        if character_rect.colliderect(jordany_rect):
            jordany_y_pos = 0
            character_x_speed += 5
        

        #1)메테오+마법
        if number =="1":
            if character_rect.colliderect(magic_rect):
                metteo_on = True
                magic_x_pos = character_x_pos
            if metteo_rect.colliderect(ddong_rect):
                ddong_count +=1
                ddong_speed +=1
                ddong_x_pos = random.randint(0,screen_width - ddong_width)
                ddong_y_pos = 0

        #2 표창
        elif number =="2":
            if character_rect.colliderect(phochang_rect):
                phochang_x_pos = character_x_pos + character_width/2 - phochang_width/2
                phochang_on =True
            if phochang_rect.colliderect(ddong_rect):
                ddong_count +=1
                ddong_speed +=1
                ddong_x_pos = random.randint(0,screen_width - ddong_width)
                ddong_y_pos = 0

        #3 부메랑
        elif number =="3":
            if bumerang_rect.colliderect(ddong_rect):
                ddong_count +=1
                ddong_speed +=1
                ddong_x_pos = random.randint(0,screen_width - ddong_width)
                ddong_y_pos = 0
            if character_rect.colliderect(bumerang_get_rect):
                bumerang_get_on = True
                bumerang_get_x_pos = character_x_pos + character_width/2 - bumerang_get_width/2


        # 피한 똥 갯수
        ddong_number = game_font.render(str(ddong_count),True,(0,0,0))

        # 5. 화면에 그리기
        screen.blit(background,(0,0))
        screen.blit(character,(character_x_pos,character_y_pos))
        screen.blit(ddong,(ddong_x_pos,ddong_y_pos))
        screen.blit(ddong_number, (10,10))
        screen.blit(cloaking,(cloaking_x_pos,cloaking_y_pos))
        screen.blit(jordany,(jordany_x_pos,jordany_y_pos))
        
        #1)메테오 + 마법
        if number == "1":
            screen.blit(metteo,(metteo_x_pos,metteo_y_pos))
            screen.blit(magic,(magic_x_pos,magic_y_pos))
        
        #2) 표창
        elif number =="2":
            screen.blit(phochang,(phochang_x_pos,phochang_y_pos))

        #3)부메랑
        elif number =="3":
            screen.blit(bumerang,(bumerang_x_pos,bumerang_y_pos))
            screen.blit(bumerang_get,(bumerang_get_x_pos,bumerang_get_y_pos))
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



#표창 속도를 늦춰야 부딪히겠구나 띄엄띄엄 움직이니까
#알림으로 어떤 무기 선택할지 받아오고 그에 맞게 case 함수로 어떤 무기 쓸지 선택
                        