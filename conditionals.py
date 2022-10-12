# Conditional
# Method evaluate data
# if then else

import random

# ask the user to select the upper bound and ensure it is a valid input
InvalidUpperBound = True # boolean is True or False
while InvalidUpperBound:
    UpperBound = input("What is the upper bound? ")
    # check if upper bound is valid
    if UpperBound.isdigit():
        InvalidUpperBound = False
        print("Upper bound: " + UpperBound)
        UpperBound = int(UpperBound)
    else:
        print("Invalid input")

# generate a random integer between 1 and the upper bound
RandomNumber = random.randint(1, UpperBound)
print("Random number: " + str(RandomNumber))

# start loop here
UserGuess = None
NumberOfGuesses = 1
while UserGuess != RandomNumber:

    # ask the user to guess the number
    UserGuess = input("Type a whole number between 1 and " + str(UpperBound) + ": ")
    # check if guess is a digit
    if UserGuess.isdigit():
        print("Your guess: " + str(UserGuess))
        UserGuess = int(UserGuess)

    # check if user guess is equal to random number
    if UserGuess == RandomNumber:
        print("You guessed correctly!")
        # exit loop here

    # user guess is not equal to random number
    else:
        NumberOfGuesses += 1
        print("Wrong!")

print("Game Over, you took " + str(NumberOfGuesses) + " to guess correctly")

# HighRange = 100
# MidRange = int(HighRange/2)
# LowRange = int(MidRange/2)
# MyGuess = MidRange
# GuessNumber = 0
# HighOrLow = "lower"
# Output = "{} is {} than {}"

# MyRandomNumber = random.randint(1, HighRange)

# print(MyRandomNumber)
# print(MyGuess)


# # evaluate the random number and compare it to the middle number
# MyLowConclusion = "{} is less than {}"
# MyHighConclusion = "{} is greater than {}"

# if MyRandomNumber > MyGuess :
#     HighOrLow = "lower"
#     print(Output.format(MyGuess,HighOrLow,MyRandomNumber))

# if MyRandomNumber < MyGuess :
#     HighOrLow = "higher"
#     print(Output.format(MyGuess,HighOrLow,MyRandomNumber))
