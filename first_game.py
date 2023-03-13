import pygame
import time 
import random
from random import randint
import time
import math
from pygame import mixer
pygame.mixer.init()
#import wavio
pygame.init()
x=300# hero
count=0
y=500
x_r=random.randint(x,y)#enemy
y_r=0
check=False
c=False
b_x_e=370
b_y_e=20

red=(255,0,0)
b_x=370
b_y=480
score=0
gd=pygame.display.set_mode((900,700))
back=pygame.image.load('back11.JPG')
back=pygame.transform.scale(back,(900,700))#backgrouynd
car_img=pygame.image.load('planeg.png')#plane
car_img=pygame.transform.scale(car_img,(200,200))
enemy=pygame.image.load("ee15.PNG")
enemy=pygame.transform.scale(enemy,(200,200))
e2=pygame.image.load("e2.PNG")
e2=pygame.transform.scale(e2,(100,100))
e=[enemy,e2]
bullet=pygame.image.load("eebb.PNG")
bullet=pygame.transform.scale(bullet,(30,30))
bullet1=pygame.image.load("bullet.PNG")
bullet1=pygame.transform.scale(bullet1,(30,30))
planet=pygame.image.load("planet.PNG")#earth
planet=pygame.transform.scale(planet,(180,180))
planet1=pygame.image.load("planet1.PNG")
planet1=pygame.transform.scale(planet1,(100,100))
planet2=pygame.image.load("planet2.PNG")#left
planet2=pygame.transform.scale(planet2,(80,70))
planet3=pygame.image.load("planet7.PNG")
planet3=pygame.transform.scale(planet3,(50,70))
star=pygame.image.load("star1.PNG")
star=pygame.transform.scale(star,(50,50))
def enmy_car(x_r,y_r):
    gd.blit(enemy,(x_r,y_r))#enemy
def car(x,y):
     gd.blit(car_img,(x,y))#plane hero
text=pygame.font.SysFont("Arial",20,'bold')
def score_text():
   img= text.render(f'Score:{score}',True,'red')
   gd.blit(img,(10,10))
def collision():#>/(x2-x1)2+(y2-y1)2
    distance=math.sqrt(math.pow(b_x-x_r,2)+math.pow(b_y-y_r,2))
    if distance<50:#if dist bet enemy hero less than 
        return True
def collision1():#>/(x2-x1)2+(y2-y1)2
    distance=math.sqrt(math.pow(b_x_e-x,2)+math.pow(b_y_e-y,2))
    if distance<80:#if dist bet enemy hero less than 
        return True

img1= text.render('Game overe',100,'white')

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            game_over=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x-=20
            elif event.key==pygame.K_RIGHT:
                x+=20
            if event.key==pygame.K_SPACE:
                if check is False:
                    check= True 
                    b_x=x+70  
            if event.key==pygame.K_SPACE:
                    c=False
                   # b_x_e=random.randint(x,y)
            
    gd.fill("black")
    gd.blit(back,(0,0))
    gd.blit(planet,(500,500))  
    gd.blit(planet1,(700,300)) 
    gd.blit(planet2,(100,100)) 
    gd.blit(planet3,(600,100)) 
   
            
    car(x,y)
    enmy_car(x_r,y_r)
    y_r+=1
    #speed of enemy
    if y_r==600:#enemy cover how much disstance
        y_r=0#  hero chnage postion
        x_r=random.randint(x,y)
        
        #gd.blit(enemy,(x_r,y_r))
    
        

    if b_y<=0:# condition back bullet
        b_y=480
        check=False

    if check: 
        gd.blit(bullet1,(b_x,b_y))# show bullet
        b_y-=5# speed of bullet
    if b_y_e>=900:#return back to positin
        b_y_e=x_r# bullet of enemy start from
        c=False
   
    if c is False:
        gd.blit(bullet,(b_x_e,b_y_e))
        b_y_e+=5
        b_x_e=x_r+80
    
    col_oc=collision()
    if col_oc:
        b_y=480
        check=False
        x_r=random.randint(x,y)
        y_r=0
        score+=100
    col_oc1=collision1()
    #score_text()
    if col_oc1:
        gd.fill('black')
        gd.blit(img1,(400,350))
        time.sleep(1)
       
        
    pygame.display.update()