plate = input("Enter plate: ")
mid = len(plate) // 2

if plate.isalpha() and (len(plate) <= 6) and (len(plate) >= 2):

    print("Valid")

else:

    if (plate[:2].isalpha()) and (len(plate) <= 6) and (plate[mid - 1].isalpha()) and plate[mid] != '0' and plate[-1].isnumeric() :

        print("Valid")

    else:

        print('Invalid')
