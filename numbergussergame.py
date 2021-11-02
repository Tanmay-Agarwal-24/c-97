import random
print("Number Guessing Game")
print("Guesss a number between(1 and 9)")
number = random.randint(1, 9)
chance=0
while chance < 5:
    guess = int(input('Guess A Number:- '))
    chance += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break

if guess == number:
    print('You guessed the number in ' + str(chance) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))