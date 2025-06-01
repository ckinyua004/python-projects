print("Welcome to the Cipher Message Program")

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
           "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
           "u", "v", "w", "x", "y", "z"]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for char in original_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % len(alphabet)
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for char in original_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_amount) % len(alphabet)
            decrypted_text += alphabet[new_position]
        else:
            decrypted_text += char
    return decrypted_text

if direction == "encode":
    result = encrypt(text, shift)
    print(f"The encoded message is: {result}")
elif direction == "decode":
    result = decrypt(text, shift)
    print(f"The decoded message is: {result}")
else:   
    print("Invalid direction. Please type 'encode' or 'decode'.")
    