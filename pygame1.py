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
screen_width = 1000
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

#똥2
ddong2 = pygame.image.load(os.path.join(image_path,"ddong.png"))
ddong2_size = ddong.get_rect().size
ddong2_width = ddong_size[0] *2
ddong2_height = ddong_size[1] *2
ddong2_x_pos = random.randint(0,screen_width - ddong_width)
ddong2_y_pos = 0 
ddong2_speed = 10
ddong2_count = 0
ddong2_on = False
#똥3
ddong3 = pygame.image.load(os.path.join(image_path,"ddong.png"))
ddong3_size = ddong.get_rect().size
ddong3_width = ddong_size[0] *2
ddong3_height = ddong_size[1] *2
ddong3_x_pos = random.randint(0,screen_width - ddong_width)
ddong3_y_pos = 0 
ddong3_speed = 10
ddong3_count = 0
ddong3_on = False
#똥4
ddong4 = pygame.image.load(os.path.join(image_path,"ddong.png"))
ddong4_size = ddong.get_rect().size
ddong4_width = ddong_size[0] *2
ddong4_height = ddong_size[1] *2
ddong4_x_pos = random.randint(0,screen_width - ddong_width)
ddong4_y_pos = 0 
ddong4_speed = 10
ddong4_count = 0
ddong4_on = False
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
jordany_y_pos = 0
jordany_speed = 20
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

# 200/500/900점일 때 존야 사용 가능
zoneya = pygame.image.load(os.path.join(image_path,"zoneya.png"))
zoneya_get_size = zoneya.get_rect().size
zoneya_width = zoneya_get_size[0]
zoneya_height = zoneya_get_size[1]
zoneya_x_pos = -1 * zoneya_width
zoneya_y_pos = 100
zoneya_on = False

zoneya_background = pygame.image.load(os.path.join(image_path,"zoneya_background.png"))
zoneya_background_get_size = zoneya_background.get_rect().size
zoneya_background_width = zoneya_background_get_size[0]
zoneya_background_height = zoneya_background_get_size[1]
zoneya_background_x_pos = -1 * zoneya_background_width
zoneya_background_y_pos = 50

# 캐릭터 이동 방향
to_x = 0

# 이동 속도
character_x_speed = 8

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

