from graphics import *
import time


# Disjuncitve Syllogism Slide
def Disjunctive(win, x, y):
    Title = Text(Point(350, 150), "Disjunctive Syllogism")
    Title.setTextColor("blue")
    Title.setSize(20)
    Disjunctive = Text(Point(350, 250), ("""{0} v {1}
~{0},
{1}""".format(x, y)))
    Disjunctive.setTextColor("black")
    Disjunctive.setSize(22)
    Title.draw(win)
    Disjunctive.draw(win)
    time.sleep(2)
    Title.undraw()
    Disjunctive.undraw()

# Modus Ponens Slide


def ModusPonens(win, x, y):
    Title = Text(Point(350, 150), "Modus Ponens")
    Title.setTextColor("blue")
    Title.setSize(20)
    ModusPonens = Text(Point(350, 250), """{0} => {1}
{0}
{1}""".format(x, y))
    ModusPonens.setTextColor("black")
    ModusPonens.setSize(22)
    ModusPonens.draw(win)
    Title.draw(win)
    time.sleep(2)
    Title.undraw()
    ModusPonens.undraw()

# Modus Tollens Slide


def ModusTollens(win, x, y):
    Title = Text(Point(350, 150), "Modus Tollens")
    Title.setTextColor("blue")
    Title.setSize(20)
    ModusTollens = Text(Point(350, 250), """{0} => {1}
~{1}
~{0}""".format(x, y))
    ModusTollens.setTextColor("black")
    ModusTollens.setSize(22)
    Title.draw(win)
    ModusTollens.draw(win)
    time.sleep(2)
    Title.undraw()
    ModusTollens.undraw()

# Conjunction Slide


def Conjunction(win, x, y):
    Title = Text(Point(350, 150), "Conjunction")
    Title.setTextColor("blue")
    Title.setSize(20)
    Conjunction = Text(Point(350, 250), """{0} & {1}
{0}
{1}""".format(x, y))
    Conjunction.setTextColor("black")
    Conjunction.setSize(22)
    Title.draw(win)
    Conjunction.draw(win)
    time.sleep(2)
    Title.undraw()
    Conjunction.undraw()

# Hypothetical Syllogism Slide


def Hypothetical(win, x, y, z):
    Title = Text(Point(350, 150), "Hypothetical Syllogism")
    Title.setTextColor("blue")
    Title.setSize(20)
    Hypothetical = Text(Point(350, 250), """{0} => {1}
{1} => {2}
{0} => {2}""".format(x, y, z))
    Hypothetical.setTextColor("black")
    Hypothetical.setSize(22)
    Title.draw(win)
    Hypothetical.draw(win)
    time.sleep(2)
    Title.undraw()
    Hypothetical.undraw()

# Material Implication Syllogism Slide


def Material_Implication(win, x, y):
    Title = Text(Point(350, 150), "Material Implication")
    Title.setTextColor("blue")
    Title.setSize(20)
    Material = Text(Point(350, 250), """(~{0} v {1})
({0} => {1})""".format(x, y))
    Material.setTextColor("black")
    Material.setSize(22)
    Title.draw(win)
    Material.draw(win)
    time.sleep(2)
    Title.undraw()
    Material.undraw()
    Title = Text(Point(350, 150), "Dilemma")
    Title.setTextColor("blue")
    Title.setSize(20)

# Dilemma Slide


def Dilemma(win, x, y, z, a):
    Title = Text(Point(350, 150), "Dilemma")
    Title.setTextColor("blue")
    Title.setSize(20)
    Dilemma = Text(Point(350, 250), """{0} v {1}
{0} => {2}
{1} => {3}
{2} v {3}
""".format(x, y, z, a))
    Dilemma.setTextColor("black")
    Dilemma.setSize(22)
    Title.draw(win)
    Dilemma.draw(win)
    time.sleep(2)
    Title.undraw()
    Dilemma.undraw()
    Title = Title = Text(
        Point(350, 150), "Enjoy having a logic filled life! ")
    Title.setTextColor("blue")
    Title.setSize(30)
    Title.draw(win)
    time.sleep(2)
    win.close()


def main():
    # Logic Variables for the logic slides powerpoint
    x = "A"
    y = "B"
    z = "C"
    a = "D"

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

    # Listed out functions for each slide utilized for the presentation
    Disjunctive(win, x, y)
    ModusPonens(win, x, y)
    ModusTollens(win, x, y)
    Hypothetical(win, x, y, z)
    Conjunction(win, x, y)
    Material_Implication(win, x, y)
    Dilemma(win, x, y, z, a)


main()
