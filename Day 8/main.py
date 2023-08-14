from graphics import logo

alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

print(logo)
keep_going = True

while keep_going:
    mode = ""
    while not mode:
        mode = input("Type encode to encrypt and decode to decrypt:\n").lower().strip()
        if mode not in ('encode','decode'):
            print("Incorrect entry. Please try again.")
            mode = ""
    
    message = input("Type your message:\n").lower()
    message = message.split(" ")
    # message = ""
    # while not message:
    #     message = input("Type your message:\n").lower()
    #     if set(message).difference("abcdefghijklmnopqrstuvwxyz"):
    #         print("Please do not include numbers or symbols. Letters or spaces only.")
    #         message = ""
    #     else:
    #         message = message.split(" ")


    shift = int(input("Type the shift number:\n")) % 26
    if shift < 0:
        shift += 26

    if mode == "encode":
        out = []
        for word in message:
            shifted_values = [ord(ch) + shift if ch in alphabet else ch for ch in word]
            #a = 97, z = 122. if larger than z, need to circle back around to start of alphabet
            encoded_word = []
            for n in shifted_values:
                if type(n) == int:
                    if n <= 122:
                        encoded_word.append(chr(n))
                    else:
                        encoded_word.append(chr(n % 122 + 97))
                else:
                    encoded_word.append(n)
            # encoded_word = [chr(n) if n <= 122 else chr((n % 122) + 97)
            #                 for n in shifted_values]
            out.append("".join(encoded_word))
        print(f"Here's the encoded results: {' '.join(out)}")

    else:
        out = []
        for word in message:
            shifted_values = [ord(ch) - shift if ch in alphabet else ch for ch in word]
            #if have letter a (97) and shift by 9, get 97 -> should get 113 (q); max is 122
            #for each letter less than 97, do letter - 97 + 123 = letter + 25
            decoded_word = []
            for n in shifted_values:
                if type(n) == int:
                    if n >= 97:
                        decoded_word.append(chr(n))
                    else:
                        decoded_word.append(chr(n + 25))
                else:
                    decoded_word.append(n)
            # decoded_word = [chr(n) if n >= 97 else chr(n + 25) for n in shifted_values]
            out.append("".join(decoded_word))
        print(f"Here's the decoded results: {' '.join(out)}")
    print()
    decision = input("Type any key + enter to keep going, otherwise press enter to quit\n")
    if not decision:
        keep_going = False

print("Goodbye.")