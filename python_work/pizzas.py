pizzas = ['PEPPERONI', 'veGETables', 'Mushrooms']
for pizza in pizzas:
    if pizza.lower() == 'pepperoni':
        print("\n")
        print(f"I really like {pizza.lower()} pizza\n")
    elif pizza.lower() == 'vegetables':
        print(f"My favourite pizza is {pizza.lower()} pizza\n")
    else:
        print(f"The best pizza is {pizza.lower()} pizza\n")
print("Pizza is the best!")

