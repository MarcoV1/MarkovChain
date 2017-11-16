import numpy as np
import matplotlib.pyplot as plt
from fcm import *
from language import bit_estimation_for_guess
import os
import time as tm

width = 0.15
#alpha_set = np.asarray([0.9, 0.5, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001]) # alpha
width_set = np.arange(1, 10)
alpha = 0.9

total = tm.time()

it = read_file(os.path.join(os.getcwd(), "guess_texts", "italian_guess.txt"))

text_pt = read_file(os.path.join(os.getcwd(), "Idioms", "portuguese.txt"))
text_en = read_file(os.path.join(os.getcwd(), "Idioms", "english.txt"))
text_fr = read_file(os.path.join(os.getcwd(), "Idioms", "french.txt"))
text_es = read_file(os.path.join(os.getcwd(), "Idioms", "spanish.txt"))
text_it = read_file(os.path.join(os.getcwd(), "Idioms", "italian.txt"))

langbit_pt, langbit_en, langbit_fr, langbit_es, langbit_it = [], [], [], [], []
i = 0
for order in width_set:
    i += 1
    start = tm.time()

    cnl_pt = combination_next_letter(order, text_pt)
    lp_pt = letter_probability(cnl_pt, alpha, text_pt)

    cnl_en = combination_next_letter(order, text_en)
    lp_en = letter_probability(cnl_en, alpha, text_en)

    cnl_fr = combination_next_letter(order, text_fr)
    lp_fr = letter_probability(cnl_fr, alpha, text_fr)

    cnl_es = combination_next_letter(order, text_es)
    lp_es = letter_probability(cnl_es, alpha, text_es)

    cnl_it = combination_next_letter(order, text_it)
    lp_it = letter_probability(cnl_it, alpha, text_it)

    langbit_pt.append(bit_estimation_for_guess(it, lp_pt, cnl_pt, alpha, order))
    langbit_en.append(bit_estimation_for_guess(it, lp_en, cnl_en, alpha, order))
    langbit_fr.append(bit_estimation_for_guess(it, lp_fr, cnl_fr, alpha, order))
    langbit_es.append(bit_estimation_for_guess(it, lp_es, cnl_es, alpha, order))
    langbit_it.append(bit_estimation_for_guess(it, lp_it, cnl_it, alpha, order))

    end = tm.time() - start

    print("Fez", i, "Time:", round(end, 2), "s")

fig, ax = plt.subplots()

enbit = ax.bar(width_set, langbit_en, width, color='r')
frbit = ax.bar(width_set + width, langbit_fr, width, color='b')
ptbit = ax.bar(width_set + width*2, langbit_pt, width, color='#1a5916')
esbit = ax.bar(width_set + width*3, langbit_es, width, color='y')
itbit = ax.bar(width_set + width*4, langbit_it, width, color='#52cc2a')

# add some text for labels, title and axes ticks
ax.set_ylabel('Bits')
ax.set_title('Estimação de bits para Italiano')
ax.set_xticks(width_set + width / 2)
#ax.set_xticklabels(('0.9', '0.5', '0.1', '0.01', '0.001', '0.0001', '0.00001', '0.000001', '0.0000001'))
ax.set_xticklabels(('Ordem 1', 'Ordem 2', 'Ordem 3', 'Ordem 4', 'Ordem 5', 'Ordem 6', 'Ordem 7', 'Ordem 8', 'Ordem 9'))

ax.legend((enbit[0], frbit[0], ptbit[0], esbit[0], itbit[0]), ('Inglês', 'Francês', 'Português', 'Espanhol', 'Italiano'))


def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2, height,
                '%d' % int(height),
                ha='center', va='bottom')


print("Total time: ", round(tm.time() - total, 2), "s")

plt.show()
