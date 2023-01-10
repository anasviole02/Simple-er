import random as ran
number = ran.randint(1,10)
for i in range(3):
    user = int(input('Enter your guess :'))
    if user == number:
        print('hurray !! , you guessed it right ...')
        break
    elif user < number:
        print('Entered numbered is lower ..')
    elif user > number:
        print('Entered numbered is higher ..')
else:
    print('Out of turns , better luck next time !!')