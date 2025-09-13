number_list = [1, 2, 2, 3, 4, 4, 5]
set_from_list = set(number_list)
print(f"Set from list: {set_from_list}")


#Practical Example

unique_words = set()
sentences = [
    "the quick brown fox",
    "jumps over the lazy dog",
    "the quick brown fox jumps again"
]

for sentence in sentences:
    words = set(sentence.split())
    unique_words.update(words)

print(f"All unique words: {unique_words}")
print(f"Total unique words: {len(unique_words)}")
