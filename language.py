from fcm import *
import os
import re

def bit_estimation_for_guess(text_class, lp, cnl, alpha, order):
    alfb = alfabeto(text_class)
    probs = []
    for i in range(0, len(text_class) - order):
        cmb = text_class[i: order + i]
        next_letter = text_class[order + i]
        if cmb in lp:
            if next_letter in lp[cmb]:
                probs.append(lp[cmb][next_letter])
            else:
                probs.append(alpha/(alpha*len(alfb)+calc_ocorr(cnl[cmb])))
        else:
            probs.append(alpha/(alpha*len(alfb)))
    bit_est = 0
    for x in range(len(probs)):
        bit_est -= math.log(probs[x],2)
    return bit_est


def main():
    lang_bit = []

    order = int(input("Ordem: "))  # valor da ordem
    alpha = float(input("Valor de alpha: "))  # valor de alpha
    text_class = input("Nome do txtfile a ser adivinhado ([language(em inglês)]_guess.txt) : ")
    text_class = read_file(os.path.join(os.getcwd(), "guess_texts", text_class))


    for filename in os.listdir(os.path.join(os.getcwd(), "Idioms")):
        text = read_file(os.path.join(os.getcwd(), "Idioms", filename))
        cnl = combination_next_letter(order, text)
        lp = letter_probability(cnl, alpha, text)
        lang_bit.append((re.sub(".txt", "", filename).capitalize(), bit_estimation_for_guess(text_class, lp, cnl, alpha, order)))

    print(lang_bit)
    print("The text is in: " + (min(lang_bit, key=lambda t: t[1])[0]))
    pass


if __name__ == '__main__':
    main()
