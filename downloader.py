import requests

print("Welcome to Pastebin downloader!")
print("")
print("Wich Paste Service are you using?")
print("1 - pastebin.com")
print("2 - hastebin.com")
SERVICE = input("Service: ")
print("Please enter your PasteID.")
print("Your PasteID is the code after the / in your Link")
PASTEID = input("PasteID: ")
filename = input("Name of text file (e.g Downloaded pastebin): ")

if SERVICE == "1":
    SERVICEDOMAIN = "https://pastebin.com/raw/" + PASTEID
elif SERVICE == "2":
    SERVICEDOMAIN = "https://hastebin.com/raw/" + PASTEID


r = requests.get(SERVICEDOMAIN)
f = open(f'{filename}.txt', 'a+')
f.write(r.text)
print(f"Text file {filename}.txt has been made!")
