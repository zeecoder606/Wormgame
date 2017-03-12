# TestGame.py
#
# Copyright (C) 2016 Abhijit Patel Here
#
# This program is free software; you can redistribute it
# and/or modify it under the terms of the GNU General
# Public License as published by the Free Software
# Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even
# the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public
# License for more details.
#
# You should have received a copy of the GNU General
# Public License along with this program; if not, write
# to the Free Software Foundation, Inc., 51 Franklin
# St, Fifth Floor, Boston, MA 02110-1301  USA
#wormgame
import random, pygame, sys
from pygame.locals import *
from gi.repository import Gtk
FPS = 15
WINDOWWIDTH = 1000
WINDOWHEIGHT = 680
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

        
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BGCOLOR = BLACK
BROWN     = (200, 128, 0)
BLUE      = (0, 0, 255)
             
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
FPSCLOCK= None 
DISPLAYSURF=None
BASICFONT=None
HEAD = 0 
HEAD = 0 

def main():
   

    pygame.init()
   
    
    game = wormgame()
    
    
    game.run()
        

class wormgame:
    def __init__(self):
        pass
    def run(self):
        global FPSCLOCK, DISPLAYSURF, BASICFONT, WINDOWWIDTH, WINDOWHEIGHT
        DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        pygame.display.set_caption('Wormy')
        FPSCLOCK = pygame.time.Clock()
        showStartScreen()
        startx = random.randint(2, CELLWIDTH - 6)
        starty = random.randint(1, 4)
        wormCoords = [{'x': startx,     'y': starty},
                      {'x': startx - 1, 'y': starty},
                      {'x': startx - 2, 'y': starty}]
        direction = RIGHT
        #showStartScreen()
        # Start the apple in a random place.
        apple = getRandomLocation()

        while True: # main game loop
            while Gtk.events_pending():
                Gtk.main_iteration()
            for event in pygame.event.get(): # event handling loop
                if event.type == QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN:
                   
                    if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                        direction = LEFT
                    elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                        direction = RIGHT
                    elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                        direction = UP
                    elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                        direction = DOWN
                    elif event.key == K_ESCAPE:
                        terminate()


            if wormCoords[HEAD]['x'] in range(12,32) and wormCoords[HEAD]['y'] == 22:
                showGameOverScreen() # game over
                is_true = True
                while is_true:
                     while Gtk.events_pending():
                         Gtk.main_iteration()
                    
                     for event in pygame.event.get():
                        
                        if event.type == pygame.KEYDOWN:
                          
                           startx = random.randint(5, CELLWIDTH - 10)
                           starty = random.randint(29, CELLHEIGHT - 2)
                           wormCoords = [{'x': startx,     'y': starty},
                                         {'x': startx - 1, 'y': starty},
                                         {'x': startx - 2, 'y': starty}]
                           direction = RIGHT
                           apple = getRandomLocation()
                           is_true = False

            elif wormCoords[HEAD]['x'] in range(18,38) and wormCoords[HEAD]['y'] == 12:
                showGameOverScreen() # game over
                is_true = True
                while is_true:
                     while Gtk.events_pending():
                         Gtk.main_iteration()
                    
                     for event in pygame.event.get():
                       
                        if event.type == pygame.KEYDOWN:
                           
                           
                           startx = random.randint(5, CELLWIDTH - 10)
                           starty = random.randint(29, CELLHEIGHT - 3)
                           wormCoords = [{'x': startx,     'y': starty},
                                         {'x': startx - 1, 'y': starty},
                                         {'x': startx - 2, 'y': starty}]
                           direction = RIGHT
                           apple = getRandomLocation()
                           is_true = False
            elif wormCoords[HEAD]['x'] in range(12,44) and wormCoords[HEAD]['y'] == 6:
                showGameOverScreen() # game over
                is_true = True
                while is_true:
                     while Gtk.events_pending():
                         Gtk.main_iteration()
                    
                     for event in pygame.event.get():
                        
                        if event.type == pygame.KEYDOWN:
                          
                           
                           startx = random.randint(5, CELLWIDTH - 5)
                           starty = random.randint(29, CELLHEIGHT - 2)
                           wormCoords = [{'x': startx,     'y': starty},
                                         {'x': startx - 1, 'y': starty},
                                         {'x': startx - 2, 'y': starty}]
                           direction = RIGHT
                           apple = getRandomLocation()
                           is_true = False
            elif wormCoords[HEAD]['x'] in range(6,44) and wormCoords[HEAD]['y'] == 28:
                showGameOverScreen() # game over
                is_true = True
                while is_true:
                     while Gtk.events_pending():
                         Gtk.main_iteration()
                    
                     for event in pygame.event.get():
                       
                        if event.type == pygame.KEYDOWN:
                           
                           
                           startx = random.randint(5, CELLWIDTH - 10)
                           starty = random.randint(29, CELLHEIGHT - 3)
                           wormCoords = [{'x': startx,     'y': starty},
                                         {'x': startx - 1, 'y': starty},
                                         {'x': startx - 2, 'y': starty}]
                           direction = RIGHT
                           apple = getRandomLocation()
                           is_true = False
                     
            elif wormCoords[HEAD]['x'] == 6 and wormCoords[HEAD]['y'] in range(6,28):
                showGameOverScreen() # game over
                is_true = True
                while is_true:
                     while Gtk.events_pending():
                          Gtk.main_iteration()
                     for event in pygame.event.get():
                        
                        if event.type == pygame.KEYDOWN:
                            
                            
                            startx = random.randint(5, CELLWIDTH - 10)
                            starty = random.randint(29, CELLHEIGHT - 3)
                            wormCoords = [{'x': startx,     'y': starty},
                                          {'x': startx - 1, 'y': starty},
                                          {'x': startx - 2, 'y': starty}]
                            direction = RIGHT
                            apple = getRandomLocation()
                            is_true = False  
            elif wormCoords[HEAD]['x'] == 12 and wormCoords[HEAD]['y'] in range(12,22):
                showGameOverScreen() # game over
                is_true = True
                while is_true:
                     while Gtk.events_pending():
                          Gtk.main_iteration()
                     for event in pygame.event.get():
                       
                        if event.type == pygame.KEYDOWN:
                         
                           startx = random.randint(3, CELLWIDTH - 5)
                           starty = random.randint(1, 5)
                           wormCoords = [{'x': startx,     'y': starty},
                                         {'x': startx - 1, 'y': starty},
                                         {'x': startx - 2, 'y': starty}]
                           direction = RIGHT
                           apple = getRandomLocation()
                           is_true = False
            elif wormCoords[HEAD]['x'] == 38 and wormCoords[HEAD]['y'] in range(12,22):
                showGameOverScreen() # game over
               
                is_true = True
                while is_true:
                     while Gtk.events_pending():
                          Gtk.main_iteration()
                     for event in pygame.event.get():
                       
                        if event.type == pygame.KEYDOWN:
                          
                           startx = random.randint(2, 7)
                           starty = random.randint(1, 5)
                           wormCoords = [{'x': startx,     'y': starty},
                                         {'x': startx - 1, 'y': starty},
                                         {'x': startx - 2, 'y': starty}]
                           direction = RIGHT
                           apple = getRandomLocation()
                           is_true = False

            elif wormCoords[HEAD]['x'] == 44 and wormCoords[HEAD]['y'] in range(6,22):
                showGameOverScreen() # game over
               
                is_true = True
                while is_true:
                     while Gtk.events_pending():
                          Gtk.main_iteration()
                     for event in pygame.event.get():
                       
                        if event.type == pygame.KEYDOWN:
                           
                           startx = random.randint(3, CELLWIDTH - 5)
                           starty = random.randint(29, CELLHEIGHT - 2)
                           wormCoords = [{'x': startx,     'y': starty},
                                         {'x': startx - 1, 'y': starty},
                                         {'x': startx - 2, 'y': starty}]
                           direction = RIGHT
                           apple = getRandomLocation()
                           is_true = False          
            for wormBody in wormCoords[1:]:
                if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                    showGameOverScreen() # game over
                    is_true = True
                    while is_true:
                     while Gtk.events_pending():
                        Gtk.main_iteration()   
                     for event in pygame.event.get():
                      
                        if event.type == pygame.KEYDOWN:
                          
                          startx = random.randint(5, CELLWIDTH - 10)
                          starty = random.randint(29, CELLHEIGHT - 2)
                          wormCoords = [{'x': startx,     'y': starty},
                                        {'x': startx - 1, 'y': starty},
                                        {'x': startx - 2, 'y': starty}]
                          direction = RIGHT
                          apple = getRandomLocation()
                          is_true = False
            # check if worm has eaten an apply
            if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
                # don't remove worm's tail segment
                apple = getRandomLocation() # set a new apple somewhere
            else:
                del wormCoords[-1] # remove worm's tail segment
            

            # move the worm by adding a segment in the direction it is moving
            if wormCoords[HEAD]['x'] == CELLWIDTH:
                   wormCoords[HEAD]['x'] = 0

            if wormCoords[HEAD]['x'] == -1:
                   wormCoords[HEAD]['x'] = CELLWIDTH

            if wormCoords[HEAD]['y'] == CELLHEIGHT:
                   wormCoords[HEAD]['y'] = 0

            if wormCoords[HEAD]['y'] == -1:
                   wormCoords[HEAD]['y'] = CELLHEIGHT 
                                        
            if direction == UP:
                newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
            elif direction == DOWN:
                newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
            elif direction == LEFT:
                newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
            elif direction == RIGHT:
                newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
            wormCoords.insert(0, newHead)
            DISPLAYSURF.fill(WHITE)
           
            drawWorm(wormCoords)
            drawApple(apple)
            drawwalls()
            drawScore(len(wormCoords) - 3)
            pygame.display.update()
            FPSCLOCK.tick(FPS)

