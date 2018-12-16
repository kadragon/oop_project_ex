import pygame
from pygame import *
from time import sleep, time
import random

baller = [0 for i in range(6)]
RED = (255, 0, 0)
Green = (100, 250, 100)
BLACK = (255, 255, 255)
pad_width = 1024
pad_height = 512
player_x = 0
player_y = 0
score = [0, 0]

x = [0 for i in range(6)]
y = [0 for i in range(6)]
ball_x = 0
ball_y = 0
midt = 5
endt = 10
midterm = True
endterm = True
ireal = 7
jreal = 7
sportsmanship = 0
sportsmanship_score = 100


def penalty(player):
    global x, y, ball_x, ball_y,sportsmanship_score
    sportsmanship_score -=20
    sent = "Foul by player " + str(1+((player)%3))
    dispMessage(sent, False)

    if ball_x <= 150 and (192<= ball_y<=320) and player <= 2:
        dispMessage("Penalty Kick", True)
        x = [396, 191, 191, 601, 300, 300]#프리킥 위치로 변경
        y = [240, 112, 368, 240, 112, 368]#똑같이
        free_shooter = random.randrange(3, 6)
        x[free_shooter] = 300
        y[free_shooter] = 245
        ball_x = 300
        ball_y =245
    elif ball_x >= 874 and (192 <= ball_y <= 320) and player >= 3:
        dispMessage("Penalty kick", True)
        x = [396, 724, 724, 601, 806, 806]  # 프리킥 위치로 변경
        y = [240, 112, 368, 240, 112, 368]  # 똑같이
        free_shooter = random.randrange(0, 2)
        x[free_shooter] = 724
        y[free_shooter] = 245
        ball_x = 724
        ball_y = 245
    elif player <=2:
        dispMessage("Free Kick", True)
        now_player_x = x[player]
        now_player_y = y[player]
        x = [396, 191, 191, 601, 806, 806]
        y = [240, 112, 368, 240, 112, 368]
        free_shooter = random.randrange(3, 6)
        x[free_shooter] = now_player_x
        y[free_shooter] = now_player_y
        gamepad.blit(image_map, (0, 0))
        show_dis_play()
        pygame.display.update()
        sleep(2)
    else:
        dispMessage("Free Kick", True)
        now_player_x = x[player]
        now_player_y = y[player]
        x = [396, 191, 191, 601, 806, 806]
        y = [240, 112, 368, 240, 112, 368]
        free_shooter = random.randrange(0, 3)
        x[free_shooter] = now_player_x
        y[free_shooter] = now_player_y
        gamepad.blit(image_map, (0, 0))
        show_dis_play()
        pygame.display.update()
        sleep(2)


#태클은 태클을 하는 사람과 공을 갖고 있는 사람간의 싸움을 뜻한다. 이에 따라 2/3의 확률로 아무일도 일어나지 않으며,
# 1/3의 확률로 사건 '태클'이 일어나게 된다. 태클을 할 경우 1/3의 확률로 공을 찬 사람이 패널티/프리 킥을 차게 된다. 2/3의 확률로 파울이 일어나지 않는다.
def tackle(player_x, player_y, player):
    global ball_x, ball_y
    if abs(ball_x - player_x) <= 40 and abs(ball_y - player_y) <= 40:
        able = random.randrange(0, 3)
        if able == 0:
            ball_x = player_x
            ball_y = player_y
            ball_move(ball_x, ball_y)
            penalty_num = random.randrange(0, 3)  # 태클 시 플레이어에게 먼저 닿을 확률이 1/3이다. 즉 파울이 될 확률이 1/3이다.
            if penalty_num == 1:
                penalty(player)


def ball_move(x, y):
    global image_ball, ball_x, ball_y
    pygame.mixer.Sound.play(shoot_sound)
    ball_x = x
    ball_y = y
    gamepad.blit(image_ball, (x, y))


def ball_direction(player_x, player_y, ball_x, ball_y):
    if player_x - ball_x > 0:
        if player_y - ball_y > 0:
            return 0  # 'Ball LeftUp'
        if player_y - ball_y == 0:
            return 1  # 'Ball Left'
        if player_y - ball_y < 0:
            return 2  # 'Ball LeftDown'
    if player_x - ball_x == 0:
        if player_y - ball_y > 0:
            return 3  # 'Ball Up'
        if player_y - ball_y == 0:
            return 4  # 'Ball Stop'
        if player_y - ball_y < 0:
            return 5  # 'Ball Down'
    if player_x - ball_x < 0:
        if player_y - ball_y > 0:
            return 6  # 'Ball RightUp'
        if player_y - ball_y == 0:
            return 7  # 'Ball Right'
        if player_y - ball_y < 0:
            return 8  # 'Ball RightDown'


