from fcm import *
from language import bit_estimation_for_guess
import os, re, time as tm

percentage = [0.05, 0.1, 0.25, 0.5, 0.75, 1]
lang_accuracy = []
each_lang = []
confusion_matrix = dict()
order = 3
alpha = 0.01

total = tm.time()

for idioms in os.listdir(os.path.join(os.getcwd(), "..\\Idioms")):
    text = read_file(os.path.join(os.getcwd(), "..\\Idioms", idioms))
    each_lang.append((re.sub(".txt", "", idioms).capitalize(), text))

for langs in os.listdir(os.path.join(os.getcwd(), "..\\guess_texts")):
    lang_accuracy.append([re.sub("_guess.txt", "", langs).capitalize(), 0])

for guess in os.listdir(os.path.join(os.getcwd(), "..\\guess_texts")):
    start = tm.time()
    text_guess = read_file(os.path.join(os.getcwd(), "..\\guess_texts", guess))
    language = re.sub("_guess.txt", "", guess).capitalize()
    
    print("Começou", language)

    for p1 in percentage:
        lang_learn = []
        for l, s in each_lang:
            cnl = combination_next_letter(order, s[0: round(len(s) * p1)])
            lp = letter_probability(cnl, alpha, s[0: round(len(s) * p1)])

            lang_learn.append((re.sub(".txt", "", l).capitalize(), lp, cnl))

        for p2 in percentage:
            lang_bit = []
            for data in lang_learn:
                be = bit_estimation_for_guess(text_guess[0: round(len(text_guess) * p2)], data[1], data[2], alpha, order)
                lang_bit.append((re.sub(".txt", "", data[0]).capitalize(), be))

            lang_guess = min(lang_bit, key=lambda t: t[1])[0]

            if language in confusion_matrix:
                if lang_guess in confusion_matrix[language]:
                    confusion_matrix[language][lang_guess] += 1
                else:
                    confusion_matrix[language][lang_guess] = 1
            else:
                confusion_matrix[language] = {lang_guess: 1}


            if language == lang_guess:
                for j in lang_accuracy:
                    if j[0] == language:
                        j[1] += 1
                        break
    
    print("Acabou", language, (tm.time() - start), "seg")

end = tm.time() - total
    
print(lang_accuracy)
print([(x, y / len(percentage) ** 2) for x, y in lang_accuracy])
print("Tempo total:", (end / 60), "minutos e ", (end % 60), "segundos")

for lang, data in confusion_matrix.items():
    print(lang)
    for language_guess, ocorr in data.items():
        print("\t" + language_guess, ": ", ocorr)
