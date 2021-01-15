import pygame 
import random 
from pygame.constants import QUIT
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(250,40,250)
YELLOW=(255, 255,0)
PURPLE=(0, 105, 100)

pygame.init()
game_display=pygame.display.set_mode((800,600))
pygame.display.set_caption('My Game')
game_over=False
clock=pygame.time.Clock()
hascommon=False



class Food:
    active=True
    
    def __init__(self, display, number):
        self.x=number*170
        self.y=200
        self.display=display
        self.head=100
        self.number=number
    def draw(self):
        pygame.draw.rect(self.display, GREEN, [self.x, 0,60,self.y])

    def move(self):
        self.y+=0.5


foods=[Food(game_display, _) for _ in range(5)]   
class Obs:
  
    def __init__(self, display):
        self.x=random.randint(0, 39)*20
        self.y=random.randint(10, 39)*20
        self.display=display
    def draw(self):
        pygame.draw.rect(self.display, RED, [self.x, self.y,20,20])


Obs=[Obs(game_display) for _ in range(23)]   

class Person:
    dy=300
    dx=100
    def __init__(self, display):
        self.direction='R'
        self.display=display
        self.mostrecent=pygame.K_UP
        self.store=pygame.K_UP
        self.event=pygame
        self.down=False
        
    def draw(self):
        pygame.draw.rect(self.display, YELLOW, [self.dx, self.dy,20,20])
        
    def move(self ):
      
    
        if self.direction=='R':
            self.dx+=20

        if self.direction=='L':
            self.dx+=-20


        if self.direction=='U':
            self.dy-=20
        if self.direction=='D':
            self.dy+=20
        if self.direction=='SR':
            self.dx+=10
            self.dy+=0
        if self.direction=='SL':
            self.dx-=10
            self.dy+=0
        for food in foods:
         
            if per.dy<=food.y and (food.number*170-10<=per.dx<=food.number*170+60):
                self.down=False
                self.direction='D'
                
                
                food.y-=20

                
                break
   
                
       
    



per=Person(game_display)

while not game_over:
    clock.tick(10)
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
            break
    
        if event.type==pygame.KEYDOWN:
            if  event.key==pygame.K_UP:
                per.direction='U'
            elif event.key==pygame.K_LEFT:
                per.direction='L'
            elif event.key==pygame.K_RIGHT:
                per.direction='R'
            elif event.key==pygame.K_DOWN:
                per.direction='D'
     
      
  
    
    game_display.fill(BLACK)

    for food in foods:
        
        if food.active:
            food.draw()
            exist=False


    per.draw()
    pygame.draw.rect(game_display, RED, [20, 200,20,20])
    if per.dx==20 and per.dy==200:
        game_over=True
    for ob in Obs:
        if per.dx==ob.x and per.dy==ob.y:
            game_over=True

    for food in foods:
        food.move()
        if food.y>per.dy+20:
            game_over=True
        if food.y>=600:
            game_over=True
        

    for ob in Obs:
        ob.draw()
    if per.dx>=800 or per.dy>=600 or per.dx<0 or per.dy<0:
            game_over=True
    per.move()
    pygame.display.update()
    clock.tick(10)
    
    