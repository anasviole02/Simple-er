while True:
    command = input('Your command :')
    if command == 'help':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')

    elif command == 'start':
        print('car started .. Ready to go !!')

    elif command == 'stop':
        print('car stopped !!')

    else:
        break