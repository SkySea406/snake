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
    if dif == "2player":
        dif = "2player"
        dif2 = 10
except IndexError:
    ctypes.windll.user32.MessageBoxW(0, "Please use the launcher.", "Error", 0x00000010)
    pygame.quit()
    exit()

if dif != "2player":
    dif = int(dif)
yon = "asagi"
snake = [100,20]
if dif == "2player":
    snake2 = [700, 20]
    yon2 = "asagi"
    snakebody2 = [[700, 20], [710, 20], [720, 20]]

snakebody = [[100, 20], [90, 20], [80, 20]]
puan = 0
puan2 = 0
def skorgoster(skor, screen, font, pos=(10, 10)):
    text = font.render(f"Skor: {skor}", True, (255, 255, 255))
    screen.blit(text, pos)
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
            if dif == "2player":
                if event.key == pygame.K_a and yon2 != "sag":
                    yon2 = "sol"
                elif event.key == pygame.K_d and yon2 != "sol":
                    yon2 = "sag"
                elif event.key == pygame.K_w and yon2 != "asagi":
                    yon2 = "yukari"
                elif event.key == pygame.K_s and yon2 != "yukari":
                    yon2 = "asagi"
    
    
    if yon == "sol":
        snake[0] -= 10
    elif yon == "sag":
        snake[0] += 10
    elif yon == "yukari":   
        snake[1] -= 10
    elif yon == "asagi":
        snake[1] += 10

    if dif == "2player":
        if yon2 == "sol":
            snake2[0] -= 10
        elif yon2 == "sag":
            snake2[0] += 10
        elif yon2 == "yukari":
            snake2[1] -= 10
        elif yon2 == "asagi":
            snake2[1] += 10
    if dif != "2player":
            if snake[0] >= 800 or snake[0] < 0 or snake[1] >= 600 or snake[1] < 0:
                pygame.quit()
                exit()
    if dif == "2player":
        if snake2[0] >= 800 or snake2[0] < 0 or snake2[1] >= 600 or snake2[1] < 0:
            ctypes.windll.user32.MessageBoxW(0, "Player 1 Won!", "Won", 0x00000040)
            pygame.quit()
            exit()
        if snake[0] >= 800 or snake[0] < 0 or snake[1] >= 600 or snake[1] < 0:
            ctypes.windll.user32.MessageBoxW(0, "Player 2 Won!", "Won", 0x00000040)
            pygame.quit()
            exit()
    if dif == "2player":
        if snake in snakebody2[1:]:
            ctypes.windll.user32.MessageBoxW(0, "Player 2 Won!", "Won", 0x00000040)
            pygame.quit()
            exit()
        if snake in snakebody[1:]:
            ctypes.windll.user32.MessageBoxW(0, "Player 2 Won!", "Won", 0x00000040)
            pygame.quit()
            exit()
        if snake2 in snakebody[1:]:
            ctypes.windll.user32.MessageBoxW(0, "Player 1 Won!", "Won", 0x00000040)
            pygame.quit()
            exit()
        if snake2 in snakebody2[1:]:
            ctypes.windll.user32.MessageBoxW(0, "Player 1 Won!", "Won", 0x00000040)
            pygame.quit()
            exit()
    if dif != "2player":
        if snake in snakebody[1:]:
            pygame.quit()
            exit()
    snakebody.insert(0, list(snake))
    if dif == "2player":
        snakebody2.insert(0, list(snake2))
        if snake2[0] == fx and snake2[1] == fy:
            puan2 += 1
            fx, fy = randompos()
            
        else:
            snakebody2.pop()
    if snake[0] == fx and snake[1] == fy:
        puan += 1
        fx, fy = randompos()
        
    else:
        snakebody.pop()
        
    

    
    screen.fill((0, 0, 0))
    key = pygame.key.get_pressed()
    
    for i in snakebody:
        pygame.draw.rect(screen, (0, 255, 0), (i[0], i[1], 10, 10))
    if dif == "2player":
        for i in snakebody2:
            pygame.draw.rect(screen, (0, 0, 255), (i[0], i[1], 10, 10))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(fx, fy, 10, 10))
    if dif != "2player":
        skorgoster(puan, screen, pygame.font.SysFont("Arial", 20), (10, 10))
    pygame.display.flip()
    if dif == "2player":
        clock.tick(dif2)
    else:
        clock.tick(dif)
        
    

