def main():
    
    greet = input("Greeting: ")
    value(greet)


def value(greeting):

    new_greet = greeting.strip().capitalize().startswith('H')

    hello_greet = greeting.strip().capitalize().startswith('Hello')

    if new_greet == True and hello_greet == True:

        print("$0")

    elif new_greet == True:

        print("$20")

    else:

        print("$100")
        
if __name__ == "__main__":
    main()