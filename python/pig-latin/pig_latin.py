def translate(text):
    def translate_word(word):
        vowels = "aeiou"
        if word[0] in vowels or word[:2] in ["xr", "yt"]:
            return word + "ay"

        for i in range(len(word)):
            if word[i] in vowels or (word[i] == "y" and i != 0):
                # Special case for "qu"
                if word[i-1:i+1] == "qu":
                    return word[i+1:] + word[:i+1] + "ay"
                return word[i:] + word[:i] + "ay"
        return word + "ay"

    return ' '.join(translate_word(word) for word in text.split())