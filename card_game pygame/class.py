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
pygame.display.set_caption("kill the monster")




class Boss:
    bosspic = pygame.image.load("green monster.png")
    bosspic = pygame.transform.scale(bosspic, (400, 300))
    x=0
    y=0
    life=500
    def __init__(self,x=20,y=10,life=500):
        self.x=x
        self.y=y
        self.life=life

    def draw(self,life):
        gameDisplay.blit(self.bosspic, (self.x, self.y))
        pygame.draw.rect(gameDisplay, red, (500, 50, life, 30))

class Player:
    picture = pygame.image.load("head 3.png")
    picture = pygame.transform.scale(picture, (200, 258))
    x=0
    y=0
    life=100
    def __init__(self,x=870,y=350,life=100):
        self.x=x
        self.y=y
        self.life=life

    def draw(self, life):
        gameDisplay.blit(self.picture,(self.x,self.y))
        pygame.draw.rect(gameDisplay, green,(950,290,life,15))




class Deck:

    images=[]
    fist = pygame.image.load("fist.png")
    heart = pygame.image.load("heart.png")
    shield = pygame.image.load("shield.png")
    sword = pygame.image.load("sword.png")
    images = [fist, heart, shield, sword]
    def _init_(self):
        #self.fist = pygame.image.load("fist.png")
        #self.heart = pygame.image.load("heart.png")
        #self.shield = pygame.image.load("shield.png")
        #self.sword = pygame.image.load("sword.png")
        self.images = [self.fist, self.heart, self.shield, self.sword]


    def draw(self, x,y,number,click):

        mouse = pygame.mouse.get_pos()
        if x + 120 > mouse[0] > x and y + 150 > mouse[1] > y and click== True:
            number = random.randint(0, 3)
        gameDisplay.blit(self.images[number], (x, y))
        return number


        #mouse = pygame.mouse.get_pos()
        #click = pygame.mouse.get_pressed()
        #number = random.randint(0, 3)
        #if  x + 120 > mouse[0] > x and y + 150 > mouse[1] > y and click[0]==1:
            #gameDisplay.blit(self.images[number], (x, y))







def game_loop():
    boss= Boss()
    player=Player()
    bossdeck= Deck()
    playerdeck= Deck()
    loop = True
    boss_num = 2
    player_num = 2
    boss_life = 500
    player_life = 100

    while loop:
        click=False

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP:
                click= True

        gameDisplay.fill(white)

        boss_num=bossdeck.draw(100,350,boss_num,click)
        player_num=playerdeck.draw(500,350,player_num,click)
        # chabge life based onb card number
        if boss_num==0:
            player_life -= 10
        if boss_num==1:
            boss_life += 10
        if boss_num==3:
            player_life -= 25

        if player_num==0:
            boss_life -= 25
        if player_num==1:
            player_life += 10
        if player_num==3:
            boss_life -= 100

        boss.draw(boss_life)
        player.draw(player_life)
        pygame.display.update()


game_loop()