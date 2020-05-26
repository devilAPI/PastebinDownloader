import requests

print("Welcome to Pastebin downloader!")
print("")
url = input("Url: ")
filename = input("Name of text file (e.g Downloaded pastebin): ")

r = requests.get(pastebin_url)
f = open(f'{filename}.txt', 'a+')
f.write(r.text)
print(f"Text file {filename}.txt has been made!")
