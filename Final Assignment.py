# Program

# find way to load in images using player input
# add a jump/slide
# add hitboxs and game overs
# space out obstacles
# add lines onthe road
# add high scores

# add clock.tick()

import pygame
import time
import random

pygame.init()
ScreenWidth = 700
ScreenHeight = 900

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREY = (131,139,139)
WHITE = (255, 255, 255)

menuFont = pygame.font.Font('ARCADECLASSIC.ttf', 30)
titleFont = pygame.font.Font('ARCADECLASSIC.ttf', 65)

class character:

    def __init__(self, name):

        self.name = name
        self.x = (ScreenWidth / 2) - 50

    def loadFrames(self):
        self.animationState = 2
        self.Jump = '/Users/williamhaines/Desktop/Python Codes/Grade 12/Final Assignment/Jump' + self.name + '.png'
        self.Slide = '/Users/williamhaines/Desktop/Python Codes/Grade 12/Final Assignment/Slide' + self.name + '.png'

    # called to pass as the picture that will be displayed. Changes the image every call
    def animate(self):
        self.Frame = '/Users/williamhaines/Desktop/Python Codes/Grade 12/Final Assignment/Frame' + str(self.animationState // 2) + self.name + '.png'
        if self.animationState == 7:
            self.animationState = 2
        else:
            self.animationState += 1
        return self.Frame

    def move(self, direction):
        if direction == 1 and self.x > 67:
            self.x -= ScreenWidth / 3
        elif direction == 2 and self.x < 532:
            self.x += ScreenWidth / 3

    def changeCharacter(playerSelected):
        # change the name here which will change the images displayed after loading images
        pass


class obstacles:

    def __init__(self, lane):
        self.y = 0
        self.move = 5

        if lane == 1:
            self.x = (ScreenWidth / 6) - 50
        elif lane == 2:
            self.x = (ScreenWidth / 2) - 50
        else:
            self.x = (ScreenWidth * (5/6)) - 50
            
        num = random.randrange(1, 3)
        if num == 1:
            self.obPic = pygame.image.load('C:\Users\willh\OneDrive\Desktop\Python Files\Subway Surfers Game\Images\Car.png')
            self.obPic = pygame.transform.scale(self.obPic, (100, 100))
        else:
            self.obPic = pygame.image.load('\Users\willh\OneDrive\Desktop\Python Files\Subway Surfers Game\Images\Gate.png')
            self.obPic = pygame.transform.scale(self.obPic, (100, 100))

    def moveScreen(self):
        self.y += self.move

    def increaseDifficulty(self):
        self.move += 1


# Will draw everything on the screen once the hwile loop has restarted
def redraw_game_window():   # Redraws the screen
    global obCount
    win.fill(BLACK)
    # specify which screen we are on and draw specific points
    if windowNum == 0:
        drawMenu()
        drawMenuButtons()
    elif windowNum == 1:
        countdown()
    elif windowNum == 2:
        mainGame(player, policeCar)
    elif windowNum == 3:
        pass
    elif windowNum == 4:
        draw_instructions()
    
    pygame.display.update()    

#---------------------#
# main menu functions #
#---------------------#

# Draws the menu screen(pulls from: drawMenuButtons())    
def drawMenu():
    menuScreen = titleFont.render('Car Chase', True, BLUE)              # how to center text on the screen
    x = (ScreenWidth / 2) - (menuScreen.get_width() / 2)                # Coordinates for the title
    y = (ScreenHeight / 2) - (menuScreen.get_height() / 2) - 180        # Coordinates for the title
    win.blit(menuScreen, (x, y))

# Draws the menu Buttons
def drawMenuButtons():
    for p in [[(143,400,190,80),'START GAME'], [(377,400,190,80),'SELECT SKIN'], [(255, 500, 190, 80), 'HOW TO PLAY']]: # Coordintes are (wherex, wherey, width, hight)
        pygame.draw.rect(win, GREY, p[0], 0)
        pygame.draw.rect(win, BLUE, p[0], 3)
        txtSurface = menuFont.render(p[1], True, WHITE)
        x = p[0][0] + (p[0][2] - txtSurface.get_width()) // 2    # gets the coordinates of the writing on the buttons
        y = p[0][1] + (p[0][3] - txtSurface.get_height()) // 2   # gets the coordinates of the writing on the buttons
        win.blit(txtSurface,(x,y))

# Funtion controls button functionality on the menu screen
def menuButtonPressed():
    clickPos = pygame.mouse.get_pos()
    if 143 < clickPos[0] < 333 and 400 < clickPos[1] < 480:
        return 1
    elif 377 < clickPos[0] < 567 and 400 < clickPos[1] < 480:
        return 3
    elif 255 < clickPos[0] < 445 and 500 < clickPos[1] < 580:
        return 4
    else:
        return 'error'

#----------------------------#
# Countdown Window Functions #
#----------------------------#

def countdown():
    global windowNum

    for i in range(3, 0, -1):
        countScreen = titleFont.render(str(i), True, WHITE)
        x = (ScreenWidth / 2) - (countScreen.get_width() / 2)
        y = (ScreenHeight / 2) - (countScreen.get_height() / 2)
        win.blit(countScreen, (x, y))
        pygame.display.update()
        pygame.time.delay(1000)
        win.fill(BLACK)        
    windowNum = 2

#-----------------------#
# Game Screen Functions #
#-----------------------#

# Displays the stationary portions of the game
def mainGame(player, enemy):
    playerImage = pygame.image.load(player.animate())
    playerImage = pygame.transform.scale(playerImage, (100, 100))
    x = ScreenWidth // 2 - 50
    win.blit(playerImage, (player.x, 600))

# Displays the mobile parts of the game
def Obstacles():
    
    for index, i in enumerate(obstacleTracker):
        win.blit(i.obPic, (i.x, i.y))
        i.moveScreen()
        if i.y >= 900:
            obstacleTracker.pop(index)
    
#------------------------#
# Skin Selector Functios #
#------------------------#


#---------------------#
# Help Page Functions #
#---------------------#

def draw_instructions():
    instructions = menuFont.render('put instructions here', True, WHITE)
    x = (ScreenWidth / 2) - (instructions.get_width() / 2)
    y = (ScreenHeight / 2) - (instructions.get_height() / 2) - 180
    win.blit(instructions, (x, y))

#--------------------------#
# Input Handling Functions #
#--------------------------#


# windowNum = 0
def TitleScreen():
    global stop
    global windowNum
    for event in pygame.event.get():
        if event.type == pygame.QUIT:              # if user clicks on the window's 'X' button
                stop = False
        elif event.type == pygame.MOUSEBUTTONDOWN: # is user presses mouse button
            if menuButtonPressed() != 'error':
                windowNum = menuButtonPressed()

# windowNum = 2
def GameScreen(player):
    global stop
    global windowNum
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move(1)
            elif event.key == pygame.K_RIGHT:
                player.move(2)
            else:
                pass

# windowNum = 3
def SkinSelect():
    global stop
    global windowNum
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = False

# windowNum = 4
def HelpScreen():
    global stop
    global windowNum
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                windowNum = 0

# Game starts here
win = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption('Car Crash Game')
windowNum = 0
player = character('Pedro')
player.loadFrames()
policeCar = character('Wilfred')
obstacleTracker = []
clock = pygame.time.Clock()

# window number guide:
# 0 = title screen
# 1 = countdown
# 2 = game screen
# 3 = skin selector
# 4 = help screen

stop = True

while stop:
    redraw_game_window()
    clock.tick(60)

    if windowNum == 0:
        TitleScreen()
    elif windowNum == 2:
        GameScreen(player)
    elif windowNum == 3:
        SkinSelect()
    elif windowNum == 4:
        HelpScreen()

pygame.quit()






        
