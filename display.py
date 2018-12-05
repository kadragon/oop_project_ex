# -*- coding: utf-8 -*-
import pygame
WHITE = (255,255,255)
dis_width = 754
dis_height = 386

# def player(obj, x, y):
#     global dis
#     dis.blit(obj, (x,y))
def player(x, y):
    global dis, P1
    dis.blit(P1, (x,y))

def ball_move(x, y):
    global dis, ball
    dis.blit(ball, (x,y))

def run_game():
    global dis, clock, P1, ball, img


    x = dis_width*0.3
    y = dis_height*0.3
    x_change = 0
    y_change = 0
    ball_x = x
    ball_y = y
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
                    ball_x_change = 0
                if event.key == pygame.K_DOWN:
                    y_change = 5
                    ball_y_change = 20
                    ball_x_change = 0
                if event.key == pygame.K_LEFT:
                    x_change = -5
                    ball_x_change = -20
                    ball_y_change = 0
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                    ball_x_change = 20
                    ball_y_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    ball_y_change = 0
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    ball_x_change = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    ball_x_change = 5

        y += y_change
        x += x_change
        ball_x = x + ball_x_change
        ball_y = y + ball_y_change

        dis.fill(WHITE)
        dis.blit(img, (0, 0))
        player(x,y)
        ball_move(ball_x, ball_y)
        pygame.display.update()
        clock.tick(60) # 초당 프레임(FPS) 설정
    pygame.quit()
    quit()

def init_game():
    global dis, clock, P1, ball, img
    pygame.init()

    dis = pygame.display.set_mode((dis_width, dis_height))

    pygame.display.set_caption('Futsal')
    P1 = pygame.image.load('circle.png')
    ball = pygame.image.load('ball.png')
    img = pygame.image.load('soccermap.png')

    clock = pygame.time.Clock() # 초당 프레임(FPS)
    run_game()

if __name__=='__main__':
    init_game()

