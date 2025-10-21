sentence = "Listen to the silent notes"

word_list = sentence.split()
sorted_word_list = []
for i in word_list:
    sorted_word = ''.join(sorted(i.lower()))
    print(sorted_word)
    sorted_word_list.append(sorted_word)
for q in range(len(sorted_word_list)):
    if sorted_word_list.count(sorted_word_list[q]) > 1:
        print(word_list[q])
