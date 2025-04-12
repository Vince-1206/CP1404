"""
Word Occurrences
Estimate: 20 minutes
Actual:
"""

import string

def count_word_occurrences(text):
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    words = text.lower().split()
    word_counts = {}

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

def print_sorted_word_counts(word_counts):
    longest_word_length = max(len(word) for word in word_counts)

    for word in sorted(word_counts):
        print(f"{word:{longest_word_length}} : {word_counts[word]}")

if __name__ == "__main__":
    text = input("Text: ")
    word_counts = count_word_occurrences(text)
    print_sorted_word_counts(word_counts)
