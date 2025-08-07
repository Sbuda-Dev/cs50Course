import sys

def main():

    choose = choice()

    first_num = int(input("Enter first number: "))
    sec_num = int(input("Enter second number: "))
    
    if choose == 1:

        print("Addition\n")
        print(add(first_num, sec_num))

    elif choose == 2:

        print("Subtraction\n")
        print(sub(first_num, sec_num))

    elif choose == 3:

        print("Multiplication\n")
        print(mult(first_num, sec_num))

    elif choose == 4:

        print("Division\n")
        print(div(first_num, sec_num))

    else:

        sys.exit("Invalid choice")

def choice():

    try:

        choose = int(input("Choose operation (1 - 4): \n"
        "1. Addition\n"
        "2. Subtraction\n"
        "3. Multiplication\n"
        "4. Division\n\n"))

        return choose

    except ValueError:

        sys.exit("Incorrect value entered.")

def add(x, y):

    try:

        answer = x + y

        return f"{x} + {y} = {answer}"
    
    except ValueError:

        sys.exit("Invalid value entered")

def sub(x, y):

    try:

        answer = x - y

        return f"{x} - {y} = {answer}"
    
    except ValueError:

        sys.exit("Invalid vale entered")

def mult(x, y):

    try:

        answer = x * y

        return f"{x} x {y} = {answer}"
    
    except ValueError:

        sys.exit("Invalid value entered")

def div(x, y):

    try:

        answer = x / y

        return f"{x} / {y} = {answer}"
    
    except ZeroDivisionError:

        sys.exit("Cannot divide by zero")

    except ValueError:

        sys.exit("Invalid value entered")
  

if __name__=="__main__":

    main()