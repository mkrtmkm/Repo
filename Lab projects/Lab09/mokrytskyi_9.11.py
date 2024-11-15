n, m = map(int, input().split())
vocabulary = {input().strip().lower() for _ in range(n)}
text_lines = [input().strip() for _ in range(m)]

text = " ".join(text_lines)
punctuation = {'.', ',', ':', ';', '-', "'", '"', '!', '?'}

words_in_text = set()
word = []

for char in text.lower():
    if char.isalpha() or char == "'":  
        word.append(char)
    else: 
        if word:
            words_in_text.add("".join(word))
            word = []

if word:
    words_in_text.add("".join(word))

if words_in_text <= vocabulary and vocabulary <= words_in_text:
    print("Everything is going to be OK.")
elif not words_in_text <= vocabulary:
    print("Some words from the text are unknown.")
else:
    print("The usage of the vocabulary is not perfect.")