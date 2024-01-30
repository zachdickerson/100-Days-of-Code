# This was my method in solving this problem.

# Does not account for large shift amounts

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(start_text,shift_amount,cipher_direction):
    found_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == 'encode':
            new_position = position + shift_amount
            if new_position > 25:
                new_position -= 26
            found_text += alphabet[new_position]
        else:
            new_position = position - shift_amount
            if new_position < 0:
                new_position += 26
            found_text += alphabet[new_position]
    
    print(f"The {cipher_direction}d text is {found_text}")

ceaser(start_text=text,shift_amount=shift,cipher_direction=direction)
