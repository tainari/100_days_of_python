import re

starting_letter = []
with open("Input/Letters/starting_letter.txt",'r') as f:
    for r in f.readlines():
        starting_letter.append(r.strip())

names = []
with open("Input/Names/invited_names.txt",'r') as f:
    for r in f.readlines():
        names.append(r.strip())

for name in names:
    with open(f"Output/ReadyToSend/letter_for_{re.sub(' ','_',name.lower())}.txt",'w') as f:
        for ind,row in enumerate(starting_letter):
            if ind == 0:
                row = re.sub("\[name\]",name,row)
            f.write(row + "\n")