def ball_pass(player_x, player_y, dir, shoot_able):
    if shoot_able:
        dx = [-12, -12, -12, 0, 0, 0, 12, 12, 12]
        dy = [-12, 0, 12, -12, 0, 12, -12, 0, 12]

        for i in range(1, 30):
            ball_move(player_x + dx[dir] * i, player_y + dy[dir] * i)
            pygame.display.update()


def sportsmanship_checker():
    global sportsmanship, sportsmanship_score
    if sportsmanship_score <= 30:
        dispMessage("You got F.",True)
        image_sports = pygame.image.load('sportsmanship_end.png')
        gamepad.blit(image_sports, (0, 0))
        pygame.display.update()
        initGame()
    if sportsmanship >= 5:
        dispMessage("BenchClearing", True)
        sportsmanship_score-=10
        return True

def throw_in(balltaker):
    global ball_x, ball_y, x, y, whistle_sound, sportsmanship, sportsmanship_score
    sportsmanship_score -=5
    sportsmanship+=1
    pygame.mixer.Sound.play(whistle_sound)
    dispMessage('Throw in', True)
    sleep(0.5)
    if 0 <= balltaker <= 2:
        who = random.randrange(3, 6)
    else:
        who = random.randrange(0, 3)

    if ball_x < 50:
        x[balltaker] += 90
        ball_x = 60
        ball_move(ball_x, ball_y)
    if ball_x > 974:
        x[balltaker] -= 90
        ball_x = 954
        ball_move(ball_x, ball_y)
    if ball_y < 22.5:
        y[balltaker] += 90
        ball_y = 32.5
        ball_move(ball_x, ball_y)
    if ball_y > 480.5:
        y[balltaker] -= 90
        ball_y = 470.5
        ball_move(ball_x, ball_y)
    x[who] = ball_x
    y[who] = ball_y


def dispMessage(text, mode):
    global gamepad
    if mode:
        length = 2
        textfont = pygame.font.Font('freesansbold.ttf', 80)
        text = textfont.render(text, True, RED)
        textpos = text.get_rect()
        textpos.center = (pad_width / 2, pad_height / 2)
    else:
        length = 0.8
        textfont = pygame.font.Font('freesansbold.ttf', 50)
        text = textfont.render(text, True, BLACK)
        textpos = text.get_rect()
        textpos.center = (pad_width / 2, pad_height / 2 + 100)
    gamepad.blit(text, textpos)
    pygame.display.update()
    sleep(length)


def goalchcker():
    global ball_x, ball_y, score, sportsmanship_score
    if ((0 < ball_x < 50) or (949 < ball_x < 1024)) and (185 < ball_y < 306):
        pygame.mixer.music.fadeout(2000)
        dispMessage('Goal!!', True)
        sportsmanship_score+=5
        if 0 < ball_x < 50:
            score[1] += 1
        else:
            score[0] += 1
        return True


def ballchecker(shoot, xchange, ychange):
    global x, y, ball_x, ball_y, baller
    for i in range(6):
        baller[i] = 0
    for i in range(6):
        if (abs(ball_x - x[i]) <= 20 and abs(ball_y - y[i]) <= 20) and not shoot:
            ball_x = x[i]
            ball_y = y[i]
        elif(abs(ball_x - x[i]) <= 20 and abs(ball_y - y[i]) <= 20) and shoot:
            ball_x = x[i] + 2 * xchange
            ball_y = y[i] + 2 * ychange
        if abs(ball_x - x[i]) <= 30 and abs(ball_y - y[i]) <= 30:
            baller[i] = 1


def time_checker():
    global gamepad, midterm, start_time
    image_sports = pygame.image.load('sportsmanship.png')
    gamepad.blit(image_sports, (0, 0))
    pygame.display.update()
    pygame.mixer.music.fadeout(2000)
    sleep(10)
    midterm = False
    start_time += 10


def end_checker():
    global gamepad, endterm, score
    image_end = pygame.image.load('end.png')
    gamepad.blit(image_end, (0, 0))
    pygame.display.update()
    pygame.mixer.music.fadeout(2000)
    if score[0] > score[1]:
        winner = 'Blue'
    elif score[0] < score[1]:
        winner = 'Red'
    else:
        winner = 'None'
    textfont = pygame.font.Font('freesansbold.ttf', 80)
    text = textfont.render(winner + '            ' + ('Blue' if random.randrange(0, 1) is 0 else 'Red') + ' ' + str(random.randrange(1, 3)), True, RED)
    textpos = text.get_rect()
    textpos.center = (pad_width / 2, pad_height / 2)
    gamepad.blit(text, textpos)
    pygame.display.update()
    sleep(10)
    endterm = False
    exit()


