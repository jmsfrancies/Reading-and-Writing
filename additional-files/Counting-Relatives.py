# This is the functions practice file that enquires on first name and how many relatives

# hello function that prints the formatted string hello fname
# and fname is inherited from the main function. Example (Hello James)
def hello(fname):
    print("Hello {}".format(fname))


# How many function inherits the relatives value from the main function
# then proceeds to compare the relatives value to the relatives dictionary key
# if the relatives value is equivalent to one of the dictionary values, then the
# formatted string after the for loop is printed out.
def howmany(relatives):
    relatives_dict = {1: "One", 2: "Two", 3: "Three", 4: "Four",
                      5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
                      9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve",
                      13: "Thriteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
                      17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty"}
    for i, value in relatives_dict.items():
        if relatives is i:
            print("{} Relatives?".format(value))


# The main function houses the fname value and relatives value
# The hello(fname) and howmany(relatives) function calls are also
# stored with the main function
def main():
    fname = str(input("What is your first name? "))
    relatives = int(input("How man relatives do you have? "))

    hello(fname)
    howmany(relatives)


main()
