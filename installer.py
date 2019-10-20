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
    global id, name, steam, author, desc
    id = input()
    if " " in id:
        print("No spaces in ID allowed!")
        take_data()
        return
    print("Mod Name:")
    name = input()
    print("Steam Directory:")
    steam = input()
    print("Author Name:")
    author = input()
    print("Description:")
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
os.rename(
    f"./{id}/src/main/resources/{id}Resources/images/char/defaultCharacter",
    f"./{id}/src/main/resources/{id}Resources/images/char/{id}Character",
)
print("Renamed character folder")
print("Renamed folders")

print("Refactoring package names")
for root, subdir, file in os.walk(f"./{id}/src/main/java/{id}/"):
    for java in file:
        with open(os.path.join(root, java), "r+") as f:
            lines = f.readlines()
            newLines = []
            for newLine in lines:
                newLine = newLine.replace("theDefault", id)
                newLine = newLine.replace("TheDefault", id.capitalize())
                newLine = newLine.replace("DefaultMod", f"{id.capitalize()}Mod")
                newLine = newLine.replace("defaultCharacter", f"{id}Character")
                newLines.append(newLine)
        with open(os.path.join(root, java), "w") as f:
            f.writelines(newLines)
print("Refactored package names")

print("Renaming Files")
os.rename(
    f"./{id}/src/main/java/{id}/DefaultMod.java",
    f"./{id}/src/main/java/{id}/{id.capitalize()}Mod.java",
)
print("Renamed files")
