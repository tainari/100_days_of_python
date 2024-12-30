with open("./Input/Letters/starting_letter.txt") as f:
    template = f.read()

with open("./Input/Names/invited_names.txt") as f:
    names = f.readlines()

for name in names:
    name = name.strip()
    letter = template.replace("[name]", name)
    with open("./Output/ReadyToSend/" + name + ".txt", "w") as f:
        f.write(letter)
    print(f"Letter to {name} complete.")