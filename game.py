from operator import pos
from turtle import position
import pygame
import numpy as np
pygame.init()
Game_array = np.zeros((3, 3, 2))
WIDTH = 300  # Width for screen
HEIGHT = 300  # height for screen
# O_img = pygame.image.load(r'E:\Python Programming\O image.png')
# X_img = pygame.image.load(r'E:\Python Programming\X image.png')

O_img = pygame.image.load("0.png")
X_img = pygame.image.load("x.png")

board = pygame.display.set_mode((WIDTH, HEIGHT))  # Screen board size
pygame.display.set_caption('TIC-TAC-TOE')  # Windows caption
# Logo = pygame.image.load("TICTACTOE.png")
Logo = pygame.image.load("car.jpeg")
pygame.display.set_icon(Logo)
BG_COLOR = (255, 255, 255)  # Background color White!!
board.fill(BG_COLOR)
pygame.display.update()
# Variables
LINE_WIDTH = 5

def draw_Lines():  

    grid = (0, 0, 0)
    for x in range(1, 3):
        pygame.draw.line(board, grid, (0, x * 100),
                         (WIDTH, x * 100), LINE_WIDTH)
        pygame.draw.line(board, grid, (x * 100, 0),
                         (x * 100, HEIGHT), LINE_WIDTH)


# Main loop
open = True
turn1 = True
count = 0

while open:
    
    draw_Lines()
    for event in pygame.event.get():
        
        if ((((Game_array[0][0][0] == Game_array[0][1][0]) and (Game_array[0][0][0] == Game_array[0][2][0]))and Game_array[0][0][0] != 0) or
            (((Game_array[1][0][0] == Game_array[1][1][0]) and (Game_array[1][0][0] == Game_array[1][2][0]))and Game_array[1][0][0] != 0) or
            (((Game_array[2][0][0] == Game_array[2][1][0]) and (Game_array[2][0][0] == Game_array[2][2][0]))and Game_array[2][0][0] != 0) or
            (((Game_array[0][0][0] == Game_array[1][0][0]) and (Game_array[0][0][0] == Game_array[2][0][0]))and Game_array[0][0][0] != 0) or
            (((Game_array[0][1][0] == Game_array[1][1][0]) and (Game_array[0][1][0] == Game_array[2][1][0]))and Game_array[0][1][0] != 0) or
            (((Game_array[0][2][0] == Game_array[1][2][0]) and (Game_array[0][2][0] == Game_array[2][2][0]))and Game_array[0][2][0] != 0) or
            (((Game_array[2][0][0] == Game_array[1][1][0]) and (Game_array[2][0][0] == Game_array[0][2][0]))and Game_array[2][0][0] != 0) or
            (((Game_array[0][0][0] == Game_array[1][1][0]) and (Game_array[0][0][0] == Game_array[2][2][0]))and Game_array[0][0][0] != 0)):
            
            if turn1:
                print("winner is player2")
            open = False
            
            if not  turn1:
                print("winner is player1")
            open = False
            
        if event.type == pygame.QUIT:
            open = False

        if count == 9:
            print("Match is Drawn")
            open = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if(pygame.mouse.get_pressed()[0]):
                Pos = pygame.mouse.get_pos()
                if Game_array[Pos[0]//100][Pos[1]//100][0] == 0:
                    if turn1:
                        print("IIIIIIIIn true")
                        board.blit(
                            O_img, ((Pos[0]//100)*100, (Pos[1]//100)*100))
                        turn1 = False
                        Game_array[Pos[0]//100][Pos[1]//100][0] = 1

                    else:
                        print("IIIIIIIIn false")
                        board.blit(
                            X_img, ((Pos[0]//100)*100, (Pos[1]//100)*100))
                        turn1 = True
                        Game_array[Pos[0]//100][Pos[1]//100][0] = 2

                    print(Pos[0]//100, Pos[1]//100)
                    count += 1

    pygame.display.update()
pygame.quit()
quit()
