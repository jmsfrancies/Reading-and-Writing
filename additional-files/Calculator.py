# numbers class that stores two numbers : number one and number two.
class Numbers():
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    # constructor that adds the numbers from the Numbers class.
    def add_numbers(self):
        addition = self.number_1 + self.number_2
        return "{0}+{1}={2}".format(self.number_1, self.number_2, addition)

    # constructor that subtracts the number with the lowest value from the highest value.
    def subtract_numbers(self):
        if self.number_1 >= self.number_2:
            subtraction = self.number_1 - self.number_2
            return "{0}-{1}={2}".format(self.number_1, self.number_2, subtraction)
        else:
            subtraction = self.number_2 - self.number_1
            return "{0}-{1}={2}".format(self.number_2, self.number_1, subtraction)

    # constructor that multiplies the numbers in the given set.
    def multiply_numbers(self):
        multiply = self.number_1 * self.number_2
        return "{0}*{1}={2}".format(self.number_1, self.number_2, multiply)

    # constructor that divides the largest number by the smallest number and rounds the answer by two decimal places.
    def divide_numbers(self):
        if self.number_1 >= self.number_2:
            division = round((self.number_1/self.number_2), 2)
            return "{0}/{1}={2}".format(self.number_1, self.number_2, division)
        else:
            division = round((self.number_2/self.number_1), 2)
            return "{0}/{1}={2}".format(self.number_2, self.number_1, division)

    # constructor that multiplies the first number to the power of the second number (exponentially).
    def exponential_numbers(self):
        exponential = self.number_1 ** self.number_2
        return "{0} to the power of {1} is: {2:,} ".format(self.number_1, self.number_2, exponential)


def main():
    x = int(input("Please enter a number greater than or equal to 1: "))
    y = int(input("Please enter a number greater than or equal to 1: "))
    question = int(input(
        "Would you like to subtract (1), multiply (2), divide (3), exponentential(4), or add (5):"))
    number_set = Numbers(x, y)
    if question == 5:
        print(number_set.add_numbers())
    elif question == 1:
        print(number_set.subtract_numbers())
    elif question == 2:
        print(number_set.multiply_numbers())
    elif question == 3:
        print(number_set.divide_numbers())
    elif question == 4:
        print(number_set.exponential_numbers())


main()
