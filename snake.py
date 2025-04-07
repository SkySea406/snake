import time
import pygame
import random
import sys
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
dif = sys,argv[1]
yon = "asagi"
deg = yon
snake = [100,20]
snakebody = [[100, 20], [90, 20], [80, 20]]

def randompos():
    return random.randrange(100, 601, 10), random.randrange(100, 401, 10)
fx, fy = randompos()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                yon = "sol"
            elif event.key == pygame.K_RIGHT:
                yon = "sag"
            elif event.key == pygame.K_UP:
                yon = "yukari"
            elif event.key == pygame.K_DOWN:
                yon = "asagi"
    
    
    
    if yon == "sol":
        snake[0] -= 10
    elif yon == "sag":
        snake[0] += 10
    elif yon == "yukari":   
        snake[1] -= 10
    elif yon == "asagi":
        snake[1] += 10
    snakebody.insert(0, list(snake))
    if snake[0] == fx and snake[1] == fy:
        
        fx, fy = randompos()
        
    else:
        snakebody.pop()
        
        
    screen.fill((0, 0, 0))
    key = pygame.key.get_pressed()
    hitboxchar = []
    for i in snakebody:
        pygame.draw.rect(screen, (0, 255, 0), (i[0], i[1], 10, 10))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(fx, fy, 10, 10))
    pygame.display.flip()
    clock.tick(dif)

