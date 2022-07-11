alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
repeat = True


def caesar(plain_text, plain_shift, plain_direction):
    final_text = ""
    for char in plain_text:
        if char in alphabet:
            new_position = 0
            if plain_direction == "encode":
                new_position = alphabet.index(char) + plain_shift
            elif plain_direction == "decode":
                new_position = alphabet.index(char) - plain_shift
            if new_position >= len(alphabet) or new_position < 0:
                new_position = new_position % len(alphabet)
            final_text += alphabet[new_position]
        else:
            final_text += char
    print(f"Your {plain_direction}d word is: {final_text}")


while repeat:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    ask_for_repeat = input("Do you want to repeat? Type 'no' to stop\n").lower()
    if ask_for_repeat == "no":
        repeat = False

print("Goodbye")