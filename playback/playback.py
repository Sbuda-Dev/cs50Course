def main ():

    sent = input("Enter sentence: ")
    print(replace_space(sent))

def replace_space(sent):

    new_sent = sent.replace(" ", "...")
    return new_sent


main()
