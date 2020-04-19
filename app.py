user_input = ''
started = False

while True:
    user_input = input("> ").lower()
    if user_input == 'help':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif user_input == 'start':
        if started:
            print('Car is already started!')
        else:
            print('Car started...Ready to go!')
            started = True
    elif user_input == 'stop':
        if not started:
            print('Car is already stopped!')
        else:
            print('Car stopped.')
            started = False
    elif user_input == 'quit':
        break
    else:
        print('Did not recognize that command.')









