from graphics import *
from random import randint

class Snake:
    def __init__(self, squareSize, winSize, color, aColor):
        self.squareSize = squareSize
        self.winSize = winSize
        self.color = color
        self.appleColor = aColor
        self.snake = []
        self.x = int(self.winSize/2)-int(self.squareSize/2)
        self.y = int(self.winSize/2)-int(self.squareSize/2)
        self.posArrX = [self.x]
        self.posArrY = [self.y]
        self.apple = None
        self.appleX = None
        self.appleY = None
        self.dir = 1

        self.generateApple()

    def update(self, key, window):
        if key == "W" or key == "w":
            if self.dir != 3:
                self.dir = 1

        elif key == "A" or key == "a":
            if self.dir != 4:
                self.dir = 2

        elif key == "S" or key == "s":
            if self.dir != 1:
                self.dir = 3

        elif key == "D" or key == "d":
            if self.dir != 2:
                self.dir = 4


        if self.posArrX[0] == self.appleX and self.posArrY[0] == self.appleY:
            self.generateApple()
            self.ate = True
        else:
            self.ate = False


        if self.dir == 1:
            if self.ate:
                self.posArrX.insert(0, self.posArrX[0])
                self.posArrY.insert(0, self.posArrY[0]-1*self.squareSize)
            else:
                self.posArrX.insert(0, self.posArrX[0])
                self.posArrY.insert(0, self.posArrY[0]-1*self.squareSize)
                self.posArrX.pop()
                self.posArrY.pop()
        elif self.dir == 2:
            if self.ate:
                self.posArrX.insert(0, self.posArrX[0]-1*self.squareSize)
                self.posArrY.insert(0, self.posArrY[0])
            else:
                self.posArrX.insert(0, self.posArrX[0]-1*self.squareSize)
                self.posArrY.insert(0, self.posArrY[0])
                self.posArrX.pop()
                self.posArrY.pop()
        elif self.dir == 3:
            if self.ate:
                self.posArrX.insert(0, self.posArrX[0])
                self.posArrY.insert(0, self.posArrY[0]+1*self.squareSize)
            else:
                self.posArrX.insert(0, self.posArrX[0])
                self.posArrY.insert(0, self.posArrY[0]+1*self.squareSize)
                self.posArrX.pop()
                self.posArrY.pop()
        else:
            if self.ate:
                self.posArrX.insert(0, self.posArrX[0]+1*self.squareSize)
                self.posArrY.insert(0, self.posArrY[0])
            else:
                self.posArrX.insert(0, self.posArrX[0]+1*self.squareSize)
                self.posArrY.insert(0, self.posArrY[0])
                self.posArrX.pop()
                self.posArrY.pop()


        if self.posArrX[0] < 0 or self.posArrY[0] < 0 or self.posArrX[0] > 400 or self.posArrY[0] > 400:
            return False

        for self.index in range(1, len(self.posArrX)):
            if self.posArrX[self.index] == self.posArrX[0] and self.posArrY[self.index] == self.posArrY[0]:
                return False

        for self.part in self.snake:
            self.part.undraw()

        self.apple.undraw()

        return True


    def draw(self, window):
        for self.part in range(len(self.posArrX)):
            self.part = Rectangle(Point(self.posArrX[self.part], self.posArrY[self.part]), Point(self.posArrX[self.part]+self.squareSize, self.posArrY[self.part]+self.squareSize))
            self.part.setFill(self.color)
            self.part.setWidth(0)
            self.part.draw(window)
            self.snake.append(self.part)

        self.apple = Rectangle(Point(self.appleX, self.appleY), Point(self.appleX+self.squareSize, self.appleY+self.squareSize))
        self.apple.setFill(self.appleColor)
        self.apple.setWidth(0)
        self.apple.draw(window)

    def generateApple(self):
        self.appleX = randint(0, int(self.winSize/self.squareSize))*self.squareSize
        self.appleY = randint(0, int(self.winSize/self.squareSize))*self.squareSize

        while self.appleX == 420 or self.appleY == 420:
            self.appleX = randint(0, int(self.winSize/self.squareSize))*self.squareSize
            self.appleY = randint(0, int(self.winSize/self.squareSize))*self.squareSize


backgroundColor = color_rgb(52, 56, 99)
appleColor = color_rgb(255, 0, 0)
playerColor = color_rgb(33, 255, 0)

win = GraphWin("Snake", 420, 420, autoflush=False)
win.setBackground(backgroundColor)
snake = Snake(20, 420, playerColor, appleColor)


while True:
    snake.draw(win)

    key = win.checkKey()
    if key == "Escape":
        break

    if snake.update(key, win):
        update(10)
    else:
        break

win.close()
