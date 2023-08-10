from graphics import logo

print(logo)
keep_going = True

while keep_going:
    mode = ""
    while not mode:
        mode = input("Type encode to encrypt and decode to decrypt:\n").lower().strip()
        if mode not in ('encode','decode'):
            print("Incorrect entry. Please try again.")
            mode = ""
    
    message = input("Type your message:\n").split(" ")

    shift = int(input("Type the shift number:\n")) % 26
    if shift < 0:
        shift += 26

    if mode == "encode":
        out = []
        for m in message:
            shifted_values = [ord(ch) + shift for ch in m]
            #a = 97, z = 122. if larger than z, need to circle back around to start of alphabet
            encoded_message = [chr(n) if n <= 122 else chr((n % 122) + 97)
                            for n in shifted_values]
            out.append("".join(encoded_message))
        print(f"Here's the encoded results: {' '.join(out)}")

    else:
        out = []
        for m in message:
            shifted_values = [ord(ch) - shift for ch in m]
            #if have letter a (97) and shift by 9, get 97 -> should get 113 (q); max is 122
            #for each letter less than 97, do letter - 97 + 123 = letter + 25
            decoded_message = [chr(n) if n >= 97 else chr(n + 25) for n in shifted_values]
            out.append("".join(decoded_message))
        print(f"Here's the decoded results: {' '.join(out)}")
    print()
    decision = input("Type any key + enter to keep going, otherwise press enter to quit\n")
    if not decision:
        keep_going = False

print("Goodbye.")