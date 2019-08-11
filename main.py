import pygame
from life import *

pygame.init()
screen = pygame.display.set_mode((300,300))
pygame.display.set_caption("It's life!!!")

x,y = 15,15
width,height = 30,30
velocity = 5
board = dead_state(50,50)


run = True

def render(board, screen):
   rec_width = 300/50
   rec_height = 300/50
   pink = (232,149,240)
   grey = (60,60,60)
   for x in range(50):
      for y in range(50):
         if board[x][y] == 1:
            pygame.draw.rect(screen,grey,(x*6,y*6,rec_width,rec_height))

while run:
   pygame.draw.rect(screen,(255,255,255),(0,0,300,300))
   render(board, screen)
   pygame.time.delay(80)
   board = next_board_state(board)
   render(board, screen)
   pygame.display.flip()
   for event in pygame.event.get():
      if event.type == pygame.MOUSEMOTION:
         x,y = pygame.mouse.get_pos()
         for i in range(int(x/6)-3,int(x/6)+2):
            for j in range(int(y/6)-3,int(y/6)+2):
               try:
                  board[i][j] = 1
               except IndexError:
                  pass
      if event.type == pygame.QUIT:
         run = False

