# For loop to iterate over string x!
# if there is a vowel within string x, then the total vowels will increment by one.
import pyttsx3
import os
# Vowel Count that can be read and heard.
def count_with_subtitles(x, total):
    engine = pyttsx3.init()
    for i in x:
        if i in ['a', 'e', 'i', 'o', 'u']:
            total += 1
            print("letter %s vowel #%d" % (i, total))
            engine.say("letter %s vowel #%d" % (i, total))

    engine.runAndWait()
    
# Vowel Count for the visually impaired
def Visually_Impaired(x, total):
    engine = pyttsx3.init()
    for i in x:
        if i in ['a', 'e', 'i', 'o', 'u']:
            total += 1
            engine.say("letter %s vowel #%d" % (i, total))

    engine.runAndWait()


# main function that stores the vowel count
def main():
    x = str(input("Please enter a statement with vowels in which you would like to have the total vowels counted: ").lower())
    y = int(input("Enter 1 for heaing impaired and 2 to read the countdown, and 3 for the hearing and reading version: "))
    total = 0
    while True:
        if y in [1,2,3]:
            if y == 1:
                Visually_Impaired(x, total)
                break
            if y == 2:
                for i in x:
                    if i in ['a', 'e', 'i', 'o', 'u']:
                        total += 1
                        print("letter %s vowel #%d" % (i, total))
                break
            if y == 3:
                count_with_subtitles(x, total)
                break
        else:
            y = int(input("Enter 1 for heaing impaired and 2 to read the countdown, and 3 for the hearing and reading version: "))
            continue
main()
