import pygame
import time
import random

pygame.init()
screen_width = 1100
screen_length = 650
gameDisplay = pygame.display.set_mode((screen_width,screen_length))
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
clock=pygame.time.Clock()
pygame.display.set_caption("吕布除魔记")



def cards(x,y):

    #pygame.draw.rect(gameDisplay, black, (x, y, 120, 150))
    card_back =pygame.image.load("cardback.jpg")
    gameDisplay.blit(card_back, (x, y))
    mouse = pygame.mouse.get_pos()
    click =pygame.mouse.get_pressed()
    if mouse[0]>x+100:
        pygame.draw.rect(gameDisplay,red,(50,350,200,290))

    largeText = pygame.font.Font('freesansbold.ttf', 30)
    TextSurf, TextRect = text_objects("health:10", largeText)
    TextRect.center = ((1000), (320))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.draw.rect(gameDisplay,green, (950, 290, 100, 10))


def player_pic(x,y,pic_choice):
    picture= pygame.image.load(pic_choice)
    picture= pygame.transform.scale(picture,(200,258))
    gameDisplay.blit(picture,(x,y))






def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((screen_length / 2), (screen_width / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

    




def game_loop():

    loop = True

    while loop:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        gameDisplay.fill(white)
        #cards(50,10)
        #cards(300,10)
        #cards(550,10)

        cards(50,350)
        cards(300,350)
        cards(550,350)

        #player_pic(900,10,"head 1.png")
        player_pic(850, 350, "head 3.png")

        pygame.display.update()
        clock.tick(15)







game_loop()












"""import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (26, 0, 0)
white = (230, 255, 255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

block_color = (255, 0, 0)

car_width = 73
crash_sound = pygame.mixer.Sound("boom.wav")
pygame.mixer.music.load('house_lo.wav')

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('racecar.pmg.png')
gameIcon = pygame.image.load('icon.png')
pygame.display.set_icon(gameIcon)

pause = False


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()


def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Game Over", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)


        button("Try Again", 200, 400, 130, 50, green, bright_green,game_loop)
        button("QUIT!", 500, 400, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("A bit Racy", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)


        button("Going!", 200, 400, 100, 50, green, bright_green,game_loop)
        button("QUIT!", 500, 400, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)
        
def unpause():
    global pause
    pause = False


def pause1():
    while pause:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Pause", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)


        button("Keep Going!", 200, 400, 130, 50, green, bright_green,unpause)
        button("QUIT!", 500, 400, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y-5, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    ButtonText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, ButtonText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def quitgame():
    pygame.quit()
    quit()

def game_loop():
    pygame.mixer.music.play(-1)
    global pause
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    pause1()




            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        things(thing_startx, thing_starty, thing_width, thing_height, block_color)

        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty + thing_height-20:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()"""