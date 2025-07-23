def main():
    
    plate = input("Enter plate: ")
    is_valid(plate)


def is_valid(s):
    
    mid = len(s) // 2

    if s.isalpha() and (len(s) <= 6) and (len(s) >= 2):

        print("Valid")

    else:

        if (s[:2].isalpha()) and (len(s) <= 6) and (s[mid - 1].isalpha()) and s[mid] != '0' and s[-1].isnumeric() :

            print("Valid")

        else:

            print('Invalid')

if __name__ == "__main__":
    main()
