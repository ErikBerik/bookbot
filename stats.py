def count_words(input_string):
    words = input_string.split()
    return len(words)

def count_characters(input_string):
    lowercase_input = input_string.lower()
    counts = {}
    for char in lowercase_input:
        counts.setdefault(char,0)
        counts[char] += 1
    return counts