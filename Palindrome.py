word_list = ["kayak","deified","rotator","Salam", "apple", "banana", "rotator"]
palindrome_words = []
longest_pal_word = ""
for word in word_list:
    if word == word[::-1]:
        palindrome_words.append(word)
for i in palindrome_words:
    if i > longest_pal_word:
        longest_pal_word = i
print(f"Palindrome words: {palindrome_words}")
print(f"Longest palindrome word: {longest_pal_word}, length: {len(longest_pal_word)}, count: {palindrome_words.count(longest_pal_word)}")