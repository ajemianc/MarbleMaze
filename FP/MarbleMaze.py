# draw.py
# # apt-get install python-pygame  or pip install pygame
import socket                   # Import socket module
import time
import sys
import pygame
import Adafruit_ADXL345
pygame.init()
accel = Adafruit_ADXL345.ADXL345(address=0x53, busnum=0)

WHITE = (255,255,255)
RED = (255, 0, 0)
BLACK = (0,0,0)
size = width, height = 800, 480
screen = pygame.display.set_mode(size)
LEFT = 1
RIGHT = 3
MID = 2
theDrawing = []
Drawings = []
down = 0
level = 1	#start at level 1
xc = 50		#x-coordinate (starting position)
yc = 50		#y-coordinate (starting position)
debugCount = 30

#Create a timer
time_start = time.time()
seconds = 0
minutes = 0

while True:
	sys.stdout.write("\r{minutes} Minutes {seconds} Seconds".format(minutes=minutes, seconds=seconds))
        sys.stdout.flush()
        time.sleep(1)
        seconds = int(time.time() - time_start) - minutes * 60
        if seconds >= 60:
            minutes += 1
            seconds = 0
    #except KeyboardInterrupt, e:
        #break
	print('Printing X, Y, Z axis values, press Ctrl-C to quit...')
    	# Read the X, Y, Z axis acceleration values and print them.
    	x, y, z = accel.read()
    	print('X={0}, Y={1}, Z={2}'.format(x, y, z))
    	# Wait half a second and repeat.
    	time.sleep(0.5)
    	while seconds %1==0:
        	screen.fill(WHITE)
       		#x,y = pygame.mouse.get_pos()
		#pygame.draw.circle(screen,BLACK,(xc,y), 15)
		xc = xc + 20
		#yc = yc + 20
		#if x > tempx+5
	    	pygame.draw.circle(screen,BLACK,(xc,yc), 20)

        	pygame.image.save(screen, "screenshot.png")
		pygame.display.flip()
"""
	print('Printing X, Y, Z axis values, press Ctrl-C to quit...')
    	# Read the X, Y, Z axis acceleration values and print them.
    	x, y, z = accel.read()
    	print('X={0}, Y={1}, Z={2}'.format(x, y, z))
    	# Wait half a second and repeat.
    	time.sleep(0.5)
    	for event in pygame.event.get():
        	screen.fill(WHITE)
       		#x,y = pygame.mouse.get_pos()
		#pygame.draw.circle(screen,BLACK,(xc,y), 15)
		xc = xc + 20
		#yc = yc + 20
		#if x > tempx+5
	    	pygame.draw.circle(screen,BLACK,(xc,yc), 20)


	if seconds %1 ==0: #event occurs every second rather than mouse button
		print('seconds loop taken')
        pygame.image.save(screen, "screenshot.png")
	pygame.display.flip()

"""

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

