word_list = ["kayak","deified","rotator","Salam", "apple", "banana", "rotator"]
longest_pal_word = ""
for word in word_list:
    if word == word[::-1] and word > longest_pal_word:
        longest_pal_word = word
print(longest_pal_word, len(longest_pal_word))