def drawPressKeyMsg():
     pressKeySurf = BASICFONT.render('Press a key to play.', True, BLACK)
     pressKeyRect = pressKeySurf.get_rect()
     pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
     DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


def checkForKeyPress():
     
     for event1 in pygame.event.get():
       
       if event1.type == pygame.KEYUP:
         
         return True
def showGameOverScreen():
     gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
     gameSurf = gameOverFont.render('Game', True, BLACK)
     overSurf = gameOverFont.render('Over', True, BLACK)
     gameRect = gameSurf.get_rect()
     overRect = overSurf.get_rect()
     gameRect.midtop = (WINDOWWIDTH / 2, 10)
     overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

     DISPLAYSURF.blit(gameSurf, gameRect)
     DISPLAYSURF.blit(overSurf, overRect)
     drawPressKeyMsg()
     pygame.display.update()
     pygame.time.wait(500)
     return
        
   
def showStartScreen():
     snakefont = pygame.font.Font('freesansbold.ttf', 100)
     snakesurf1 = snakefont.render('Wormy', True, BLUE)
     snakesurf2 = snakefont.render('Game!', True, BLUE)
     movx = WINDOWWIDTH / 2
     movy = 50   
     DISPLAYSURF.fill(WHITE)
     snakerect1 = snakesurf1.get_rect()
     snakerect1.topright = (movx,movy)
     DISPLAYSURF.blit(snakesurf1,snakerect1)
     snakerect2 = snakesurf2.get_rect()
     snakerect2.topright = (movx,movy+100)
     DISPLAYSURF.blit(snakesurf2,snakerect2)

     drawPressKeyMsg()         
     movx += 10
     movy = 50
         
     pygame.display.update()
     FPSCLOCK.tick(10)
     si_true = True
     while si_true:
          while Gtk.events_pending():
                Gtk.main_iteration()
          for event in pygame.event.get():
                        
                if event.type == pygame.KEYUP:
                    si_true = False
                    return 

