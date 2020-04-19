user_input = ''

while user_input != 'quit':
    user_input = input("> ").lower()
    if user_input == 'help':
        print('start - to start the car')
        print('stop - to stop the car')
        print('quit - to exit')
    elif user_input == 'start':
        print('Car started...Ready to go!')
    elif user_input == 'stop':
        print('Car stopped.')
    else:
        print('Did not recognize that command.')
    if user_input == 'quit':
        break









