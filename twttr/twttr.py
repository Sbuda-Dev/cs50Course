vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'U', 'u']

word_list = []

word = input("Enter word: ")

for i in word:

    if i not in vowels:

        word_list.append(i)

new_word = "".join(word_list).rstrip()
print(new_word)
