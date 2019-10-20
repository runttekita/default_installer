import requests
import zipfile
import os
import shutil


id = ""
name = ""
dir = "."
steam = ""
author = ""
desc = ""


def take_data():
    print("Mod ID (no spaces):")
    global id
    id = input()
    if " " in id:
        print("No spaces in ID allowed!")
        take_data()
        return
    print("Mod Name:")
    global name
    name = input()
    print("Steam Directory:")
    global steam
    steam = input()
    print("Author Name:")
    global author
    author = input()
    print("Description")
    global desc
    desc = input()
    print("Downloading the Default...")


take_data()

default = requests.get(
    "https://github.com/Gremious/StS-DefaultModBase/archive/master.zip"
)

with open(f"{dir}default.zip", "wb") as f:
    f.write(default.content)

print("Extracting the Default...")
with zipfile.ZipFile(f"{dir}default.zip", "r") as zip:
    zip.extractall(dir)

print("Refactoring the Default")

os.remove(f"{dir}default.zip")
shutil.move("./StS-DefaultModBase-master/theDefault", ".")
shutil.rmtree("./StS-DefaultModBase-master")

print("Renaming folders")
os.rename("./theDefault", f"./{id}")
print("Renamed main folder")
os.rename(f"./{id}/src/main/java/theDefault", f"./{id}/src/main/java/{id}")
print("Renamed src folder")
os.rename(
    f"./{id}/src/main/resources/theDefaultResources",
    f"./{id}/src/main/resources/{id}Resources",
)
print("Renamed resource folder")


print("Refactored folder names")
