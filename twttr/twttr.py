def main():

    word = input("Enter word: ")
    
    print(shorten(word))


def shorten(word):

    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'U', 'u']

    word_list = []

    for i in word:

        if i not in vowels:

            word_list.append(i)

    new_word = "".join(word_list).rstrip()

    return new_word


if __name__ == "__main__":
    main()