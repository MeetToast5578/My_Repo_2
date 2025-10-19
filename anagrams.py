# Klaviaturadan daxil edilmiş sözlərdən ibarət cümlə şəklində verilmiş sətirdə anagram sözləri çapa verən proqramı Python dilində yazın.

# Qeyd : əgər yoxdursa "-1" çapa versin

sentence_ = "Listen to the silent notes"
def anagrams(sentence):
    word_count_dict = dict()
    word_dict = dict()
    word_list = sentence.split(' ')
    sorted_word_list = []
    for word in word_list:
        sorted_word = ''.join(sorted(word.lower()))
        sorted_word_list.append(sorted_word)
        word_dict.update({word: sorted_word})
    for i in sorted_word_list:
        if sorted_word_list.count(i) > 1:
            word_count_dict.update({i: sorted_word_list.count(i)})
    if len(word_count_dict) > 0:
        print("Anagrams Found")
    else:
        print("Anagrams not found", -1)
    try:       
        for item in word_dict:
            for q in word_count_dict:
                if q == word_dict.get(item):
                    print(item)
    except Exception as e:
        print(e)
        
anagrams(sentence_)