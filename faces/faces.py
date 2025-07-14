def main():

    sen = input().rstrip()

    print(convert(sen))


def convert(sent):

    new_sent = sent.replace(':)','🙂').replace(':(','☹️').replace('\n', '')

    return new_sent

main()

