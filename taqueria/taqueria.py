menu = {

    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

meal_count = 0

while True:

    try:

        order = input("Item: ").title()
        meal_count += menu[order]
        price = format(meal_count, '.2f')
        print('$' + str(price))

    except EOFError:

        break

    except Exception:

        continue
