
def encrypt(message, shift):
    result = ""

    for char in message:
        if char.isupper():
            position = ord(char) - ord("A")
            new_position = (position + shift) % 26
            result += chr(new_position + ord("A"))

        elif char.islower():
            position = ord(char) - ord("a")
            new_position = (position + shift) % 26
            result += chr(new_position + ord("a"))

        else:
            result += char

    return result


def decrypt(message, shift):
    return encrypt(message, -shift)
