fruit = {'Apple': 130, 'Avocado': 50, 'Sweet Cherries': 100, 'Kiwifruit': 90, 'Pear': 100}

user_fruit = input("Item: ").title()

for i in fruit:

    if i == user_fruit:

        print("Calories: ",fruit[i])
