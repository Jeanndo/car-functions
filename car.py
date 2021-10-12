MENUE = '''
start - to start the car
stop - to stop the car
quit - to quite the game
'''
started = False
while 1:
    command = input("> ").lower()
    if command == 'help':
        print(MENUE)
    elif command == 'start':
        if started:
            print('Already started')
        else:
            started = True
            print('car has been started enjoy driving')
    elif command == 'stop':
        if not started:
            print('car is already stopped')
        else:
            started = True
            print('the car is now stoped')
    elif command == 'quit':
        print('game exiting')
        break
    else:
        print("I don't understand that ")

