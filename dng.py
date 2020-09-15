import pygame
import time
from datetime import datetime
import random
import sys
from pygame.locals import *
import pymysql

width = 1100
height = 600
red = (255, 0, 0)
white = (255, 255, 255)
trans_c = (215, 251, 255)
black = (0, 0, 0)
bright_green = (0, 255, 0)

fps = 32
gameWindow = pygame.display.set_mode((width, height))
seconds = time.time()

dino = 'gallery/images/frzi.png'

backgroundm = 'gallery/images/game_backgroundm.png'
gamebackground = 'gallery/images/game_background.png'
backgroundn = 'gallery/images/backgroundn.png'
treew = 'gallery/images/tree.png'
treeg = 'gallery/images/atree1.png'
tree2 = 'gallery/images/btree1.png'
tree3 = 'gallery/images/tree1.png'
bird = 'gallery/images/bird.png'
base = 'gallery/images/base.png'
player = 'gallery/images/dino1.png'

game_sprites = {}
game_audio = {}


# connection = pymysql.connect(host="localhost", user="root", passwd="", database="db_dino")
# cursor = connection.cursor()

# connection.close()

def welcome_screen():
    while True:
        # gameWindow.fill(red)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == pygame.K_UP):
                return
            else:
                gameWindow.blit(game_sprites['game_background'], (0, 0))
                text_on_screen("Dinosour", red, 370, 40)
                text_on_screen("Game", red, 400, 90)
                gameWindow.blit(game_sprites['dino'], (100, 270))
                gameWindow.blit(game_sprites['tree'], (480, 250))
                gameWindow.blit(game_sprites['bird'], (800, 40))
                # gameWindow.blit(game_sprites['base'], (0, 500))
                # text_on_screen("PLAY", white, 100, 170)

                largeText = pygame.font.Font('freesansbold.ttf', 100)
                TextSurf, TextRect = text_objects("PLAY", largeText)
                TextRect.center = ((150), (170))
                gameWindow.blit(TextSurf, TextRect)

                largeText = pygame.font.Font('freesansbold.ttf', 85)
                TextSurf, TextRect = text_objects("PLAYERS", largeText)
                TextRect.center = ((650), (170))
                gameWindow.blit(TextSurf, TextRect)

                if 251 > mouse[0] > 32 and 200 > mouse[1] > 120:
                    pygame.draw.rect(gameWindow, bright_green, [150, 170, 50, 20])
                    click = pygame.mouse.get_pressed()
                    if click[0] == 1:
                        game_loop()
                if 845 > mouse[0] > 450 and 200 > mouse[1] > 120:
                    pygame.draw.rect(gameWindow, bright_green, [650, 170, 50, 20])
                    click = pygame.mouse.get_pressed()
                    if click[0] == 1:
                        users()

                pygame.display.update()
                clock.tick(fps)


def text_on_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def text_on_screen_2(text, color, x, y):
    screen_text = font2.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# def users():
#     print("ENTER YOUR CHOICE")
#     print("1->FOR NEW USER")
#     print("2->FOR EXISTING USER")
#     a=input()
#     b=int(a)
#     if b==1:
#
#     if b==2:
#
#     if b!=1 or 2:
#         print("enter valid choice")


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((width / 2), (height / 2))
    gameWindow.blit(TextSurf, TextRect)


def get_random_trees():
    x = width + random.randint(0, 10)
    y = int((height - game_sprites['base'].get_height()) + 112) - 50
    my_list = [game_sprites['treeg'], game_sprites['tree2'], game_sprites['tree3']]
    a = random.choice(my_list)
    loc = [
        {'tx': x, 'ty': y, 'ai': a}
    ]
    return loc


