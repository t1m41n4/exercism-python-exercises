def is_pangram(sentence):
    unique_letters = set()

    for char in sentence.lower():
        if 'a' <= char <= 'z':
            unique_letters.add(char)

    return len(unique_letters) == 26
