a = int(input("Enter the number: "))
i = 1
while i <= 10:
    print(a, "*", i, "=", a * i)
    i += 1


# while loop with else
x = 1
while x < 3:
    print(x)
    x += 1
else:
    print("limit crossed")


# guessing game
import random

jackpot = random.randint(1, 100)
count = 1
while 1:
    guess = int(input("Enter a number between 1 and 100:"))
    if guess == jackpot:
        print("You guessed a correct number")
        break
    elif guess > jackpot:
        print("Wrong guess! Guess lower")
    else:
        print("Wrong guess! Guess higher")
    count += 1
print("Total number of attempts:", count)
