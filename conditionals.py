# Conditional
# Method evaluate data
# if then else

import random

# ask the user to select the upper bound
UpperBound = input("What is the upper bound? ")
print("Upper bound: " + UpperBound)
UpperBound = int(UpperBound)

# generate a random integer between 1 and the upper bound
RandomNumber = random.randint(1, UpperBound)
print("Random number: " + str(RandomNumber))

# ask the user to guess the number
UserGuess = input("Type a whole number between 1 and " + str(UpperBound) + ": ")
print("Your guess: " + str(UserGuess))

# check if user guess is equal to random number
if int(UserGuess) == RandomNumber:
    print("You guessed correctly!")

# user guess is not equal to random number
else:
    print("Wrong!")

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