def terminate():
     pygame.quit()
     sys.exit()


def getRandomLocation():
    p = random.randint(0, CELLWIDTH - 1)
    q = random.randint(0, CELLHEIGHT - 1)
    if p in range(12,32) and q == 22:
       p = 5
       q = random.randint(0, CELLHEIGHT - 1)
    if p in range(18,38) and q == 12:
       p = 2
       q = random.randint(0, CELLHEIGHT - 1)
    if p in range(12,44) and q == 6:
       p = 25
       q = random.randint(13, 21)
    if p in range(6,44) and q == 28:
       p = 27
       q = random.randint(13, 19)
    elif p == 6 and q in range(6,28):
       p = 46
       q = random.randint(0, CELLHEIGHT - 1)
    elif p == 12 and q in range(12,22):
       p = 47
       q = random.randint(0, CELLHEIGHT - 1)
    elif p == 38 and q in range(12,22):
       p = 48
       q = random.randint(0, CELLHEIGHT - 1)
    elif p == 44 and q in range(6,22):
       p = 22
       q = random.randint(14, 20)
    else:
        p=p
        q=q
    return {'x': p, 'y': q}



def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, BLACK)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 120, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

def drawwalls():
    wallsrect = pygame.Rect(120, 120, CELLSIZE, 440)
    pygame.draw.rect(DISPLAYSURF, BROWN, wallsrect)

    wallsrecta = pygame.Rect(240, 240, CELLSIZE, 200)
    pygame.draw.rect(DISPLAYSURF, BROWN, wallsrecta)

    wallsrectb = pygame.Rect(120, 560, 760, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, BROWN, wallsrectb) 

    wallsrectc = pygame.Rect(240, 440, 400, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, BROWN, wallsrectc)

    wallsrectc = pygame.Rect(240, 120, 640, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, BROWN, wallsrectc)
    
    wallsrectc = pygame.Rect(880, 120, CELLSIZE, 320)
    pygame.draw.rect(DISPLAYSURF, BROWN, wallsrectc)

    wallsrectc = pygame.Rect(360, 240, 400, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, BROWN, wallsrectc)

    wallsrectc = pygame.Rect(760, 240, CELLSIZE, 200)
    pygame.draw.rect(DISPLAYSURF, BROWN, wallsrectc)
    
def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, GREEN, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 3, y + 3, CELLSIZE -6 , CELLSIZE - 6)
        pygame.draw.rect(DISPLAYSURF, BLUE, wormInnerSegmentRect)


def drawApple(apple):
    x = apple['x'] * CELLSIZE
    y = apple['y'] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, RED, appleRect)



if __name__ == '__main__':
    main()


