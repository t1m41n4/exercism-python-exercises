def rotate(text, key):
    result = []

    for char in text:
        if 'a' <= char <= 'z':  # Check if character is a lowercase letter
            new_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':  # Check if character is an uppercase letter
            new_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:  # Non-alphabetic characters remain the same
            new_char = char
        result.append(new_char)

    return ''.join(result)