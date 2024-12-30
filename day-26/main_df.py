import pandas

df = pandas.read_csv("./nato_phonetic_alphabet.csv")
alphabet = {}
for index, row in df.iterrows():
    alphabet[row.letter] = row.code

more = True
while more:
    user_name = input("Type a name to convert: ").lower()
    if user_name == 'quit':
        more = False
    else:
        output = [alphabet.get(letter, letter) for letter in user_name]
        print(output)