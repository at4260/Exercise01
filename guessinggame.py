import random

print "Hello!"
name = raw_input("What's your name?")
print "Guess a random number between 1-100!"

correct_number = random.randint(1,101)

while True:
    number = input("Your guess?")
    if number > correct_number:
        print "Your guess is too high, try again."
    elif number < correct_number:
        print "Your guess is too low, try again."
    else:
        print "You did it!"
        break