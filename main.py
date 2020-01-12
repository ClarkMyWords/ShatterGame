import pygame

from Word import Word
from Game import Game

# initialize
# set screen size

pygame.init()
screen = pygame.display.set_mode((1000, 600))
done = False

clock = pygame.time.Clock()

gameState = 0;
gameTime = 0;
button1 = [66,133]
button2 = [382,133]
button3 = [66,366]
button4 = [382,366]


color = (255, 100, 0)
white = (255, 255, 255)
black = (0, 0, 0)

font = pygame.font.Font('freesansbold.ttf', 50)
text = font.render('SHATTER', True, white, black)
#textRect = text.get_rect()
textRect = [380,25]

text2 = [pygame.font.Font('freesansbold.ttf', 50).render('START', True, white, color), [110,185]]
text3 = [pygame.font.Font('freesansbold.ttf', 50).render('LEVEL', True, white, color), [426,185]]
text4 = [pygame.font.Font('freesansbold.ttf', 50).render('ABOUT', True, white, color), [100,421]]
text5 = [pygame.font.Font('freesansbold.ttf', 50).render('QUIT', True, white, color), [446,421]]
text6 = [pygame.font.Font('freesansbold.ttf', 50).render('QUIT', True, white, color), [446,421]]





while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    gameTime += 1
    gameTime %= 60


    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: textRect[0] += 10
    if pressed[pygame.K_DOWN]: y += 3
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3


    screen.fill((0, 0, 0))
    color = (255, 100, 0)

    pygame.draw.rect(screen, color, pygame.Rect(button1[0], button1[1], 250, 150))
    pygame.draw.rect(screen, color, pygame.Rect(button2[0], button2[1], 250, 150))
    pygame.draw.rect(screen, color, pygame.Rect(button3[0], button3[1], 250, 150))
    pygame.draw.rect(screen, color, pygame.Rect(button4[0], button4[1], 250, 150))

    if gameTime > 30:
        screen.blit(text, textRect)
    screen.blit(text2[0], text2[1])
    screen.blit(text3[0], text3[1])
    screen.blit(text4[0], text4[1])
    screen.blit(text5[0], text5[1])


    pygame.display.flip()
    clock.tick(60)
