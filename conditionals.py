# Conditional
# Method evaluate data
# if then else

import random

HighRange = 100
MidRange = int(HighRange/2)
LowRange = int(MidRange/2)
MyGuess = MidRange
GuessNumber = 0
HighOrLow = "lower"
Output = "{} is {} than {}"

MyRandomNumber = random.randint(1, HighRange)

print(MyRandomNumber)
print(MyGuess)


# evaluate the random number and compare it to the middle number
MyLowConclusion = "{} is less than {}"
MyHighConclusion = "{} is greater than {}"

if MyRandomNumber > MyGuess :
    HighOrLow = "lower"
    print(Output.format(MyGuess,HighOrLow,MyRandomNumber))

if MyRandomNumber < MyGuess :
    HighOrLow = "higher"
    print(Output.format(MyGuess,HighOrLow,MyRandomNumber))
