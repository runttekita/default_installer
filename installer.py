import requests
import zipfile
import os
import shutil

group_id = ""
id = ""
name = ""
dir = "."
steam = ""
author = ""
desc = ""


def take_data():
    global id, name, steam, author, desc, group_id
    print("Group ID (no spaces):")
    group_id = input()
    if " " in group_id:
        print("No spaces in group id")
        take_data()
        return
    print("Artifact ID (no spaces, lowercase first letter):")
    id = input()
    if " " in id or id[0].isupper():
        print("Cannot have spaces or uppercase letters as first letter in id")
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

print("Refactoring files")
for root, subdir, file in os.walk(f"./{id}/src/main/java/{id}/"):
    for java in file:
        with open(os.path.join(root, java), "r") as f:
            lines = f.readlines()
            newLines = []
            for newLine in lines:
                newLine = newLine.replace("theDefault", id)
                newLine = newLine.replace("TheDefault", id.capitalize())
                newLine = newLine.replace("DefaultMod", f"{id.capitalize()}Mod")
                newLine = newLine.replace("defaultCharacter", f"{id}Character")
                newLine = newLine.replace("defaultMod", f"{id}Mod")
                newLine = newLine.replace("Default Mod", name)
                newLine = newLine.replace(
                    "A base for Slay the Spire to start your own mod from, feat. the Default.",
                    desc,
                )
                newLine = newLine.replace("Gremious", author)
                newLines.append(newLine)
        with open(os.path.join(root, java), "w") as f:
            f.writelines(newLines)

with open(f"./{id}/pom.xml", "r") as f:
    lines = f.readlines()
    newLines = []
    for newLine in lines:
        newLine = newLine.replace("defaultmod", group_id)
        newLine = newLine.replace("DefaultMod", id)
        newLine = newLine.replace("C:/My Stuff/Games/Steam/steamapps", steam)
        newLine = newLine.replace("Default Mod", name)
        newLine = newLine.replace("A default base to start your own mod from.", desc)
        newLines.append(newLine)
    with open(f"./{id}/pom.xml", "w") as f:
        f.writelines(newLines)

# Gross copy paste thats compeltely unececesary but im lazy and heck spelling
for root, subdir, file in os.walk(f"./{id}/src/main/resources/{id}Resources/localization/eng/"):
    for java in file:
        with open(os.path.join(root, java), "r") as f:
            lines = f.readlines()
            newLines = []
            for newLine in lines:
                newLine = newLine.replace("theDefault", id)
                newLine = newLine.replace("TheDefault", id.capitalize())
                newLine = newLine.replace("DefaultMod", f"{id.capitalize()}Mod")
                newLine = newLine.replace("defaultCharacter", f"{id}Character")
                newLine = newLine.replace("defaultMod", f"{id}Mod")
                newLine = newLine.replace("Default Mod", name)
                newLine = newLine.replace(
                    "A base for Slay the Spire to start your own mod from, feat. the Default.",
                    desc,
                )
                newLine = newLine.replace("Gremious", author)
                newLines.append(newLine)
        with open(os.path.join(root, java), "w") as f:
            f.writelines(newLines)

with open(f"./{id}/pom.xml", "r") as f:
    lines = f.readlines()
    newLines = []
    for newLine in lines:
        newLine = newLine.replace("defaultmod", group_id)
        newLine = newLine.replace("DefaultMod", id)
        newLine = newLine.replace("C:/My Stuff/Games/Steam/steamapps", steam)
        newLine = newLine.replace("Default Mod", name)
        newLine = newLine.replace("A default base to start your own mod from.", desc)
        newLines.append(newLine)
    with open(f"./{id}/pom.xml", "w") as f:
        f.writelines(newLines)


print("Refactored files")

print("Renaming Files")
os.rename(
    f"./{id}/src/main/java/{id}/DefaultMod.java",
    f"./{id}/src/main/java/{id}/{id.capitalize()}Mod.java",
)
os.rename(
    f"./{id}/src/main/java/{id}/characters/TheDefault.java",
    f"./{id}/src/main/java/{id}/characters/{id.capitalize()}.java",
)
os.rename(
    f"./{id}/src/main/resources/{id}Resources/localization/eng/DefaultMod-Card-Strings.json",
    f"./{id}/src/main/resources/{id}Resources/localization/eng/{id.capitalize()}Mod-Card-Strings.json"
)
os.rename(
    f"./{id}/src/main/resources/{id}Resources/localization/eng/DefaultMod-Character-Strings.json",
    f"./{id}/src/main/resources/{id}Resources/localization/eng/{id.capitalize()}Mod-Character-Strings.json"
)

os.rename(
    f"./{id}/src/main/resources/{id}Resources/localization/eng/DefaultMod-Event-Strings.json",
    f"./{id}/src/main/resources/{id}Resources/localization/eng/{id.capitalize()}Mod-Event-Strings.json"
)

os.rename(
    f"./{id}/src/main/resources/{id}Resources/localization/eng/DefaultMod-Keyword-Strings.json",
    f"./{id}/src/main/resources/{id}Resources/localization/eng/{id.capitalize()}Mod-Keyword-Strings.json"
)

os.rename(
    f"./{id}/src/main/resources/{id}Resources/localization/eng/DefaultMod-Orb-Strings.json",
    f"./{id}/src/main/resources/{id}Resources/localization/eng/{id.capitalize()}Mod-Orb-Strings.json"
)

os.rename(
    f"./{id}/src/main/resources/{id}Resources/localization/eng/DefaultMod-Potion-Strings.json",
    f"./{id}/src/main/resources/{id}Resources/localization/eng/{id.capitalize()}Mod-Potion-Strings.json"
)

os.rename(
    f"./{id}/src/main/resources/{id}Resources/localization/eng/DefaultMod-Power-Strings.json",
    f"./{id}/src/main/resources/{id}Resources/localization/eng/{id.capitalize()}Mod-Power-Strings.json"
)

os.rename(
    f"./{id}/src/main/resources/{id}Resources/localization/eng/DefaultMod-Relic-Strings.json",
    f"./{id}/src/main/resources/{id}Resources/localization/eng/{id.capitalize()}Mod-Relic-Strings.json"
)

os.rename(
    f"./{id}/src/main/resources/{id}Resources/images/char/wammyChar/theDefaultAnimation.autosave.scml",
    f"./{id}/src/main/resources/{id}Resources/images/char/wammyChar/{id}Animation.autosave.scml",
)

os.rename(
    f"./{id}/src/main/resources/{id}Resources/images/char/wammyChar/theDefaultAnimation.scml",
    f"./{id}/src/main/resources/{id}Resources/images/char/wammyChar/{id}Animation.scml",
)

print("Renamed files")
