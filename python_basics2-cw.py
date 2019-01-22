import random


def main():
    # problem1()
    # problem2()
    problem3()
    # problem4()


# PROBLEM1
# Create a random number. Print the number.
def problem1():
    import random
    randomNumber = random.randint(0, 9)
    print(randomNumber)


########################################################################################
# PROBLEM2
# Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.
def problem2():
    userInput = input("Put a string: ")
    while (userInput != "q"):
        userInput = input("Put a string: ")
        print(userInput)


########################################################################################
# PROBLEM3
# Create a function that will loop until the user enters '0'.
# Ask the user to enter a positive integer number.
# Print 0 to that number and ask them again to enter a number until they enter '0'.
# Repeat.
def problem3():
    userInput = int(input("Put a positive number: "))
    while (userInput != 0):
        for num in range(0, (userInput + 1)):
            print(num)
        userInput = int(input("Put a number: "))


########################################################################################
# PROBLEM4
# Create a function that creates a random number. Ask the user to guess the random number.
# Keep letting the user guess until they get it right, then quit.
# If they don't get it right, tell them if their next guess has to be higher or lower.
def problem4():
    userInput = int(input("Guess a number: "))

    randomNum = random.randint(0, 5)
    # print(randomNum)
    while (userInput != randomNum):
        if (userInput <= randomNum):
            print(f"{userInput} is not enough. You have to be higher")
            userInput = int(input("Guess a number: "))
        elif (userInput > randomNum):
            print(f"{userInput} is a lot. You have to be lower")
            userInput = int(input("Guess a number: "))

    print(f"{userInput} is correct")


########################################################################################
if __name__ == '__main__':
    main()
