months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:

    date = input("Enter date: ")

    try:

        month, day, year = date.split("/")

        if int(month) > 0 and int(month) <= 12 and int(day) > 0 and int(day) <= 31:

            break
        
    except:

        try:

            old_month, old_day, year = date.split(" ")


            for i in range(len(months)):

                if old_month == months[i] and "," in old_day:

                    month = i + 1

                    day = old_day.replace(",", "")


            if int(month) > 0 and int(month) <= 12 and int(day) > 0 and int(day) <= 31:

                break

        except:

            print()
            pass

print(f"{year}-{int(month):02}-{int(day):02}")