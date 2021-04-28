command =''
started = False
print ('You enter your car')
print ('type "help" for instructions')
while True:
    command = input('>').lower()
    if command == 'start':
        if started:
            print ('Car is already running')
        else:
            started = True
            print('Car started......')
    elif command == 'stop':
        if not started:
            print ('Already stopped')
        else:
            started = False
            print ('Car stopped.')
    elif command == ('move'):
        if not started:
            print ('car is not running')
        else:
            print ('car has moved')
    elif command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to quit
        ''')
    elif command == 'quit':
        break
    else:
        print('Invalid Input')
