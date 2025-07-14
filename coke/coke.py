change_counter = 50

while change_counter != 0:

    print("Amount due:", change_counter)

    user_amount = int(input("Insert coin: "))

    if user_amount == 25:

        change_counter -= user_amount

    elif user_amount == 10:

        change_counter -= 10

    elif user_amount == 5:

        change_counter -= 5

    if change_counter < 0:

        abs(change_counter)
        break

print("Change owed:", abs(change_counter))
