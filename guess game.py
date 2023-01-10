the_guess = 9
limit = 3

i = 1
while i <= limit:
    your_guess = int(input('your guess :'))
    i += 1
    if your_guess == the_guess:
        print(f'Your guess is correct !!')
        break
else:
    print('sorry , you failed !!')