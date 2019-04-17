filename = 'programming_poll.txt'

while True:
    poll = input('Why do you like programming? ')
    if poll == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(poll + '\n')