print("로딩중...")
time.sleep(3)
while _running:
    while running:
        dt = clock.tick(30)
        
        # 2. 이벤트 처리 (키보드,마우스 등)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                
                if event.key ==pygame.K_RIGHT:
                    to_x += character_x_speed
                if event.key == pygame.K_LEFT:
                    to_x -= character_x_speed
                if event.key ==pygame.K_SPACE:                        
                        #1) 메테오 + 마법
                    if number =="1":    
                        if metteo_on ==True:    
                            metteo_x_pos = character_x_pos +character_width/2 -metteo_width/2
                            metteo_speed = 200
                            metteo_on = False
                            #2) 표창
                    elif number =="2":
                        if phochang_on ==True:
                            phochang_speed = -50
                            phochang_on = False
                            #3 부메랑
                    elif number =="3":
                        if bumerang_on ==True and bumerang_get_on ==True:
                            bumerang_speed = 30 * bumerang_dir
                            bumerang_on = False                    
                if event.key == pygame.K_3:
                    if zoneya_on ==True:
                        zoneya_on = False
                        zoneya_background_x_pos = screen_width/2 - zoneya_background_width/2
                        zoneya_background_y_pos = screen_height/2 - zoneya_background_height/2
                        time.sleep(2)
                        zoneya_x_pos = -1 * zoneya_width
                        zoneya_y_pos = 100
                        zoneya_background_x_pos = -1 * zoneya_background_width
                        zoneya_background_y_pos = 50
                        ddong_speed = 10
                        ddong2_speed = 10
                        ddong3_speed = 10
                        ddong4_speed = 10
                        if ddong_y_pos > 1:
                            ddong_y_pos = -1 *ddong_height
                        if ddong2_y_pos > 1:
                            ddong2_y_pos = -1 *ddong2_height
                        if ddong3_y_pos > 1:
                            ddong3_y_pos = -1 *ddong3_height
                        if ddong4_y_pos > 1:
                            ddong4_y_pos = -1 *ddong4_height
                        
                        
                        

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0
        # 3. 게임 캐릭터 위치 정의

        #존야 
        if ddong_count ==200 or ddong_count ==500 or ddong_count==900 :
            zoneya_on = True
        
        if zoneya_on == True :
            zoneya_x_pos = 10
        
        character_x_pos += to_x

        if character_x_pos < 0 :
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width
        

        ddong_y_pos += ddong_speed
        if ddong_count > 10:
            ddong2_on = True
        if ddong_count > 80:
            ddong3_on = True
        if ddong_count >120:
            ddong4_on = True
        if ddong2_on ==True:
            ddong2_y_pos += ddong2_speed
        if ddong3_on ==True:
            ddong3_y_pos += ddong3_speed
        if ddong4_on ==True:
            ddong4_y_pos += ddong4_speed
        if ddong_y_pos >screen_height:
            ddong_y_pos = 0            
            ddong_x_pos = random.randint(0,screen_width-ddong_width) 
            ddong_speed += 0.3
            ddong_count += 1          
        if ddong2_y_pos >screen_height:
            ddong2_y_pos = 0
            ddong2_x_pos = random.randint(0,screen_width-ddong_width)
            ddong2_speed += 0.4
            ddong_count += 1
        if ddong3_y_pos >screen_height:
            ddong3_y_pos = 0
            ddong3_x_pos = random.randint(0,screen_width-ddong_width)
            ddong3_speed += 0.6
            ddong_count += 1
        if ddong4_y_pos >screen_height:
            ddong4_y_pos = 0
            ddong4_x_pos = random.randint(0,screen_width-ddong_width)
            ddong4_speed += 1
            ddong_count += 1
        cloaking_y_pos += cloaking_speed
        if cloaking_y_pos > screen_height-cloaking_height:
            cloaking_y_pos = screen_height-cloaking_height
        
        if jordany_y_pos > screen_height -jordany_height:
            jordany_y_pos = screen_height -jordany_height
        #1#메테오
        if number =="1":
            metteo_y_pos += metteo_speed
            if metteo_y_pos > screen_height:
                metteo_y_pos = -3000
                metteo_on = True
                metteo_speed = 0
            if ddong_count > 50:
                metteo = pygame.transform.scale(metteo, (200,200))
                metteo_width = metteo.get_rect().size[0]
                metteo_height = metteo.get_rect().size[1]
            if ddong_count > 100:
                metteo = pygame.transform.scale(metteo, (300,300))
                metteo_width = metteo.get_rect().size[0]
                metteo_height = metteo.get_rect().size[1]
            if ddong_count > 200:
                metteo = pygame.transform.scale(metteo, (400,400))
                metteo_width = metteo.get_rect().size[0]
                metteo_height = metteo.get_rect().size[1]
        #2 표창
        elif number =="2":
            phochang_y_pos += phochang_speed
            if phochang_y_pos <-200:
                phochang_y_pos = screen_height - phochang_height
                phochang_x_pos = character_x_pos + character_width/2 -phochang_width/2
                phochang_on = True
                phochang_speed = 0
            if ddong_count >100:
                phochang = pygame.transform.scale(phochang,(55,55))
                phochang_width = phochang.get_rect().size[0]
                phochang_height = phochang.get_rect().size[1]
                
            
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
            if ddong_count > 150 :
                bumerang = pygame.transform.scale(bumerang,(210,210))
                bumerang_width = bumerang.get_rect().size[0]
                bumerang_height = bumerang.get_rect().size[1]
                bumerang_y_pos = screen_height/2 - bumerang_height/2
            
        # 4. 충돌 처리


        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        ddong_rect = ddong.get_rect()
        ddong_rect.left = ddong_x_pos
        ddong_rect.top = ddong_y_pos

        ddong2_rect = ddong2.get_rect()
        ddong2_rect.left = ddong2_x_pos
        ddong2_rect.top = ddong2_y_pos
        
        ddong3_rect = ddong3.get_rect()
        ddong3_rect.left = ddong3_x_pos
        ddong3_rect.top = ddong3_y_pos
        
        ddong4_rect = ddong4.get_rect()
        ddong4_rect.left = ddong4_x_pos
        ddong4_rect.top = ddong4_y_pos

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
        
        if character_rect.colliderect(ddong2_rect):
            if cloaking_occur == True:
                ddong2_x_pos = random.randint(0,screen_width-ddong2_width)
                ddong2_y_pos = 0
                cloaking_occur = False
                cloaking_y_pos = 0
                cloaking_x_pos = random.randint(0,screen_width-cloaking_width)
                cloaking_speed = 10
            else:         
                running = False
        
        if character_rect.colliderect(ddong3_rect):
            if cloaking_occur == True:
                ddong3_x_pos = random.randint(0,screen_width-ddong3_width)
                ddong3_y_pos = 0
                cloaking_occur = False
                cloaking_y_pos = 0
                cloaking_x_pos = random.randint(0,screen_width-cloaking_width)
                cloaking_speed = 10
            else:         
                running = False
        
        if character_rect.colliderect(ddong4_rect):
            if cloaking_occur == True:
                ddong4_x_pos = random.randint(0,screen_width-ddong4_width)
                ddong4_y_pos = 0
                cloaking_occur = False
                cloaking_y_pos = 0
                cloaking_x_pos = random.randint(0,screen_width-cloaking_width)
                cloaking_speed = 10
            else:         
                running = False

        if character_rect.colliderect(jordany_rect):
            jordany_x_pos = random.randint(0,screen_width - jordany_width)
            jordany_y_pos = 0
            if character_x_speed >23:
                character_x_speed += 0

            else:
                character_x_speed += 5       

        #1)메테오+마법
        if number =="1":
            if character_rect.colliderect(magic_rect):
                metteo_on = True
                magic_x_pos = character_x_pos
            if metteo_rect.colliderect(ddong_rect):
                ddong_count +=1
                ddong_speed +=0.3
                ddong_x_pos = random.randint(0,screen_width - ddong_width)
                ddong_y_pos = 0
                jordany_y_pos += jordany_speed *2
            if metteo_rect.colliderect(ddong2_rect):
                ddong_count +=1
                ddong2_speed +=0.4
                ddong2_x_pos = random.randint(0,screen_width - ddong2_width)
                ddong2_y_pos = 0
                jordany_y_pos += jordany_speed *2
            if metteo_rect.colliderect(ddong3_rect):
                ddong_count +=1
                ddong3_speed +=0.6
                ddong3_x_pos = random.randint(0,screen_width - ddong3_width)
                ddong3_y_pos = 0
                jordany_y_pos += jordany_speed *2
            if metteo_rect.colliderect(ddong4_rect):
                ddong_count +=1
                ddong4_speed +=1
                ddong4_x_pos = random.randint(0,screen_width - ddong4_width)
                ddong4_y_pos = 0
                jordany_y_pos += jordany_speed *2

        #2 표창
        elif number =="2":
            if character_rect.colliderect(phochang_rect):
                phochang_x_pos = character_x_pos + character_width/2 - phochang_width/2
                phochang_on =True
            if phochang_rect.colliderect(ddong_rect):
                ddong_count +=1
                ddong_speed +=0.3
                ddong_x_pos = random.randint(0,screen_width - ddong_width)
                ddong_y_pos = 0
                jordany_y_pos += jordany_speed *4
            if phochang_rect.colliderect(ddong2_rect):
                ddong_count +=1
                ddong2_speed +=0.4
                ddong2_x_pos = random.randint(0,screen_width - ddong2_width)
                ddong2_y_pos = 0
                jordany_y_pos += jordany_speed *4
            if phochang_rect.colliderect(ddong3_rect):
                ddong_count +=1
                ddong3_speed +=0.6
                ddong3_x_pos = random.randint(0,screen_width - ddong3_width)
                ddong3_y_pos = 0
                jordany_y_pos += jordany_speed *4
            if phochang_rect.colliderect(ddong4_rect):
                ddong_count +=1
                ddong4_speed +=1
                ddong4_x_pos = random.randint(0,screen_width - ddong4_width)
                ddong4_y_pos = 0
                jordany_y_pos += jordany_speed *4

        #3 부메랑
        elif number =="3":
            if bumerang_rect.colliderect(ddong_rect):
                ddong_count +=1
                ddong_speed +=0.3
                ddong_x_pos = random.randint(0,screen_width - ddong_width)
                ddong_y_pos = 0
                jordany_y_pos += jordany_speed * 1.5
            if bumerang_rect.colliderect(ddong2_rect):
                ddong_count +=1
                ddong2_speed +=0.4
                ddong2_x_pos = random.randint(0,screen_width - ddong2_width)
                ddong2_y_pos = 0
                jordany_y_pos += jordany_speed * 1.5
            if bumerang_rect.colliderect(ddong3_rect):
                ddong_count +=1
                ddong3_speed +=0.6
                ddong3_x_pos = random.randint(0,screen_width - ddong3_width)
                ddong3_y_pos = 0
                jordany_y_pos += jordany_speed * 1.5
            if bumerang_rect.colliderect(ddong4_rect):
                ddong_count +=1
                ddong4_speed +=1
                ddong4_x_pos = random.randint(0,screen_width - ddong4_width)
                ddong4_y_pos = 0
                jordany_y_pos += jordany_speed * 1.5
            if character_rect.colliderect(bumerang_get_rect):
                bumerang_get_on = True
                bumerang_get_x_pos = character_x_pos + character_width/2 - bumerang_get_width/2


        # 피한 똥 갯수
        ddong_number = game_font.render(str(ddong_count),True,(0,0,0))

        # 5. 화면에 그리기
        
        screen.blit(background,(0,0))
        screen.blit(zoneya_background,(zoneya_background_x_pos,zoneya_background_y_pos))
        screen.blit(character,(character_x_pos,character_y_pos))
        screen.blit(ddong,(ddong_x_pos,ddong_y_pos))
        screen.blit(ddong2,(ddong2_x_pos,ddong2_y_pos))
        screen.blit(ddong3,(ddong3_x_pos,ddong3_y_pos))
        screen.blit(ddong4,(ddong4_x_pos,ddong4_y_pos))
        screen.blit(ddong_number, (10,10))
        screen.blit(cloaking,(cloaking_x_pos,cloaking_y_pos))
        screen.blit(jordany,(jordany_x_pos,jordany_y_pos))
        screen.blit(zoneya,(zoneya_x_pos,zoneya_y_pos))
        
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
    screen.blit(game_over,(screen_width/2 - 150 , screen_height/2- 50))
    screen.blit(game_over2,(screen_width/2 - 140,screen_height/2 - 10))
    
    pygame.display.update() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            _running = False
pygame.quit()


# 움직임이 끊기는데 해결 할 수 있는 방법을 찾아보자.