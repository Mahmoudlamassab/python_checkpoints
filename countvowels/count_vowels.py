def is_vowel(letter):
    return letter.lower() in "aeiou"

def count_vowels(text):
    count = 0
    for char in text:
        if is_vowel(char):
            count += 1
    return count

assert count_vowels("Hello World") == 3
print("Checkpoint OK")