def show_dis_play():
    global x, y, ball_x, ball_y, gamepad, image, image_ball, start_time, midt, endt, sportsmanship_score
    if sportsmanship_score >=100:
        sportsmanship_score=100
    for i in range(6):
        gamepad.blit(image[i], (x[i], y[i]))
    gamepad.blit(image_ball, (ball_x, ball_y))

    delta_time = int(time() - start_time)

    if delta_time // 60 == midt:
        time_checker()
        midt += 10
    elif delta_time // 60 == endt:
        end_checker()
        endt +=5

    textfont = pygame.font.Font('freesansbold.ttf', 20)
    text = textfont.render('Time %02d : %02d     Score %d : %d     Sportsmanship Score: %d' % (delta_time // 60, delta_time % 60, score[0], score[1], sportsmanship_score), True, RED)
    textpos = text.get_rect()
    textpos.center = (pad_width / 2, 16)
    gamepad.blit(text, textpos)
    pygame.display.update()


def out_check():
    global ball_x, ball_y
    if ball_x < 50 or ball_x > 974 or ball_y < 22.5 or ball_y > 480.5:
        return True
    else:
        return False


def runGame():
    global x, y, ball_x, ball_y, gamepad, baller, image_map, score, start_time, midterm, endterm, ireal, jreal, sportsmanship
    shoot = False
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
        x = [396, 191, 191, 601, 806, 806]
        y = [240, 112, 368, 240, 112, 368]
        ball_x = 498
        ball_y = 240
        x_change = [0 for i in range(6)]
        y_change = [0 for i in range(6)]
        ball_x_change = 0
        ball_y_change = 0

        gamepad.blit(image_map, (0, 0))
        show_dis_play()
        pygame.display.update()
        dispMessage('%d : %d' % (score[0], score[1]), True)

        while True:
            for event in pygame.event.get():
                shoot_able = False
                ballchecker(0, 0, 0)
                for i in range(6):
                    if baller[i] == 1:
                        shoot_able = True
                        shooter_x = x[i]
                        shooter_y = y[i]

                dir = ball_direction(shooter_x, shooter_y, ball_x, ball_y)
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
                                if sportsmanship !=0:
                                    sportsmanship -=1

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

                shoot = False
                if event.type == pygame.KEYDOWN:
                    key_shoot= [K_3, K_6, K_9, K_d, K_h, K_SPACE]
                    ireal = 1
                    jreal = 1

                    for i in range(6):
                        if baller[i] == 1:
                            ireal = i
                    for j in range(6):
                        if event.key == key_shoot[j]:
                            jreal = j

                    if ireal == jreal:
                        ball_pass(ball_x, ball_y, dir, shoot_able)
                        shoot = True

                key_tackle = [K_1, K_4, K_7, K_a, K_f, K_LCTRL]
                if event.type == pygame.KEYDOWN:
                    for i in range(6):
                        who = key_tackle[i]
                        if event.key == who:
                            tackle(x[i], y[i], i)

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

            ballchecker(shoot, ball_x_change, ball_y_change)
            
            if goalchcker():
                break
            if sportsmanship_checker():
                sportsmanship=0
                break
            if not midterm:
                midterm = True
                break
            if not endterm:
                endterm = True
                break
            if out_check():
                dribbleout = 0
                for i in range(6):
                    if baller[i] == 1:
                        dribbleout = 1
                        throw_in(i)
                if dribbleout == 0:
                    throw_in(ireal)

            gamepad.blit(image_map, (0, 0))
            show_dis_play()
            pygame.display.update()
            clock.tick(60)


def intro_screen():
    image_intro = pygame.image.load('intro.png')

    pygame.mixer.music.load('intro.wav')
    pygame.mixer.music.play(-1)
    crashed = False
    intro_time = time()
    delta_time = 1
    while not crashed:
        if time() - intro_time >= 0.8 * delta_time and delta_time % 2:
            gamepad.blit(image_intro, (0, 0))
            pygame.display.update()
            delta_time += 1
        elif time() - intro_time >= 0.8 * delta_time:
            dispMessage('[Press SPACE to start]', False)
            delta_time += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
                break
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    image_tuto = pygame.image.load('tuto.png')
                    gamepad.blit(image_tuto, (0, 0))
                    pygame.display.update()
                    sleep(7)
                    runGame()


def initGame():
    global gamepad, image, image_ball, clock, bgm_sound, shoot_sound, start_sound, whistle_sound, image_map, sportsmanship_score
    sportsmanship_score=100
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    image = list()
    pygame.display.set_caption('PyFootball')
    bgm_sound = pygame.mixer.Sound('bgm.wav')
    shoot_sound = pygame.mixer.Sound('shoot.wav')
    start_sound = pygame.mixer.Sound('start.wav')
    whistle_sound = pygame.mixer.Sound('whistle.wav')

    for i in range(6):
        image.append(pygame.image.load('image%d.png' % (i + 1)))
    image_ball = pygame.image.load('image_ball.png')
    image_map = pygame.image.load('FutsalMap.png')
    clock = pygame.time.Clock()
    intro_screen()

initGame()
