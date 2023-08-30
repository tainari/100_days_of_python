import pandas

alphabet_data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet = {row.letter:row.code for (ind, row) in alphabet_data.iterrows()}

user_word = input("Please enter a word to translate: ")

if not user_word:
    print("Nothing entered. Exiting now.")
    quit()

translated_word = [nato_alphabet.get(ch.upper(),ch) for ch in user_word]

print(f"Your output is: {' '.join(translated_word)}")