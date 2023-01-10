year = int(input("Enter the year :"))

if year % 4 == 0 and year % 400 == 0:
    print(year,'is a Leap year')
elif year % 4 == 0 and year % 100 != 0:
    print((year ,'is a leap year'))
else:
    print('common year or not a leap year')