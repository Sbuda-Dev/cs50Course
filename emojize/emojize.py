import emoji

emo = input("Enter emoji: ")

emoj = emoji.emojize(emo, language="alias")

print(emoj)

