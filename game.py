import pygame
import time 
pygame.init()
car_img=pygame.image.load('plane')
car_img=pygame.transform.scale(car_img,(800,600))
gd=pygame.display.set_mode((800,600))

def game_intro():
    intro=False
    while intro == False:
        gd.blit(car_img, (0, 0))
#        button(100,300,"PLAY")
 #       button(600,300,"QUIT")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
game_intro()
pygame.quit()
quit()