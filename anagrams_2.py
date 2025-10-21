sentence = "Listen to the silent notes"

word_list = sentence.split()
sorted_word_list = []
count = 0
for i in word_list:
    sorted_word = ''.join(sorted(i.lower()))
    sorted_word_list.append(sorted_word)
for q in range(len(sorted_word_list)):
    if sorted_word_list.count(sorted_word_list[q]) > 1:
        count+=1
        print(word_list[q])
if count == 0:
    print("-1")
    
