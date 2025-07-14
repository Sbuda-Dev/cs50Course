eq = input("Enter equation: ")

new = eq.split()

first_num = new[0]
second_num = new[2]

if '+' in eq:

    ans = int(first_num) + int(second_num)

    print(float(ans))

elif '-' in eq:

    ans = int(first_num) - int(second_num)

    print(float(ans))

elif '*' in eq:

    ans = int(first_num) * int(second_num)

    print(float(ans))

elif '/' in eq:

    ans = int(first_num) / int(second_num)

    print(ans)
