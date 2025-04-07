import time
import pygame
import random
import sys
import ctypes

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
try:
    dif = sys.argv[1]
    if dif == "rainbow":
        dif2 = 10
        ctypes.windll.user32.MessageBoxW(0, "Rainbow mode activated.", "Info", 0x00000040)
except IndexError:
    ctypes.windll.user32.MessageBoxW(0, "Please use the launcher.", "Error", 0x00000010)
    pygame.quit()
    exit()
if dif !="rainbow":
    dif = int(dif)
yon = "asagi"
deg = yon
snake = [100,20]
snakebody = [[100, 20], [90, 20], [80, 20]]
puan = 0
font = pygame.font.SysFont("Arial", 20)

def randompos():
    return random.randrange(100, 601, 10), random.randrange(100, 401, 10)
fx, fy = randompos()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and yon != "sag":
                yon = "sol"
            elif event.key == pygame.K_RIGHT and yon != "sol":
                yon = "sag"
            elif event.key == pygame.K_UP and yon != "asagi":
                yon = "yukari"
            elif event.key == pygame.K_DOWN and yon != "yukari":
                yon = "asagi"
    
    
    
    if yon == "sol":
        snake[0] -= 10
    elif yon == "sag":
        snake[0] += 10
    elif yon == "yukari":   
        snake[1] -= 10
    elif yon == "asagi":
        snake[1] += 10
    if snake[0] >= 800 or snake[0] < 0 or snake[1] >= 600 or snake[1] < 0:
        pygame.quit()
        exit()
    if snake in snakebody[1:]:
        pygame.quit()
        exit()
    snakebody.insert(0, list(snake))
    if snake[0] == fx and snake[1] == fy:
        puan += 1
        fx, fy = randompos()
        
    else:
        snakebody.pop()
        
    text = font.render("Score: " + str(puan), True, (255, 255, 255))   
    screen.fill((0, 0, 0))
    key = pygame.key.get_pressed()
    hitboxchar = []
    for i in snakebody:
        if dif == "rainbow":
            pygame.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (i[0], i[1], 10, 10))
        else:
            pygame.draw.rect(screen, (0, 255, 0), (i[0], i[1], 10, 10))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(fx, fy, 10, 10))
    pygame.display.flip()
    if dif =="rainbow":
        clock.tick(dif2)
    else:
        clock.tick(dif)

