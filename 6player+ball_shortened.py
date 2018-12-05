import pygame
from pygame import *
from time import sleep, time
import random

baller = [0 for i in range(6)]
Green = (100, 250, 100)
pad_width = 1024
pad_height = 512
player_x = 0
player_y = 0
RED = (255, 0, 0)
score = [0, 0]

x = [0 for i in range(6)]
y = [0 for i in range(6)]
ball_x = 0
ball_y = 0

def tackle(player_x, player_y):
    global ball_x, ball_y
    if abs(ball_x - player_x) <= 40 and abs(ball_y - player_y) <= 40:
        able = random.randrange(0, 6)
        if able >= 4:
            ball_y = player_y
            ball_x = player_x
            ball_move(ball_x, ball_y)
    return

def ball_move(x, y):
    global image_ball, ball_x, ball_y
    pygame.mixer.Sound.play(shoot_sound)
    ball_x = x
    ball_y = y
    gamepad.blit(image_ball, (x, y))


def ball_direction(player_x, player_y, ball_x, ball_y):
    if player_x - ball_x > 0:
        if player_y - ball_y > 0:
            return 'Ball LeftUp'
        if player_y - ball_y == 0:
            return 'Ball Left'
        if player_y - ball_y < 0:
            return 'Ball LeftDown'
    if player_x - ball_x == 0:
        if player_y - ball_y > 0:
            return 'Ball Up'
        if player_y - ball_y == 0:
            return 'Ball Stop'
        if player_y - ball_y < 0:
            return 'Ball Down'
    if player_x - ball_x < 0:
        if player_y - ball_y > 0:
            return 'Ball RightUp'
        if player_y - ball_y == 0:
            return 'Ball Right'
        if player_y - ball_y < 0:
            return 'Ball RightDown'


def ball_pass(player_x, player_y, dir, shoot_able):
    print('shootable = ', shoot_able)
    if shoot_able != 0:
        if dir == 'Ball Left':
            for i in range(1,30):
                ball_move(player_x-12*i, player_y)
                pygame.display.update()
        elif dir == 'Ball Right':
            for i in range(1,30):
                ball_move(player_x+12*i, player_y)
                pygame.display.update()
        elif dir == 'Ball Up':
            for i in range(1,30):
                ball_move(player_x, player_y-12*i)
                pygame.display.update()
        elif dir == 'Ball Down':
            for i in range(1,30):
                ball_move(player_x, player_y+12*i)
                pygame.display.update()
        elif dir == 'Ball LeftUp':
            for i in range(1,30):
                ball_move(player_x-12*i, player_y-12*i)
                pygame.display.update()
        elif dir == 'Ball RightUp':
            for i in range(1,30):
                ball_move(player_x+12*i, player_y-12*i)
                pygame.display.update()
        elif dir == 'Ball LeftDown':
            for i in range(1,30):
                ball_move(player_x-12*i, player_y+12*i)
                pygame.display.update()
        elif dir == 'Ball RightDown':
            for i in range(1,30):
                ball_move(player_x+12*i, player_y+12*i)
                pygame.display.update()


def dispMessage(text):
    global gamepad
    textfont = pygame.font.Font('freesansbold.ttf', 80)
    text = textfont.render(text, True, RED)
    textpos = text.get_rect()
    textpos.center = (pad_width / 2, pad_height / 2)
    gamepad.blit(text, textpos)
    pygame.display.update()
    sleep(2)


def goalchcker():
    global ball_x, ball_y, score
    if ((0 < ball_x < 75) or (949< ball_x < 1024)) and (206 < ball_y < 306):
        print('goal')
        pygame.mixer.music.fadeout(2000)
        dispMessage('Goal!!')
        if 0 < ball_x < 75:
            score[0] += 1
        else:
            score[1] += 1
        print(score)
        return True
    elif ((0 < ball_x < 120) or (904< ball_x < 1024)) and (106 < ball_y < 406):
        pass
    #보통 골대 가까이 가면 소리 커지거나 군중 소리 나던데...


def ballchecker(shoot, xchange, ychange):
    global x, y, ball_x, ball_y, baller
    for i in range(6):
        baller[i] = 0
    for i in range(6):
        if (abs(ball_x - x[i]) <= 20 and abs(ball_y - y[i]) <= 20) and (shoot == 0):
            ball_x = x[i]
            ball_y = y[i]
        elif(abs(ball_x - x[i]) <= 20 and abs(ball_y - y[i]) <= 20) and (shoot == 1):
            ball_x = x[i] + 2 * xchange
            ball_y = y[i] + 2 * ychange
        if abs(ball_x - x[i]) <= 30 and abs(ball_y - y[i]) <= 30:
            baller[i] = 1


