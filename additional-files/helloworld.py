from colorama import Fore,Style,Back
def main():
    space = " "
    for i in "HelloWorld!":
        print(Back.GREEN)
        print(Style.BRIGHT + Fore.RED + "{0}{1}".format(space,i))
        space = space + " "
    print(Style.RESET_ALL)
main()