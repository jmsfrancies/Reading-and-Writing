from random import randrange

# This is the guess the number game program
# You must guess between one and thirty 
# if you don't, then that guess will not count 
# and you will be asked once again. Otherwise, 
# the program will tell you if you guessed 
# too high or too low!

def main():
    x = randrange(1,31)
    #print(x)
    y = int(input("Please guess a number between 1 to 30: "))
    total = 0
    while total < 5:
        if y < 1 or y > 30:
            y = int(input("Please guess a number between 1 to 30: "))
        else:
            if x == y:
                print("Correct! you've guessed the correct number: {}".format(x))
                break
            elif x > y:
                print("You must guess higher to find the correct number")
                total = total + 1
                y = int(input("Please guess a number between 1 to 30: "))
            else:
                print("You must guess lower than your previous number")
                total = total + 1
                y = int(input("Please guess a number between 1 to 30: "))
                 
        
main()        