# MarbleMaze1.py
import socket                   # Import socket module
import time
import pygame
import Adafruit_ADXL345
import sys
import random
import os

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
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
def white_text(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()
    
def black_text(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()
    
def red_text(text, font):
    textSurface = font.render(text, True, (252,0,0))
    return textSurface, textSurface.get_rect()
    
def pink_text(text, font):
    textSurface = font.render(text, True, (241,140,142))
    return textSurface, textSurface.get_rect()
    
def score_text(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()
    
def timer_text(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()
    
def Score(Points):
  largeText = pygame.font.Font('freesansbold.ttf',15)
  TextSurf, TextRect = score_text("Score =" +str(Points), largeText)
  TextRect.center = ( ((width/2)-60),(460))
  screen.blit(TextSurf, TextRect)

def Wait(counter):
  wait_text = ["Get Ready!", "3","2","1","GO"]
  largeText = pygame.font.Font('freesansbold.ttf',30)
  TextSurf, TextRect = white_text(wait_text[counter], largeText)
  TextRect.center = ( ((width/2)),(height/2))
  screen.blit(TextSurf, TextRect)
  pygame.display.update()
  
def Display_timer(timer):

  largeText = pygame.font.Font('freesansbold.ttf',15)
  TextSurf, TextRect = score_text("Timer =" +str(timer), largeText)
  TextRect.center = ( ((width/2)+60),(460))
  screen.blit(TextSurf, TextRect)
  
def game_intro():
    Intro = True
    Play = False
    Info = False
    
    move = 0
    move1 = width
    while Intro:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()   
                start_click = Start_button.collidepoint(pos)
                info_click = Info_button.collidepoint(pos)
                if start_click:    
                    Intro = False
                    Play = True
                if info_click:    
                    Intro = False
                    Info = True   
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
               
        screen.fill(BLACK)

        largeText = pygame.font.Font('freesansbold.ttf',120)
        smallText = pygame.font.Font("freesansbold.ttf",20)
        
        TextSurf, TextRect = white_text("Marble Maze", largeText)
        TextRect.center = ((width/2),(height/4))
        screen.blit(TextSurf, TextRect)
        
        mouse = pygame.mouse.get_pos() 
        if 200+100 > mouse[0] > 200 and 320+40 > mouse[1] > 320:
            Start_button = pygame.draw.rect(screen, (241, 228, 228), (200,320,100,40))
        else:
            Start_button = pygame.draw.rect(screen, (151, 100, 199),(200,320,100,40))
        
        if 500+100 > mouse[0] > 500 and 320+40 > mouse[1] > 320:
            Info_button = pygame.draw.rect(screen,(21, 205, 168), (500,320,100,40)) 
        else:
            Info_button = pygame.draw.rect(screen, (9, 154, 151),(500,320,100,40))
        menu_words = ["Start", "Info"]
        menu_placement = [(250,340), (550,340)]
        
        textSurf, textRect = white_text(menu_words[0], smallText)
        textRect.center = menu_placement[0]
        screen.blit(textSurf, textRect) 
        textSurf, textRect = white_text(menu_words[1], smallText)
        textRect.center = menu_placement[1]
        screen.blit(textSurf, textRect)
        
        if move > width:
          move = 0
        else:
          move +=10
        if move1 < 0:
          move1 = width
        else:
          move1 -=10
        pygame.draw.circle(screen,(241, 228, 228),(move,270), 12)
        pygame.draw.circle(screen,(21, 205, 168),(move1,210), 12)
        pygame.draw.circle(screen,(151, 100, 199),(move,420), 12)
        pygame.draw.circle(screen,(9, 154, 151),(move1,400), 12)

        pygame.display.update()
        clock.tick(15)
    return Play,Info,Intro

def info_screen():
    Play = False
    Info = True
    Intro = False
    
    
    while Info:
        screen.fill((54,98,43))
        mouse = pygame.mouse.get_pos() 
        if 200+100 > mouse[0] > 200 and 320+40 > mouse[1] > 320:
            Start_button = pygame.draw.rect(screen, (198,227,119), (200,320,100,40))
        else:
            Start_button = pygame.draw.rect(screen, (114, 157, 57),(200,320,100,40))
        if 500+100 > mouse[0] > 500 and 320+40 > mouse[1] > 320:
            Back_button = pygame.draw.rect(screen,(198,227,119), (500,320,100,40)) 
        else:
            Back_button = pygame.draw.rect(screen, (114, 157, 57),(500,320,100,40))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()   
                start_click = Start_button.collidepoint(pos)
                back_click = Back_button.collidepoint(pos)
                if start_click:    
                    Play = True
                    Info = False  
                if back_click:    
                    Info = False
                    Intro = True   
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        info_words = ["Start", "Back", "Game Directions & Info", 
        "Lift the Board and tilt to move the marble.",
        "Avoid touching the wall! Beat the timer to win!", "Game by Corinne Ajemian and Keara Cole", "University of Rhode Island ELE409 2019"]
        info_placement = [(250,340), (550,340), ((width/2), 50), ((width/2), 125), ((width/2), 175), ((width/2), 225), ((width/2), 275)]       
        #Start
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = white_text(info_words[0], smallText)
        textRect.center = info_placement[0]
        screen.blit(textSurf, textRect)
        #Back
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = white_text(info_words[1], smallText)
        textRect.center = info_placement[1]
        screen.blit(textSurf, textRect)
        #Game Directions & Info
        largeText = pygame.font.Font('freesansbold.ttf',60)
        TextSurf, TextRect = white_text(info_words[2], largeText)
        TextRect.center = info_placement[2]
        screen.blit(TextSurf, TextRect)
        #Lift the Board and tilt to move the marble.
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = white_text(info_words[3], smallText)
        textRect.center = info_placement[3]
        screen.blit(textSurf, textRect)
        #Avoid touching the wall! Beat the timer to win!.
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = white_text(info_words[4], smallText)
        textRect.center = info_placement[4]
        screen.blit(textSurf, textRect)
        #Game by Corinne Ajemian and Keara Cole
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = white_text(info_words[5], smallText)
        textRect.center = info_placement[5]
        screen.blit(textSurf, textRect)
        #URI ELE409 2019
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = white_text(info_words[6], smallText)
        textRect.center = info_placement[6]
        screen.blit(textSurf, textRect)
         
        pygame.display.update()
        clock.tick(15)
    return Play,Info,Intro

def game_win(Points):

    Win = True
    while Win:
        screen.fill((7,13,89))
        mouse = pygame.mouse.get_pos() 
        if 3600+100 > mouse[0] > 360 and 320+40 > mouse[1] > 320:
            Restart_button = pygame.draw.rect(screen, (206,221,239), (350,320,100,40))
        else:
            Restart_button = pygame.draw.rect(screen, (88, 147, 212),(350,320,100,40))
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()   
                is_inside = Restart_button.collidepoint(pos)
                if is_inside:    
                    Win = False
                    Intro = True
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        win_words = ["Restart"]
        win_placement = [(400,340)]       
        #Start
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = black_text(win_words[0], smallText)
        textRect.center = win_placement[0]
        screen.blit(textSurf, textRect)
        
        largeText = pygame.font.Font('freesansbold.ttf',120)
        TextSurf, TextRect = white_text("YOU WIN", largeText)
        TextRect.center = ((width/2),(height/4))
        screen.blit(TextSurf, TextRect)
        
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = white_text("Score = " +str(Points), largeText)
        TextRect.center = ( ((width/2)),200)
        screen.blit(TextSurf, TextRect)
        pygame.display.update()
        
        clock.tick(15)
    return Intro, Win
           
def game_over():

    Lose = True
    while Lose:
        screen.fill((95,0,0))
        mouse = pygame.mouse.get_pos() 
        if 3600+100 > mouse[0] > 360 and 320+40 > mouse[1] > 320:
            Restart_button = pygame.draw.rect(screen, (221,0,0), (350,320,100,40))
        else:
            Restart_button = pygame.draw.rect(screen, (189, 0, 0),(350,320,100,40))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()   
                is_inside = Restart_button.collidepoint(pos) 
                if is_inside:    
                    Lose = False
                    Intro = True
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
               
        largeText = pygame.font.Font('freesansbold.ttf',120)
        TextSurf, TextRect = red_text("Game Over!", largeText)
        TextRect.center = ((width/2),(height/4))
        screen.blit(TextSurf, TextRect)

        lose_words = ["Restart"]
        lose_placement = [(400,340)]       
        #Restart
        smallText = pygame.font.Font("freesansbold.ttf",20)
        textSurf, textRect = red_text(lose_words[0], smallText)
        textRect.center = lose_placement[0]
        screen.blit(textSurf, textRect)
        
        pygame.display.update()
        clock.tick(15)
    return Intro, Lose
            
def updatePoints():
  a, b, c = accel.read()
  float(a)
  float(b)
  print('X={0}, Y={1}'.format(a, b))
  if a > 2:
    RIGHT = 1
    Rratio = abs((a/255.0) * 10.0) * 3.0
  else: 
    RIGHT = Rratio = 0
  if a < -12:
    LEFT = 1
    Lratio = abs((a/270.0) * 10.0) * 3.0
  else: 
    LEFT = Lratio = 0
  if b < -15:
    DOWN = 1
    Dratio = abs((b/262.0) * 10.0) * 3.0
  else:
    DOWN = Dratio = 0
  if b > -7:
    UP = 1
    Uratio = abs((b/252.0) * 10.0) * 3.0
  else:
    UP = Uratio = 0
  return DOWN, Dratio, LEFT, Lratio, RIGHT, Rratio, UP, Uratio
  
def game(player, end_rect): 
  Play = True
  #Set levels to begin and end with
  Level = 1
  Final_Level = 3
  Points = 100
  lvls_winpoints = [100, 200, 300]
  #Set Colors
  Wall_color = (127, 71, 130)
  Player_color = (253, 208, 67)
  Background_color = (226, 89,139)
  Goal_color = (170, 92, 159)
  #Directions
  DOWN = LEFT = RIGHT = UP = 0
  #Timer values
  lvls_timer = [35, 35, 15]
  lvl_counter = 0
  timer = lvls_timer[lvl_counter]
  minutes = 0
  time_start = time.time()
  while Play:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit(); sys.exit();
    #start game timer for points
    seconds = int(time.time() - time_start) - minutes * 60
    print(seconds)
    #Reset Screen
    screen.fill(Background_color)
    if seconds < 5:
      for wall in walls:
      	pygame.draw.rect(screen, Wall_color, wall.rect)
      Wait(seconds)
    else:
      #Update movement
      if DOWN == 1:
        player.move(0, Dratio)
      if UP == 1:
        Uratio = Uratio * -1
        player.move(0, Uratio)
      if RIGHT == 1:
        player.move(Rratio, 0)
      if LEFT == 1:
        Lratio = Lratio * -1
        player.move(Lratio, 0)
      DOWN, Dratio, LEFT, Lratio, RIGHT, Rratio, UP, Uratio = updatePoints()
      # Draw marble over Rect
      (x,y,a,b)=player.rect
      x= x+6
      y= y+6
      marble=pygame.draw.circle(screen,Player_color,(x,y), 12)
      # Time Count Down
      if timer > 0:
        timer = lvls_timer[lvl_counter] - seconds
      else:
        Play = False
        Win = False
        Lose = True          
      for wall in walls:
        if  marble.colliderect(wall.rect):
          Points = Points - 1
          if Points <= 0:
            Points = 0         
      #New Level
      if player.rect.colliderect(end_rect):
        time_start = time.time()
        Points += lvls_winpoints[lvl_counter]
        lvl_counter +=1
        Points += timer
        timer = 60    
        if Level == Final_Level:
          Play = False
          Win = True
          Lose = False
        elif Level ==2:
          Level = 3
          del walls[:]
          Wall_color = (227, 227, 227)
          Player_color = (203, 55, 55)
          Background_color = (238, 111, 87)
          Goal_color = (250, 250, 250)
          Start_place = (400,32, 12, 12)
          player.rect = pygame.Rect(Start_place)
          x = y = 0
          for row in level3:
              for col in row:
                  if col == "W":
                      Wall((x, y))
                  if col == "E":
                      end_rect = pygame.Rect(x, y, 80, 16)
                  x += 16
              y += 16
              x = 0
        elif Level == 1:
          Level = 2
          del walls[:]
          Wall_color = (205, 69, 69)
          Player_color = (241, 104, 33)
          Background_color = (243, 163, 51)
          Goal_color = (255, 254, 154)
          Start_place = (750,32, 12, 12)
          player.rect = pygame.Rect(Start_place)
          x = y = 0
          for row in level2:
              for col in row:
                  if col == "W":
                      Wall((x, y))
                  if col == "E":
                      end_rect = pygame.Rect(x, y, 16, 80)
                  x += 16
              y += 16
              x = 0
      #Draw screen
      for wall in walls:
      	pygame.draw.rect(screen, Wall_color, wall.rect)
      Score(Points)
      Display_timer(timer)
      pygame.draw.rect(screen, Goal_color, end_rect)
      pygame.draw.rect(screen, Player_color, player.rect)
      pygame.display.flip()
      #Sleep Time
      time_elapsed = (time.time() - time_start)
      #print(time_elapsed)
      time.sleep(0.1)
  return Play, Win, Lose, Points 

Game = True
Intro = True
Lose = False
Win = False
while Game:      
  walls = []
  Start_place = (50,50,12,12)
  player = Player() # Create the player
  level1 = [         #50 by 30
  "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
  "W     WW                                         E",
  "W     WW                                          ",
  "W     WW                                          ",
  "W     WW       WWWWWWWWWWWWWWWWWWWWWWWWWWWWW     W",
  "W     WW       WWWWWWWWWWWWWWWWWWWWWWWWWWWWW     W",
  "W     WW                                  WW     W",
  "W     WW                                  WW     W",
  "W     WW                                  WW     W",
  "W     WWWWWWWWWWWWW       WWWWWWW         WW     W",
  "W     WWWWWWWWWWWWW       WWWWWWW         WW     W",
  "W                WW                       WW     W",
  "W                WW                       WW     W",
  "W                WW                       WW     W",
  "W     WW         WWWWWWWWWWWWWWWW         WW     W",
  "W     WW         WWWWWWWWWWWWWWWW         WW     W",
  "W     WW         WW                       WW     W",
  "W     WW         WW                       WW     W",
  "W     WW         WW               WWWWWWWWWWWWWWWW",
  "W     WW         WW               WWWWWWWWWWWWWWWW",
  "W     WW                                         W",
  "W     WW                                         W",
  "W     WW                                         W",
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
  "E     WW                                         W",
  "      WW                                         W",
  "      WW                                         W",
  "W     WW       WWWWWWWWWWWWWWWWWWWWWWWWWWWWW     W",
  "W     WW       WWWWWWWWWWWWWWWWWWWWWWWWWWWWW     W",
  "W     WW                                  WW     W",
  "W     WW                                  WW     W",
  "W     WW                                  WW     W",
  "W     WWWWWWWWWWWWW       WWWWWWW         WW     W",
  "W     WWWWWWWWWWWWW       WWWWWWW         WW     W",
  "W                WW                       WW     W",
  "W                WW                       WW     W",
  "W                WW                       WW     W",
  "W     WW         WWWWWWWWWWWWWWWW         WW     W",
  "W     WW         WWWWWWWWWWWWWWWW         WW     W",
  "W     WW         WW                       WW     W",
  "W     WW         WW                       WW     W",
  "W     WW         WW               WWWWWWWWWWWWWWWW",
  "W     WW         WW               WWWWWWWWWWWWWWWW",
  "W     WW                                         W",
  "W     WW                                         W",
  "W     WW                                         W",
  "W     WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW      W",
  "W     WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW      W",
  "W                                                W",
  "W                                                W",
  "W                                                W",
  "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
  "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
  ]
  level3 = [         #50 by 30
  "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
  "W   E               WW      WW     E             W",
  "W                   WW      WW                   W",
  "W                   WW      WW                   W",
  "W                   WW      WW                   W",
  "W         WW        WW      WW        WW         W",
  "W         WW        WW      WW        WW         W",
  "W         WW        WW      WW        WW         W",
  "W         WW        WW      WW        WW         W",
  "W         WWWWWWWWWWWW      WWWWWWWWWWWW         W",
  "W         WWWWWWWWWWWW      WWWWWWWWWWWW         W",
  "W                   WW      WW                   W",
  "W                   WW      WW                   W",
  "W                   WW      WW                   W",
  "W     WW            WW      WW            WW     W",
  "W     WW            WW      WW            WW     W",
  "W     WW            WW      WW            WW     W",
  "W     WW            WW      WW            WW     W",
  "W     WW            WW      WW            WW     W",
  "W     WW            WW      WW            WW     W",
  "W     WW            WW      WW            WW     W",
  "W     WW            WW      WW            WW     W",
  "W     WW            WW      WW            WW     W",
  "W     WWWWWWWWWWWWWWWW      WWWWWWWWWWWWWWWW     W",
  "W     WWWWWWWWWWWWWWWW      WWWWWWWWWWWWWWWW     W",
  "W                                                W",
  "W                                                W",
  "W                                                W",
  "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
  "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
  ]
  x = y = 0
  for row in level1:
      for col in row:
          if col == "W":
              Wall((x, y))
          if col == "E":
              end_rect = pygame.Rect(x, y, 16, 80)
          x += 16
      y += 16
      x = 0
  count = 0

  #Initialize screen, clock, G-Senosr, Game
  screen = pygame.display.set_mode(size)
  clock = pygame.time.Clock()
  accel = Adafruit_ADXL345.ADXL345(address=0x53, busnum=0)     
  pygame.init()
  #Functions for different screens
  if Intro:
    Play,Info,Intro = game_intro()
  elif Info:
    Play,Info,Intro = info_screen()
  elif Play:
    Play, Win, Lose, Points = game(player, end_rect)
  elif Lose:
    Intro, Lose = game_over()
  elif Win:
    Intro, Win = game_win(Points)

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
