answer = input("What is the answer to the great question of life, the universe and everything? ")

if answer.strip() == '42':

    print("Yes")

elif answer.lower() == 'forty-two':

    print('Yes')

elif answer.title() == 'Forty Two':

    print('Yes')

else:

    print('No')
