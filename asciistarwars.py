from random import randint
file = open("characters.txt","r")


characters = []
character = ""

for line in file:
    if line != ",\n":
        character += line
    else:
        characters.append(character)
        character = ""
file.close()


print("Your character is\n")

randInt = randint(1, 16)

print(characters[randInt])

print("\n\n\nAscii art source:\nwww.ascii-art.de")
