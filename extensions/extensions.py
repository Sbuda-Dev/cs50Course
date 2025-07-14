fi = input("Enter file name: ").lower().strip()

if fi.endswith('.gif') or fi.endswith('/gif'):

    print("image/gif")

elif fi.endswith('.jpg') or fi.endswith('/jpg'):

    print("image/jpeg")

elif fi.endswith(".jpeg") or fi.endswith('/jpeg'):

    print("image/jpeg")

elif fi.endswith(".pdf") or fi.endswith('/pdf'):

    print("application/pdf")

elif fi.endswith(".png") or fi.endswith('/png'):

    print("image/png")

elif fi.endswith(".txt") or fi.endswith('/txt'):

    print("text/plain")

elif fi.endswith(".zip") or fi.endswith('/zip'):

    print("application/zip")

else:

    print("application/octet-stream")
