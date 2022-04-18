import pyshorteners
while True:
    link=input("Enter The Link:-")
    shortener=pyshorteners.Shortener()
    shortlink=shortener.tinyurl.short(link)
    print(shortlink)