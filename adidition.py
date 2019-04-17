print('type quit to quit.')

while True:
    try:
        x = input('Number 1 = ')

        if x.lower() == 'quit':
            break
        x = int(x)

        y = input('Number 2 = ')

        if y.lower() == 'quit':
            break
        y = int(y)

    except ValueError:
        print('That is not a number')
    else:
        print(x + y)