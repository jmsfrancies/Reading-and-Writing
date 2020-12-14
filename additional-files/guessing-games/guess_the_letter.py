from random import randrange
# The guessing game function utilizes the new word to guess variable and usable letters list
# The sentinel loop is a while loop with a conditional parameter, which is checking for the total amount of guesses.



def guessing_game(new_word_to_guess, usable_letters):
    new_word_to_guess.lower()
    total = len(new_word_to_guess) + 5
    guessed_letter_list = ""
    number_of_occurences = 0
    while total > 0:
        guessed_letter = str(
            input("Please enter a letter found within the english alphabet: ")).lower()
        if guessed_letter not in usable_letters:
            print("You've already used the letter {}. Please choose another letter! ".format(
                guessed_letter))
        else:
            if guessed_letter not in new_word_to_guess:
                total -= 1
                usable_letters.remove(guessed_letter)
                print("Guessed letters that are within the word".format(
                    guessed_letter_list))
                print("the letter {} isn't found in the word. \nThe letter that you have guessed has been removed".format(
                    guessed_letter))
                print(usable_letters)
            else:
                total -= 1
                usable_letters.remove(guessed_letter)
                number_of_occurences += new_word_to_guess.count(guessed_letter)
                print("letters that are in the word {}".format(
                    guessed_letter_list))
                for i in new_word_to_guess.lower():
                    if i == guessed_letter:
                        guessed_letter_list += guessed_letter
                        print("letters that are in the word {}".format(
                            guessed_letter_list))
                if number_of_occurences == len(new_word_to_guess):
                    print("The word is {}".format(new_word_to_guess))
                    break
        if total == 0:
            print("Out of guesses!\nthe word was {}".format(new_word_to_guess))

# The main Function stores the guessing word list, usable letters list, and guessing game function call.


def main():
    guessing_word_list = ["hello", "goodbye", "sweet", "chicken",
                          "tasty", "paper", "salad", "motorcycle", "bicycle", "train"]
    rand_int = randrange(1, len(guessing_word_list))
    usable_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                      "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    new_word_to_guess = guessing_word_list.pop(rand_int)
    # print(new_word_to_guess)
    guessing_game(new_word_to_guess, usable_letters)


main()
