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
    for y in range(5):
        y = int(input("Please guess a number between 1 to 30: "))
        if y >= 1 and y <= 30:
            if x == y:
                print("Correct! you've guessed the correct number: {}".format(x))
                break
            elif x > y:
                print("You must guess higher to find the correct number")
            else:
                print("You must guess lower than your previous number")
        else:
            print("Please enter a number between 1 and 30 ")
            break
    print("The correct answer is: %d"%(x))
main()        