def show_dis_play():
    global x, y, ball_x, ball_y, gamepad, image, image_ball, start_time

    for i in range(6):
        gamepad.blit(image[i], (x[i], y[i]))
    gamepad.blit(image_ball, (ball_x, ball_y))

    delta_time = int(time() - start_time)

    textfont = pygame.font.Font('freesansbold.ttf', 20)
    text = textfont.render('Time %02d : %02d     Score %d : %d' % (delta_time // 60, delta_time % 60, score[0], score[1]), True, RED)
    textpos = text.get_rect()
    textpos.center = (pad_width / 2, 20)
    gamepad.blit(text, textpos)
    pygame.display.update()


def runGame():
    global x, y, ball_x, ball_y, gamepad, baller, image_map, score, start_time

    start_time = time()

    while True:
        pygame.init()
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.Sound.play(start_sound)
        pygame.mixer.music.load('bgm.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(5.0)

        shooter_x = 0
        shooter_y = 0
        x = [410, 205, 205, 615, 820, 820]
        y = [256, 128, 384, 256, 128, 384]
        ball_x = 512
        ball_y = 256
        x_change = [0 for i in range(6)]
        y_change = [0 for i in range(6)]
        ball_x_change = 0
        ball_y_change = 0

        gamepad.blit(image_map, (0, 0))
        show_dis_play()
        pygame.display.update()
        dispMessage('%d : %d' % (score[0], score[1]))

        while True:
            for event in pygame.event.get():
                shoot_able = 0
                ballchecker(0, 0, 0)
                for i in range(6):
                    if baller[i] == 1:
                        print('baller now=', i)
                        shoot_able = 1
                        shooter_x = x[i]
                        shooter_y = y[i]

                dir = ball_direction(shooter_x, shooter_y, ball_x, ball_y)
                print(dir)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                key = [[K_2, K_q, K_w, K_e], [K_5, K_r, K_t, K_y], [K_8, K_u, K_i, K_o], [K_s, K_z, K_x, K_c],
                       [K_g, K_v, K_b, K_n], [K_UP, K_LEFT, K_DOWN, K_RIGHT]]

                if event.type == pygame.KEYDOWN:
                    for i in range(6):
                        player = key[i]
                        for j in range(4):
                            direction = player[j]
                            if event.key == direction:
                                if j is 0:
                                    y_change[i] = -5
                                    ball_y_change = -10
                                if j is 1:
                                    x_change[i] = -5
                                    ball_x_change = -10
                                if j is 2:
                                    y_change[i] = 5
                                    ball_y_change = 10
                                if j is 3:
                                    x_change[i] = 5
                                    ball_x_change = 10

                if event.type == pygame.KEYUP:
                    for i in range(6):
                        player = key[i]
                        for j in range(4):
                            direction = player[j]
                            if event.key == direction:
                                if j % 2:
                                    x_change[i] = 0
                                    ball_x_change = 0
                                else:
                                    y_change[i] = 0
                                    ball_y_change = 0

                shoot = 0
                if event.type == pygame.KEYDOWN:
                    if event.key in [K_SPACE, K_3, K_6, K_9, K_d, K_h]:
                        print('Ball Shoot')
                        print(i)
                        ball_pass(ball_x, ball_y, dir, shoot_able)
                        shoot = 1

                key_tackle = [K_1, K_4, K_7, K_a, K_f, K_LCTRL]
                if event.type == pygame.KEYDOWN:
                    for i in range(0, 6):
                        who = key_tackle[i]
                        if event.key == who:
                            print("Ball Tackle")
                            print(i)
                            tackle(x[i], y[i])

            for i in range(6):
                x[i] += x_change[i]

                if x[i] < 0:
                    x[i] = 0
                if x[i] > 1014:
                    x[i] = 1014

                y[i] += y_change[i]

                if y[i] < 10:
                    y[i] = 10
                if y[i] > 502:
                    y[i] = 502

            for i in range(6):
                if baller[i] == 1:
                    ball_x += ball_x_change
                    ball_y += ball_y_change
                    if ball_x < 10:
                        ball_x = 10
                    if ball_x > 1014:
                        ball_x = 1014
                    if ball_y < 10:
                        ball_y = 10
                    if ball_y > 502:
                        ball_y = 502
            print('ball position=', ball_x, ball_y)
            ballchecker(shoot, ball_x_change, ball_y_change)
            if goalchcker():
                break
            gamepad.blit(image_map, (0, 0))
            show_dis_play()
            pygame.display.update()
            clock.tick(60)

def intro_screen():
    image_intro = pygame.image.load('intro.png')
    gamepad.blit(image_intro, (0, 0))
    pygame.display.update()
    pygame.mixer.music.load('intro.wav')
    pygame.mixer.music.play(-1)
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                break
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    runGame()
    return

def initGame():
    global gamepad, image, image_ball, clock, image_goalsign, bgm_sound, shoot_sound, crowd_sound, start_sound, whistle_sound, image_map

    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    image = list()
    pygame.display.set_caption('PyFootball')
    bgm_sound = pygame.mixer.Sound('bgm.wav')
    shoot_sound = pygame.mixer.Sound('shoot.wav')
    crowd_sound = pygame.mixer.Sound('crowd.wav')
    start_sound = pygame.mixer.Sound('start.wav')
    whistle_sound = pygame.mixer.Sound('whistle.wav')

    for i in range(6):
        image.append(pygame.image.load('image%d.png' % (i + 1)))
    image_ball = pygame.image.load('image_ball.png')
    image_goalsign = pygame.image.load('image_goalsign.png')
    image_map = pygame.image.load('FutsalMap.png')
    clock = pygame.time.Clock()
    intro_screen()

initGame()
