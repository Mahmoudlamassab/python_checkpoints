def is_vowel(letter):
    return letter.lower() in "aeiou"


def count_vowels(text):
    return sum(is_vowel(char) for char in text)


assert count_vowels("Hello World") == 3
print("Checkpoint OK")
