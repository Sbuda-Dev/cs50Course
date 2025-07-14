camel_word = input("Enter camelCase variable: ")

snake_list = []

for i, j in enumerate(camel_word):

    if j.isupper() and i > 0:

        snake_list.append('_')
    snake_list.append(j.lower())
snake_word = "".join(snake_list)

print(snake_word)
