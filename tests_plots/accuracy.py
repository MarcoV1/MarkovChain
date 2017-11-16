from fcm import *
from language import bit_estimation_for_guess
import os, re
from time import time as tm


confusion_matrix = dict()
order = 3
alpha = 0.01
tamanhos = [700000, 600000, 500000, 400000, 300000, 200000, 100000, 50000, 25000]

total = tm()

for tamanho in tamanhos:
    print("Para tamanho = ", str(tamanho))
    lang_length, lang_learn = [], []
    for idioms in os.listdir(os.path.join(os.getcwd(), "..", "Idioms")):
        text = read_file(os.path.join(os.getcwd(), "..", "Idioms", idioms))
        text = text[0: tamanho]
        lang_length.append((len(text), re.sub(".txt", "", idioms).capitalize()))

        cnl = combination_next_letter(order, text)
        lp = letter_probability(cnl, alpha, text)

        lang_learn.append((re.sub(".txt", "", idioms).capitalize(), lp, cnl))

    print(lang_length)

    for idiom in os.listdir(os.path.join(os.getcwd(), "..", "Classifier")):
        start = tm()
        language = idiom
        print("Começou", language)
        for text in os.listdir(os.path.join(os.getcwd(), "..", "Classifier", idiom)):
            text_guess = read_file(os.path.join(os.getcwd(), "..", "Classifier", language, text))
            lang_bit = []
            for data in lang_learn:
                be = bit_estimation_for_guess(text_guess, data[1], data[2], alpha, order)
                lang_bit.append((data[0], be))

            lang_guess = min(lang_bit, key=lambda t: t[1])[0]

            if language in confusion_matrix:
                if lang_guess in confusion_matrix[language]:
                    confusion_matrix[language][lang_guess] += 1
                else:
                    confusion_matrix[language][lang_guess] = 1
            else:
                confusion_matrix[language] = {lang_guess: 1}

            '''if language == lang_guess:
                for j in lang_accuracy:
                    if j[0] == language:
                        j[1] += 1
                        break
'''
        print("Acabou", language, (tm() - start), "seg")

end = tm() - total

print("Tempo total:", int(end / 60), "minutos e ", round(end % 60, 2), "segundos")

for lang, data in confusion_matrix.items():
    print(lang)
    for language_guess, ocorr in data.items():
        print("\t" + language_guess, ": ", ocorr)

