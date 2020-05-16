#Game-0.1
import pygame
import os
import sks
from pygame.locals import *


if __name__ == '__main__':
    white = (255, 255, 255)
    screen_width, screen_height = 960, 640
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("The Game")
    
    pygame.init()

    fig_path = r'*/Game/Pic'
    paper = pygame.image.load(fig_path + 'paper.png').convert_alpha()
#基础设置
    
    while True:
        screen.fill(white)
        screen.blit(paper, (0, 0))
     
        pygame.display.flip()
    
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

