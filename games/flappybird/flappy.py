#! /usr/bin/env python3
# https://www.youtube.com/watch?v=3ZPQI2-ciWI&t=128s
import pygame
import sys
import random


def main():
    pygame.init() # initializes pygame
    screen = pygame.display.set_mode((576, 1024))
    
    # load images
    background = pygame.image.load("./images/background.jpg").convert()
    background = pygame.transform.scale2x(background)
    
    # bird = pygame.image.load("./santa.jpg").convert()
    
    
    while True:
        for event in pygame.event.get(): # produces exit option on window
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.blit(background,(0,0))
        # screen.blit(bird,(0,0))
        
        pygame.display.update()
    
    
if __name__ == "__main__":
    main()