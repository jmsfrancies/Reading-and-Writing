from graphics import *
import time

# Slide show function


def slide_show(win):
    # slide show dictionary that stores the slides required for the presentation.
    slide_show_dict = {"Disjunctive Syllogism": "P v Q\n~ P\nQ", "Modus Ponens": "P => Q\nP \nQ",
                       "Modus Tollens": "P => Q\n~ Q \n~ P", "Conjunction": "P & Q\nP\nQ",
                       "Material Implication": "~ P v Q\nP => Q", "Hypothectical Syllogism": "P=>Q\nQ=>R\nP=>R",
                       "Dilemma": "P v Q\nP => R\nQ => S\nR v S"}

    # for loop that prints the slides onto the graphics window.
    for i, value in slide_show_dict.items():
        Title = Text(Point(350, 150), i)
        Title.setTextColor("blue")
        Title.setSize(20)
        Body = Text(Point(350, 250), value)
        Body.setTextColor("black")
        Body.setSize(22)
        Title.draw(win)
        Body.draw(win)
        time.sleep(2)
        Title.undraw()
        Body.undraw()


def main():
    # Win object that creates the window and background color.
    win = GraphWin("Logic, Logic, Logic!", 700, 500)
    win.setBackground(color_rgb(200, 200, 200))

    # Segment that is responsible for collecting and storing the first name and last name of the user.
    first_name = Text(Point(200, 200), "Enter Your First Name: ").draw(win)
    last_name = Text(Point(200, 250), "Enter Your Last Name: ").draw(win)
    first_name_inputText = Entry(Point(325, 200), 15)
    last_name_inputText = Entry(Point(325, 250), 15)
    first_name_inputText.setText("")
    last_name_inputText.setText("")
    first_name_inputText.draw(win)
    last_name_inputText.draw(win)

    # Button to prompt the user to click after the user adds his or her name.
    button = Text(Point(250, 300), "Click Anywhere To Start! ")
    button.draw(win)
    win.getMouse()

    # Once the user clicks on the screen, the first name, last name, and the button are undrawn.
    first_name.undraw()
    last_name.undraw()
    first_name_inputText.undraw()
    last_name_inputText.undraw()
    button.undraw()

    # Slogan that describes what the different logic symbols look like and what they mean.
    Slogan = Text(Point(350, 250), """Hello, {0} {1}!
Enjoy Learning some Logic.
The (=>) conditional if then, statement.
The '&' the conjunction, and the 'v'
Disjunction symbol.
ENJOY!""".format(first_name_inputText.getText(), last_name_inputText.getText()))
    Slogan.setTextColor("black")
    Slogan.setSize(22)
    Slogan.draw(win)
    time.sleep(2)
    Slogan.undraw()
    Slogan = Text(Point(350, 150), "Here are a few Logic rules!")
    Slogan.setTextColor("blue")
    Slogan.setSize(28)
    Slogan.draw(win)
    time.sleep(1)
    Slogan.undraw()
    time.sleep(2)
    slide_show(win)
    # Slide Show Function for the presentation
    slide_show(win)


main()
