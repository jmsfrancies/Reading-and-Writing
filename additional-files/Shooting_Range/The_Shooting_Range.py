# You are welcome to write and include any other Python files you want or need
# however your game must be started by calling the main function in this file.
from graphics import *
import sys
import os
import time
from playsound import playsound

def Ready(win, title):
    # for loop to print each target ring onto the graphics window
    total = 0
    target_color = ["Blue", "Green", "Yellow", "Orange", "Red"]
    for i in reversed(range(30, 171, 35)):
        Target = Circle(Point(250, 250), i)
        #Target.setfill is formatted to be one of the five colors on the target color list
        Target.setFill("{0}".format(target_color[total]))
        Target.draw(win)
        total = total + 1

    # Where the gunshots display
    for i in range(8):
        BulletHole = win.getMouse()
        #Replace the pathname with the github pathname
        playsound('/Users/jamesboonfrancies/Desktop/Reading-And-Writing/Reading-and-Writing/additional-files/Shooting_Range/9mmShot.mp3')
        x = BulletHole.getX()
        y = BulletHole.getY()
        BulletHole = Circle(Point(x, y), 2.5)
        BulletHole.setFill("black")
        BulletHole.setOutline("white")
        BulletHole.draw(win)


    title.setText("Great Shooting! Please Come Again!")
    win.getMouse()
    win.getMouse()
    win.close()

# Main Function that houses the graphics window and Ready function call
def main():
    win = GraphWin("The Shooting Range", 500, 500)
    win.setBackground("white")
    title = Text(Point(250, 25), """Welcome to The Handgun Shooting Range!
Where Precision and accuracy get further refined!""")
    title.setSize(20)
    title.setStyle("bold italic")
    title.draw(win)
    win.getMouse()
    Ready(win, title)


main()
