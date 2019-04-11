prompt =('How old are you?\nType 0 to leave: ' )


# only 3 tickets left to movie
tickets_left = 3

age = ' '
while tickets_left > 0:
    age = int(input(prompt))

    if age == 0:
        break
    elif age <= 3:
        print('freeeeee')
    elif age > 3 and age <= 12:
        print('That will be 10 bucks.')
    else:
        print('That will be 12 bucks')

# subtract a ticket each time one is sold
    tickets_left -= 1

print('Have a great day')

