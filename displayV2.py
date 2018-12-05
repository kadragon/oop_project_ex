# -*- coding: utf-8 -*-
import pygame
WHITE = (255,255,255)
dis_width = 754
dis_height = 386

def player_move(x, y):
    global dis, P1
    dis.blit(P1, (x,y))

def ball_move(x, y):
    global dis, ball
    dis.blit(ball, (x,y))

def direction(x, y, ball_x, ball_y):
    if x - ball_x > 0:
        if y- ball_y > 0:
            return 'Ball LeftUp'
        if y- ball_y == 0:
            return 'Ball Left'
        if y- ball_y < 0:
            return 'Ball LeftDown'
    if x - ball_x == 0:
        if y- ball_y > 0:
            return 'Ball Up'
        if y- ball_y == 0:
            return 'Ball Stop'
        if y- ball_y < 0:
            return 'Ball Down'
    if x - ball_x < 0:
        if y- ball_y > 0:
            return 'Ball RightUp'
        if y- ball_y == 0:
            return 'Ball Right'
        if y- ball_y < 0:
            return 'Ball RightDown'

def ball_pass(x, y, dir):
    if dir == 'Ball Left':
        for i in range(1,50):
            ball_move(x-12*i, y)
            pygame.display.update()
    if dir == 'Ball Right':
        for i in range(1,50):
            ball_move(x+12*i, y)
            pygame.display.update()
    if dir == 'Ball Up':
        for i in range(1,50):
            ball_move(x, y-12*i)
            pygame.display.update()
    if dir == 'Ball Down':
        for i in range(1,50):
            ball_move(x, y+12*i)
            pygame.display.update()
    if dir == 'Ball LeftUp':
        for i in range(1,50):
            ball_move(x-12*i, y-12*i)
            pygame.display.update()
    if dir == 'Ball RightUp':
        for i in range(1,50):
            ball_move(x+12*i, y-12*i)
            pygame.display.update()
    if dir == 'Ball LeftDown':
        for i in range(1,50):
            ball_move(x-12*i, y+12*i)
            pygame.display.update()
    if dir == 'Ball RightDown':
        for i in range(1,50):
            ball_move(x+12*i, y+12*i)
            pygame.display.update()
    return

def run_game():
    global dis, clock, P1, ball, background

    x = dis_width*0.5
    y = dis_height*0.5
    ball_x = dis_width*0.5
    ball_y = dis_height*0.5
    x_change = 0
    y_change = 0
    ball_x_change = 0
    ball_y_change = 0

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed =True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                    ball_y_change = -20
                    #print("UP")
                if event.key == pygame.K_DOWN:
                    y_change = 5
                    ball_y_change = 20
                    #print("DOWN")
                if event.key == pygame.K_LEFT:
                    x_change = -5
                    ball_x_change = -20
                    #print("LEFT")
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                    ball_x_change = 20
                    #print("RIGHT")

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    ball_y_change = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    ball_x_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Ball Shoot")
                    ball_pass(ball_x, ball_y, dir)
                    #ball_x_change = 100


        y += y_change
        x += x_change
        ball_x = x + ball_x_change
        ball_y = y + ball_y_change
        dir = direction(x, y, ball_x, ball_y)
        print(dir)

        dis.fill(WHITE)
        dis.blit(background, (0, 0))
        player_move(x,y)
        ball_move(ball_x, ball_y)
        pygame.display.update()
        clock.tick(60) # 초당 프레임(FPS) 설정
    pygame.quit()
    quit()

def init_game():
    global dis, clock, P1, ball, background
    pygame.init()

    dis = pygame.display.set_mode((dis_width, dis_height))

    pygame.display.set_caption('Futsal')
    P1 = pygame.image.load('circle.png')
    ball = pygame.image.load('ball.png')
    background = pygame.image.load('soccermap.png')

    clock = pygame.time.Clock() # 초당 프레임(FPS)
    run_game()

if __name__=='__main__':
    init_game()

