import random

print "Hello!"
name = raw_input("What's your name?")
print "Guess a random integer between 1-100!"

correct_number = random.randint(1,101)
counter = 0

while True:
    g_guess = raw_input("Your guess?")
    try:
        number = float(g_guess)
        if number > 100 or number < 1:
            print "1 AND 100!!!"
        else:
            if number > correct_number:
                print "Your guess is too high, try again."
            elif number < correct_number:
                print "Your guess is too low, try again."
            else:
                print "You did it!"
                counter += 1
                break
    except ValueError:
        print "Guess a REAL number between 1-100!"
    counter += 1

print "Well done! You found my number in %s tries!" % counter
        