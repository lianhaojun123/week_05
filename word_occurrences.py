WORD_COUNT = {}

text = input("Text: ")
text_words = text.split()

for text_word in text_words:
    WORD_COUNT[text_word] = WORD_COUNT.get(text_word, 0) + 1


text_list = [text_word for text_word in WORD_COUNT.items()]
text_list.sort()
longest_word = len(text_words)

for i in range(len(text_list)):
    print(f"{text_list[i][0]:{longest_word}} : {text_list[i][1]}")


