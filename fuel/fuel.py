while True:

    try:

        fraction = input("Fractions: ")

        numer, denom = fraction.split("/")

        perc = round(((int(numer) / int(denom)) * 100), 0)
        int_perc = int(perc)
        sign = '%'

        if '-' not in fraction and int_perc >= 0 and int_perc <= 100:

            if int(numer) == 0 or int_perc <= 1:

                print('E')
                break

            elif perc >= 99:

                print('F')
                break

            else:

                print(str(int_perc) + sign.strip())
                break

    except ZeroDivisionError:

        print("Error, cannot divide by zero")

    except ValueError:

        print("Invalid values entered")

