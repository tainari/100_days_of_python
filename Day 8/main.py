from graphics import logo

print(logo)

mode = input("Type encode to encrypt and decode to decrypt:\n").lower().strip()

message = input("Type your message:\n")

shift = int(input("Type the shift number:\n")) % 26
if shift < 0:
    shift += 26

if mode == "encode":
    shifted_values = [ord(ch) + shift for ch in message]
    #a = 97, z = 122. if larger than z, need to circle back around to start of alphabet
    encoded_message = [chr(n) if n <= 122 else chr((n % 122) + 97)
                       for n in shifted_values]
    print(f"Here's the encoded results: {''.join(encoded_message)}")

else:
    shifted_values = [ord(ch) - shift for ch in message]
    #if have letter a (97) and shift by 9, get 97 -> should get 113 (q); max is 122
    #for each letter less than 97, do letter - 97 + 123 = letter + 25
    decoded_message = [chr(n) if n >= 97 else chr(n + 25) for n in shifted_values]
    print(f"Here's the decoded results: {''.join(decoded_message)}")
