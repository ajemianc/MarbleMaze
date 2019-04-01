# draw.py
# # apt-get install python-pygame  or pip install pygame
import socket                   # Import socket module
import time
import pygame
import Adafruit_ADXL345
pygame.init()
accel = Adafruit_ADXL345.ADXL345(address=0x53, busnum=0)

#Variables
#Colors
WHITE = (255,255,255)
RED = (255, 0, 0)
BLACK = (0,0,0)
#Sizes
size = width, height = 800, 480
screen = pygame.display.set_mode(size)
#Directions
DOWN = 0
LEFT = 1
RIGHT = 3
MID = 2
#Drawings
theDrawing = []
Drawings = []
#Levels
Level = 1	#start at level 1
#coordinates
xc = 50		#x-coordinate (starting position)
yc = 50		#y-coordinate (starting position)
color = RED
clock = pygame.time.Clock()
x = 50
y = 50

def updatePoints(x,y):
  #x, y, z = accel.read()
  x +=3
  y +=3
  return x,y

while (True):
 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit(); sys.exit();
    for i in range(0,10):
  #erase the screen
      screen.fill(WHITE)

  # Read the X, Y, Z axis acceleration values and print them.
      
      
      pygame.draw.circle(screen,color,(x,y), 15)
      x, y, z = accel.read()
      print('X={0}, Y={1}'.format(x, y))
      x = abs(x)
      x = x * 3
      x = int(x)
      y = abs(y)
      y = y * 1.7
      y = round(y,0)
      y = int(y)
      #pygame.draw.circle(screen,color,(x,y), 15)
      pygame.display.flip()
    
  #for i in range(0,10):
  #    x, y, z = accel.read()
  #    print('X={0}, Y={1}, Z={2}'.format(x, y, z))
  
  #    pygame.display.flip()
  #    clock.tick(60)
#######SOCKET Portion###############   	
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == MID:
      pygame.image.save(screen, "screenshot.png")
 
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
