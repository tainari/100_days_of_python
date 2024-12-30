import csv

alphabet = {}
with open("nato_phonetic_alphabet.csv") as f:
    rd = csv.reader(f)
    next(rd)
    for row in rd:
        alphabet[row[0].lower().strip()] = row[1].strip()

more = True
while more:
    user_name = input("Type a name to convert: ").lower()
    if user_name == 'quit':
        more = False
    else:
        output = [alphabet.get(letter, letter) for letter in user_name]
        print(output)