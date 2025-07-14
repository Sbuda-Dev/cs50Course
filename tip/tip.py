def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):

    removed = d.removeprefix('$')

    return float(removed)

def percent_to_float(p):

    removed = p.removesuffix('%')

    percent = float(removed) / 100

    return percent

main()
