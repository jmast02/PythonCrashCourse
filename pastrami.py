sandwich_orders = ['turkey', 'blt', 'ham', 'meatball', 'philly', 'pastrami', 'pastrami', 'pastrami']

print('Oh no we ran out of pastrami.')

#lets remove all pastrami's
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


finished_sandwiches = []

#while sandwhich_orders still has a sandwich in it.
while sandwich_orders:

    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"Your {current_sandwich} is complete!")


#iterate through the finished sandwiches.
for sandwich in finished_sandwiches:
    print(f"Completed subs: {sandwich}")


