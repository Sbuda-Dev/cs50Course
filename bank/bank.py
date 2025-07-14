greet = input("Greeting: ")

new_greet = greet.strip().capitalize().startswith('H')

hello_greet = greet.strip().capitalize().startswith('Hello')

if new_greet == True and hello_greet == True:

    print("$0")

elif new_greet == True:

    print("$20")

else:

    print("$100")
