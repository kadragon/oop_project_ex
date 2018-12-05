# -*- coding: utf-8 -*-
"""
ASDW로 이동, 마우스 움직이며 방향, 마우스 클릭하여 발사
공부하면서 오픈소스 좀 바꾼건데 나중에 슛이나 패스 방향 설정할 때 적용할 수 있을 듯
"""
# Import library
import math
import random
import pygame
from pygame.locals import *

# 초기 게임설정
pygame.init()
pygame.mixer.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("동동 이미지")
# 속도 제어
FPS = 50
fpsClock=pygame.time.Clock()

# 키 입력 체크
keys = [False, False, False, False]
# 플레이어 버니 위치
playerpos = [100, 100]
# 화살 발사 횟수
acc = [0, 0]
# 화살 각도
arrows = []
# 적생성
badtimer = 100
# badtimer만큼 줄인다.
badtimer1 = 0
# 적 좌표 리스트
badguys = [[640, 100]]
healthvalue = 194

# Load images
# player = pygame.image.load("resources/images/dude.png")
# grass = pygame.image.load("resources/images/grass.png")
# castle = pygame.image.load("resources/images/castle.png")
# arrow = pygame.image.load("kakao_mu.png")
# badguyimg1 = pygame.image.load("resources/images/badguy.png")
# badguyimg = badguyimg1
# healthbar = pygame.image.load("resources/images/healthbar.png")
# health = pygame.image.load("resources/images/health.png")
# gameover = pygame.image.load("resources/images/gameover.png")
# youwin = pygame.image.load("resources/images/youwin.png")
player = pygame.image.load("plane.png")
grass = pygame.image.load("soccermap.png")
castle = pygame.image.load("circle.png")
arrow = pygame.image.load("ball.png")
badguyimg1 = pygame.image.load("circle.png")
badguyimg = badguyimg1

# Load audio
# hit = pygame.mixer.Sound("resources/audio/explode.wav")
# enemy = pygame.mixer.Sound("resources/audio/enemy.wav")
# shoot = pygame.mixer.Sound("resources/audio/shoot.wav")
# hit.set_volume(0.05)
# enemy.set_volume(0.05)
# shoot.set_volume(0.05)
# pygame.mixer.music.load("FIVE.mp3")
# pygame.mixer.music.play(-1, 0.0)
# pygame.mixer.music.set_volume(0.25)

# keep looping through
running = 1
exitcode = 0
while running:
    global accuracy
    # 5 - clear the screen before drawing it again
    screen.fill(0)

    #잔디를 그린다.
    for x in range(width//grass.get_width()+1): #잔디 100픽셀 (5)
        for y in range(height//grass.get_height()+1):
            screen.blit(grass, (x*100, y*100))

    #성을 배치
    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))
    # 6.1 - Set player position and rotation
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)
    # 6.2 - Draw arrows
    for bullet in arrows:
        index = 0
        velx = math.cos(bullet[0])*10
        vely = math.sin(bullet[0])*10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        #화살을 그려주고 제거하는 역할
        index += 1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))
    # 6.3 - Draw badgers
    if badtimer == 0: #적이 0이 될때 생성
        badguys.append([640, random.randint(50, 430)])
        badtimer = 100 - (badtimer1 * 2)
        if badtimer1 >= 35:
            badtimer1 = 35
        else:
            badtimer1 += 5
    index = 0
    for badguy in badguys:
        if badguy[0] < -64:
            badguys.pop(index)
        badguy[0] -= 7
        # 6.3.1 - Attack castle
        badrect = pygame.Rect(badguyimg.get_rect())
        badrect.top = badguy[1]
        badrect.left = badguy[0]
        if badrect.left < 64:
            # hit.play()
            healthvalue -= random.randint(5,20)
            badguys.pop(index)
        # 6.3.2 - Check for collisions
        # 충돌 체크
        index1 = 0
        for bullet in arrows:
            bullrect = pygame.Rect(arrow.get_rect()) #적을헤치우는 좌표
            bullrect.left = bullet[1]
            bullrect.top = bullet[2]
            if badrect.colliderect(bullrect):
                # enemy.play()
                acc[0] += 1
                badguys.pop(index)
                arrows.pop(index1)
            index1 += 1
        # 6.3.3 - Next bad guy
        index += 1
    for badguy in badguys:
        screen.blit(badguyimg, badguy)
    # 6.4 - Draw clock
    # 시계
    font = pygame.font.Font(None, 24)
    survivedtext = font.render(str((90000-pygame.time.get_ticks())//60000)+":"+str((90000-pygame.time.get_ticks())//1000%60).zfill(2), True, (0,0,0))
    textRect = survivedtext.get_rect()
    textRect.topright = [635, 5]
    screen.blit(survivedtext, textRect)
    # 6.5 - Draw health bar
    # screen.blit(healthbar, (5, 5))
    # for health1 in range(healthvalue):
    #     screen.blit(health, (health1 + 8, 8))
    # update the screen
    pygame.display.flip()
    fpsClock.tick(FPS)
    # loop through the events
    for event in pygame.event.get():
        #키를 누를때
        if event.type == KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True
        #키를 뗄때 동작이 자동으로 멈춘다.False
        if event.type == KEYUP:
            if event.key == K_w:
                keys[0] = False
            elif event.key == K_a:
                keys[1] = False
            elif event.key == K_s:
                keys[2] = False
            elif event.key == K_d:
                keys[3] = False
        if event.type == QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == MOUSEBUTTONDOWN:
            # shoot.play()
            position = pygame.mouse.get_pos()
            #화살 증가 횟수
            acc[1] += 1
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])
    # 9 - Move player
    if keys[0]:
        playerpos[1] -= 5
    elif keys[2]:
        playerpos[1] += 5
    if keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5
    badtimer -= 1
    # 10 - Win/Lose check
    if pygame.time.get_ticks() >= 90000:
        running = 0
        exitcode = 1
    if healthvalue <= 0:
        running = 0
        exitcode = 0
    if acc[1] != 0:
        accuracy = acc[0]*1.0/acc[1]*100
    else:
        accuracy = 0

# 11 - Win/lose display
if exitcode == 0:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (255, 0, 0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    # screen.blit(gameover, (0, 0))
    screen.blit(text, textRect)
else:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (0, 255, 0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    # screen.blit(youwin, (0, 0))
    screen.blit(text, textRect)

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
