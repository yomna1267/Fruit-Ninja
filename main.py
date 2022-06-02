import pygame
import random
pygame.init()

WIDTH = 800
HEIGHT = 600
lives = 3
score = 0
FPS = 12
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

fruits = ['apple', 'orange', 'watermelon', 'bomb']

def randomFruits(fruit):
    fruitPath = "fruits/" + fruit +".png"
    fruitsInfo[fruit] = {
        'img' : pygame.image.load(fruitPath),
        'x' : random.randint(WIDTH -750, WIDTH-150),
        'y' : 800,
        'speedX' : random.randint(0, 10),
        'speedY': random.randint(-80, -60),
        'cnt' : 0,
        'cut' : False,
        'THROW' : False
    }
    if random.random() >= 0.75:
        fruitsInfo[fruit]['THROW'] = True
    else:
        fruitsInfo[fruit]['THROW'] = False



fruitsInfo ={}

for fruit in fruits:
    randomFruits(fruit)


pygame.display.set_caption("Fruit Ninja")
icon = pygame.image.load("img/icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load("img/woodBack.jpg")

title = pygame.font.Font('Adoha.otf', 50)
title_text = title.render("Fruit Ninja", True, WHITE)
title_rect = title_text.get_rect()
title_rect.center = WIDTH / 2 , HEIGHT - 450

scr = pygame.font.Font('Adoha.otf', 25)
score_text = scr.render("Score : " + str(score), True, WHITE)
score_rect = score_text.get_rect()
score_rect.center = WIDTH - 730 , HEIGHT - 570

live = pygame.font.Font('Adoha.otf', 25)
live_text = live.render("Live : " + str(lives), True, WHITE)
live_rect = live_text.get_rect()
live_rect.center = WIDTH - 70 , HEIGHT - 570

play = pygame.font.Font('Adoha.otf', 40)
play_text = play.render("Press any key to play again! " , True, WHITE)
play_rect = play_text.get_rect()
play_rect.center = WIDTH /2 , HEIGHT - 150

def gameover():
    screen.blit(background, (0, 0))
    screen.blit(title_text, title_rect)
    screen.blit(score_text, score_rect)
    screen.blit(live_text, live_rect)
    screen.blit(play_text, play_rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                waiting = False


running = True
game_over = False

while running:
    screen.fill(RED)
    screen.blit(background, (0, 0))
    screen.blit(score_text, score_rect)
    screen.blit(live_text, live_rect)
    if not game_over:
        lives = 3
        score = 0
        game_over = True
        gameover()

    for key, value in fruitsInfo.items():

        if value['THROW']:
            value['x'] += value['speedX']
            value['y'] += value['speedY']
            value['speedY'] += (1* value['cnt'])
            value['cnt'] += 1

            if value['y'] <= 800:
                screen.blit(value['img'], (value['x'], value['y']))
            else:
                randomFruits(key)

            mousePosition = pygame.mouse.get_pos()

            if not(value['cut']) and mousePosition[0] > value['x'] and mousePosition[0] < value['x'] + 64 \
                and mousePosition[1] > value['y'] and mousePosition[1] < value['y'] + 64:
                if key == 'bomb':
                    lives -= 1
                    if lives < 0:
                        gameover()
                        lives = 3
                        score = 0
                        game_over = False
                    halfFruit = "fruits/explosion.png"
                else:
                    halfFruit = "fruits/" + "half-" + key+".png"
                value['img'] = pygame.image.load(halfFruit)
                value ['x'] += 20
                if key != 'bomb':
                    score += 1
                score_text = scr.render("Score : " + str(score), True, WHITE)
                live_text = live.render("Live : " + str(lives), True, WHITE)
                value['cut'] = True
        else:
            randomFruits(key)




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
exit()