# ---------------------------------- Task 2 ---------------------------------- #
words = []


while True:
    word = input("Enter a word: ")
    if word == '0':
        break
    words.append(word)


vowel_words = [w for w in words if w[0].lower() in 'aeiou']


print("Words that start with a vowel:", vowel_words)
# ---------------------------------------------------------------------------- #