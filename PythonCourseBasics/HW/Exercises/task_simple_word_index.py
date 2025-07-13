#--------------------------------------------Task:-------------------------------------------------#
# Write in file named task_simple_word_index.py
# Make a program which will counts how many times a word appears in given text

text = """apple and banana one apple one banana
a red apple and a green apple"""

words = text.lower().split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(f"{word} - {count}")
#--------------------------------------------------------------------------------------------------#