sandwich_orders = ['turkey', 'blt', 'ham', 'meatball', 'philly']


# create empty list to store finished sandwiches
finished_sandwiches = []

#while sandwhich_orders still has a sandwich in it.
while sandwich_orders:

    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"Your {current_sandwich} is complete!")


#iterate through the finished sandwiches.
for sandwich in finished_sandwiches:
    print(f"\nCompleted subs: {sandwich}")