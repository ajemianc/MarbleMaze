# draw.py
# # apt-get install python-pygame  or pip install pygame
import socket                   # Import socket module
import time
import pygame
import Adafruit_ADXL345
import sys
import random
import os

#from Player import Player 
#from Player import Wall 
#Variables
#Colors
WHITE = (255,255,255)
RED = (255, 0, 0)
BLACK = (0,0,0)
GREEN = (30, 105, 53)
GOLD = (255, 215, 0)
DARK_PURPLE = (92, 46, 152)
#Level 1 Colors
PINK1 = (254, 233, 236)
GREEN1 = (230, 255, 182)
BLUE1 = (182, 255, 244)
PURPLE1 = (208, 182, 255)
#Level 2 Colors
PINK2 = (255, 106, 222)
GREEN2 = (106,255,139)
BLUE2 = (106,147,255)
YELLOW2 = (255, 214, 106)
#Level 3 Colors
RED3 = (255, 86, 89)
GREEN3 = (172,255,89)
BLUE3 = (89,255,255)
PURPLE3 = (172, 89, 255)
#Sizes
size = width, height = 800, 480

##Player.py
class Player(object):
 def __init__(self):
   self.rect = pygame.Rect(Start_place)
 def move(self, dx, dy):
   if dx !=0:
     self.move_single_axis(dx,0)
   if dy !=0:
     self.move_single_axis(0,dy)
 
 def move_single_axis(self, dx, dy):
   self.rect.x += dx
   self.rect.y += dy
   
   for wall in walls:
     if self.rect.colliderect(wall.rect):
        if dx > 0: # Moving right; Hit the left side of the wall
          self.rect.right = wall.rect.left
        if dx < 0: # Moving left; Hit the right side of the wall
          self.rect.left = wall.rect.right
        if dy > 0: # Moving down; Hit the top side of the wall
          self.rect.bottom = wall.rect.top
        if dy < 0: # Moving up; Hit the bottom side of the wall
          self.rect.top = wall.rect.bottom
##Wall.py
class Wall(object):
  def __init__(self, pos):
    walls.append(self)
    self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
