prompt = '\nenter some pizza toppings:'
prompt += "\ntype 'quit' to quit. "


toppings = ''
while toppings != 'quit':
    toppings = input(prompt)

    if toppings != 'quit':
        print("adding topping:", toppings)
