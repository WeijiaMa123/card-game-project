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
boss_life=500
player_life=100




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


#class Cards:

class Deck:
    def _init_(self):





def game_loop():
    boss= Boss()
    player=Player()
    loop = True

    while loop:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        gameDisplay.fill(white)
        boss.draw(500)
        player.draw(100)
        pygame.display.update()


game_loop()