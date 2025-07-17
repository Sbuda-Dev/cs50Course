import inflect

p = inflect.engine()

names = []

while True:

    try:

        name = input("Enter name: ")
        names.append(name)

    except EOFError:

        print()
        break

sent = p.join(names)
print(f"Adieu, adieu, to {sent}")