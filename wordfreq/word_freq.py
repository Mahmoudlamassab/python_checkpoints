def word_freq(text):
    words = text.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1


assert word_freq("a b a") == {"a": 2, "b": 1}
print("Checkpoint OK")
