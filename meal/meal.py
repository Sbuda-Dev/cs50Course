def main():

    time = input("What is the time? ")

    converted = convert(time)

    if converted >= 7 and converted <= 8:

        print("Breakfast time")

    elif converted >= 12 and converted <= 13:

        print("Lunch time")

    elif converted >= 18 and converted <= 19:

        print("Dinner time")

def convert(time):

    hours, minutes = time.split(":")

    hours = int(hours)
    minutes = int(minutes)

    new_time = hours + (minutes/60)

    return float(new_time)

if __name__ == "__main__":
    main()