def game_loop():
    game_exit = False
    # a = input("enter name")
    start_time = time.time()
    score = 0
    basex = 0
    basey = int(height * 0.8)
    playerx = int(width / 5)
    playery = int((height - game_sprites['base'].get_height()) + 112)
    y1 = playery
    tree1 = get_random_trees()
    tree2 = get_random_trees()
    t1 = [
        {'tx': tree1[0]['tx'], 'ty': tree1[0]['ty'], 'im': tree1[0]['ai']}
    ]

    t2 = [
        {'tx': tree2[0]['tx'] + 100, 'ty': tree2[0]['ty'], 'im': tree2[0]['ai']}
    ]
    messagex = int(width * 0.65)
    messagey = int(height * 0.11)
    tree_vel = -5
    # y1 = playery - 50
    with open("hscore.txt", 'r') as f:
        h_score = f.read()

    while not game_exit:
        end_time = time.time()
        score = int(end_time - start_time)

        for event in pygame.event.get():
            print("tree_1 position is", t1[0]['ty'])
            print("tree_2 position is", t2[0]['ty'])

            with open("hscore.txt", 'w') as f:
                f.write(str(h_score))

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                playery -= 50

        if score > int(h_score):
            h_score = score

        if playery < y1:
            playery += 5

        if t1[0]['tx'] < -t1[0]['im'].get_width() or t2[0]['tx'] < -t2[0]['im'].get_width():
            t1.pop(0)
            t2.pop(0)

        if 0 < t1[0]['tx'] < 5:
            newtree = get_random_trees()
            newtree2 = get_random_trees()
            t1.append(newtree2[0])
            t2.append(newtree[0])

        for t4, t5 in zip(t1, t2):
            t4['tx'] += tree_vel
            t5['tx'] += tree_vel
            t4['im'] = t1[0]['im']
            t5['im'] = t2[0]['im']

        if score < 2:
            gameWindow.blit(game_sprites['daybg'], (0, 0))
        else:
            gameWindow.blit(game_sprites['nightbg'], (0, 0))
        gameWindow.blit(game_sprites['base'], (basex, basey))
        gameWindow.blit(game_sprites['player'], (playerx, playery))
        text_on_screen_2("Score:" + str(score), red, messagex, messagey)
        text_on_screen_2("high score" + str(h_score), red, messagex, messagey + 100)

        for t4, t5 in zip(t1, t2):
            gameWindow.blit(t1[0]['im'], (t4['tx'], t4['ty']))
            gameWindow.blit(t2[0]['im'], (t5['tx'], t5['ty']))

        if ((abs(playerx - t1[0]['tx']) < 10 or abs(playerx - t2[0]['tx']) < 10) and abs(playery - t1[0]['ty']) < 20):
            print(
                f" playerx is {playerx} and playery is {playery} and postoin of tree is {abs(playery - t1[0]['ty'])} ")
            game_exit = True
        pygame.display.update()
        clock.tick(fps)


if __name__ == '__main__':
    x = pygame.init()
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 95)
    font2 = pygame.font.SysFont(None, 45)
    pygame.display.set_caption("Dinosour game")
    game_sprites['dino'] = pygame.image.load(dino).convert_alpha()
    game_sprites['player'] = pygame.image.load(player).convert_alpha()
    game_sprites['game_background'] = pygame.image.load(gamebackground).convert_alpha()
    game_sprites['tree'] = pygame.image.load(treew).convert_alpha()
    game_sprites['bird'] = pygame.image.load(bird).convert_alpha()
    game_sprites['base'] = pygame.image.load(base).convert_alpha()
    game_sprites['nightbg'] = pygame.image.load(backgroundn).convert_alpha()
    game_sprites['daybg'] = pygame.image.load(backgroundm).convert_alpha()
    game_sprites['treeg'] = pygame.image.load(treeg).convert_alpha()
    game_sprites['tree2'] = pygame.image.load(tree2).convert_alpha()
    game_sprites['tree3'] = pygame.image.load(tree3).convert_alpha()
    game_audio['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    game_audio['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    game_audio['point'] = pygame.mixer.Sound('gallery/audio/point.wav')

    # database connection

while True:
    welcome_screen()
    game_loop()