#############Functions###############
running = True
def srtscreen_text(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()
    
def score_text(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()
    
def Score(Points):

  largeText = pygame.font.Font('freesansbold.ttf',15)
  TextSurf, TextRect = score_text("Score =" +str(Points), largeText)
  TextRect.center = ( ((width/2)-20),(460))
  screen.blit(TextSurf, TextRect)
  
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()   
                is_inside = Start_button.collidepoint(pos) 
                if is_inside:    
                    intro = False
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
               
        screen.fill(BLACK)
        largeText = pygame.font.Font('freesansbold.ttf',120)
        TextSurf, TextRect = srtscreen_text("Marble Maze", largeText)
        TextRect.center = ((width/2),(height/4))
        screen.blit(TextSurf, TextRect)
        
        mouse = pygame.mouse.get_pos() 
        if 200+100 > mouse[0] > 150 and 360+40 > mouse[1] > 450:
            Start_button = pygame.draw.rect(screen, PURPLE1, (200,360,100,40))
        else:
            Start_button = pygame.draw.rect(screen, GREEN1,(200,360,100,40))

        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = srtscreen_text("Start", smallText)
        textRect.center = ( (200+(100/2)), (360+(40/2)) )
        screen.blit(textSurf, textRect)
        
        End_button = pygame.draw.rect(screen, (255, 255, 255), (500,360,100,40)) 
        
        pygame.display.update()
        clock.tick(15)
        
def updatePoints():
  a, b, c = accel.read()
  float(a)
  float(b)
  print('X={0}, Y={1}'.format(a, b))
  if a > 2:
    RIGHT = 1
    Rratio = abs((a/255.0) * 10.0) * 2.0
  else: 
    RIGHT = Rratio = 0
  if a < -12:
    LEFT = 1
    Lratio = abs((a/270.0) * 10.0) * 2.0
  else: 
    LEFT = Lratio = 0
  if b < -15:
    DOWN = 1
    Dratio = abs((b/262.0) * 10.0)
  else:
    DOWN = Dratio = 0
  if b > -7:
    UP = 1
    Uratio = abs((b/252.0) * 10.0) * 2.0
  else:
    UP = Uratio = 0
  return DOWN, Dratio, LEFT, Lratio, RIGHT, Rratio, UP, Uratio
  
def game(player, end_rect): 
  Points = 75
  Level = 1
  Final_Level = 3
  while (True):
    Wall_color = PURPLE1
    Player_color = BLUE1
    Background_color = PINK1
    Goal_color = GREEN1
    #Directions
    DOWN = LEFT = RIGHT = UP = 0
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit(); sys.exit();
  
      constant = 1
      time_start = time.time()
      #Start position of Marble
      x = 32
      y = 32
      minutes = 0
      num = 0
      while constant %1==0:
          #start game timer for points
          seconds = int(time.time() - time_start) - minutes * 60
          #Reset Screen
          screen.fill(Background_color)
          #Update movement
          #print('X={0}, Y={1}'.format(x, y))
          if DOWN == 1:
            player.move(0, Dratio)
          if UP == 1:
            print(Uratio)
            Uratio = Uratio * -1
            player.move(0, Uratio)
          if RIGHT == 1:
            print(Rratio)
            player.move(Rratio, 0)
          if LEFT == 1:
            print(Lratio)
            Lratio = Lratio * -1
            player.move(Lratio, 0)
          DOWN, Dratio, LEFT, Lratio, RIGHT, Rratio, UP, Uratio = updatePoints()
          # Draw marble over Rect
          (x,y,a,b)=player.rect
          x= x+6
          y= y+6
          marble=pygame.draw.circle(screen,Player_color,(x,y), 12)
          # Score keeper
          #print("Points =",Points)
          #if seconds%10 == 0:
          Points = seconds
          
          for wall in walls:
            if  marble.colliderect(wall.rect):
                Points = Points - 1
          if player.rect.colliderect(goal_rect):
            Points +=100
            
          #New Level
          if player.rect.colliderect(end_rect):    
            if Level == Final_Level:
              #game_end()
              print("Game Over")
            elif Level ==2:
              Level = 3
              del walls[:]
              Wall_color = RED3
              Player_color = GREEN3
              Background_color = BLUE3
              Goal_color = PURPLE3
              Start_place = (300,32, 12, 12)
              player = Player() # Create the player
              x = y = 0
              for row in level3:
                  for col in row:
                      if col == "W":
                          Wall((x, y))
                      if col == "E":
                          end_rect = pygame.Rect(x, y, 16, 16)
                      x += 16
                  y += 16
                  x = 0
            if Level == 1:
              Level = 2
              del walls[:]
              Wall_color = YELLOW2
              Player_color = GREEN2
              Background_color = PINK2
              Goal_color = GREEN2
              Start_place = (300,32, 12, 12)
              player = Player() #Reset Player
              x = y = 0
              for row in level2:
                  for col in row:
                      if col == "W":
                          Wall((x, y))
                      if col == "E":
                          end_rect = pygame.Rect(x, y, 16, 16)
                      x += 16
                  y += 16
                  x = 0
          #Draw screen
          for wall in walls:
          	pygame.draw.rect(screen, Wall_color, wall.rect)
          Score(Points)
          pygame.draw.rect(screen, RED3, goal_rect)
          pygame.draw.rect(screen, Goal_color, end_rect)
          pygame.draw.rect(screen, Player_color, player.rect)
          pygame.display.flip()
          #Sleep Time
          time_elapsed = (time.time() - time_start)
          #print(time_elapsed)
          time.sleep(0.1)
          
Start_place = ((width/2),(height/2),12,12)
walls = []
player = Player() # Create the player
level1 = [         #50 by 30
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W     WW                                         W",
"W     WW                                         W ",
"W     WW                                         W ",
"W     WW       WWWWWWWWWWWWWWWWWWWWWWWWWWWWW     W",
"W     WW       WWWWWWWWWWWWWWWWWWWWWWWWWWWWW     W",
"W     WW                                  WW     W",
"W     WW                                  WW     W",
"W     WW     G                            WW     W",
"W     WWWWWWWWWWWWW       WWWWWWW         WW     W",
"WG    WWWWWWWWWWWWW       WWWWWWW         WW     W",
"W                WW                       WW     W",
"W                WW                       WW     W",
"W     WW         WW                       WW     W",
"W     WW         WWWWWWWWWWWWWWWWWWE      WW     W",
"W     WW         WWWWWWWWWWWWWWWWWW       WW     W",
"W     WW         WW                       WW     W",
"W     WW         WW                       WW     W",
"W     WW         WW             WWWWWWWWWWWWWWWWWW",
"W     WW         WW             WWWWWWWWWWWWWWWWWW",
"W     WW G                                       W",
"W     WW                                         W",
"W     WW                    WWWWWWWWWWWWWWW      W",
"W     WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW      W",
"W     WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW      W",
"W                                                W",
"W                                                W",
"W                                                W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]
level2 = [         #50 by 30
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"W                                                W",
"WEG                                              W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]
level3 = [         #50 by 30
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
"W                                                E",
"W                                                 ",
"W     WW                                          ",
"W     WW                                         W",
"W     WW                                         W",
"W     WW                                  WW     W",
"W     WW                                  WW     W",
"W     WW                                  WW     W",
"W     WWWWWWWWWWWWW       WWWWWWW         WW     W",
"W     WWWWWWWWWWWWW       WWWWWWW         WW     W",
"W                WW       WWWWWWW         WW     W",
"W                WW                       WW     W",
"W     WW         WW                       WW     W",
"W     WW         WWWWWWWWWWWWWWWWWW       WW     W",
"W     WW         WWWWWWWWWWWWWWWWWW       WW     W",
"W     WW         WW                       WW     W",
"W     WW         WW                       WW     W",
"W     WW         WW             WWWWWWWWWWWWWWWWWW",
"W     WW         WW             WWWWWWWWWWWWWWWWWW",
"W     WW         WW                              W",
"W     WW         WW                              W",
"W     WW                    WWWWWWWWWWWWWWW      W",
"W     WW                    WWWWWWWWWWWWWWW      W",
"W     WW                    WWWWWWWWWWWWWWW      W",
"W     WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW      W",
"W     WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW      W",
"W                                                W",
"W                                                W",
"WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
]
x = y = 0
for row in level2:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 80, 16)
        if col == "G":
            goal_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0
count = 0

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
accel = Adafruit_ADXL345.ADXL345(address=0x53, busnum=0)     
pygame.init()
game_intro()
game(player, end_rect)   

#######SOCKET Portion###############   	
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 40000                    # Reserve a port for your service.

s.connect(('131.128.49.109', port))
# Try get some sleep
time.sleep(3)
filename='screenshot.png'
f = open(filename,'rb')
l = f.read(1024)
while (l):
  s.send(l)
  l = f.read(1024)
f.close()

print('Done sending')
s.close()
print('connection closed')
