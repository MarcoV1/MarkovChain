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
    for x in probs:
        bit_est -= math.log(probs,2)
    return bit_est


def main():
    lang_bit = []
    manual_values, text_guess = "", ""
    quit = False

    while manual_values not in ('yes', 'y', 'no', 'n'):
        manual_values = input("Manually input order and alpha values? (y/n) ").lower()

        if manual_values in ('yes', 'y'):
             while True:
                order = input("Order: ")  # valor da ordem
                try:
                    order = int(order)
                except ValueError:
                    print("Invalid value for order, must be integer.")
                    continue
                if order < 1:
                    print("Order must be a value greater or equal to 1.")
                    continue
                break

             while True:
                alpha = input("Alpha value: ")  # valor de alpha
                try:
                    alpha = float(alpha)
                except ValueError:
                    print("Invalid value for alpha, must be float.")
                    continue
                if alpha <= 0:
                    print("Alpha must be a value greater than zero.")
                    continue
                break

        elif manual_values in ('no', 'n'):
            order, alpha = 3, 0.000001
            print("Using default values. Order -> {}, Alpha -> {}.".format(order, alpha))

        else:
            print("\tPlease answer y/yes or n/no.")

    print('''
Let's guess the language.
Choose an option.
1 - Read one of the default guess text files.
2 - Read a custom text file.
3 - Input a text.
4 - exit''')
    op = ""
    while op not in ("1", "2", "3", "4"):
        op = input("Option: ")
        if op not in ("1", "2", "3", "4"):
            print("\tInvalid option.\n")

    if op == "1":
        text_class = input("\nText file name ([language]_guess.txt) : ")
        text_guess = read_file(os.path.join(os.getcwd(), "guess_texts", text_class))
    elif op == "2":
        text_class = input("\nName of Text File (with absolute path if needed): ")
        text_guess = read_file(text_class)
    elif op == "3":
        text_class = input("\nText: ")
        text_guess = read_text(text_class)
    elif op == "4":
        quit = True

    if not quit:
        for filename in os.listdir(os.path.join(os.getcwd(), "Idioms")):
            text = read_file(os.path.join(os.getcwd(), "Idioms", filename))
            cnl = combination_next_letter(order, text)
            lp = letter_probability(cnl, alpha, text)
            lang_bit.append((re.sub(".txt", "", filename).capitalize(), bit_estimation_for_guess(text_guess, lp, cnl, alpha, order)))

        print(lang_bit)
        print("The text is in: " + (min(lang_bit, key=lambda t: t[1])[0]))
    else:
        print("Program exit.")
        exit()


    '''
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
    '''

if __name__ == '__main__':
    ra = ""
    main()
    while ra.lower() not in ('yes', 'y', 'no', 'n'):
        ra = input("Run program again? (y/n) ").lower()

        if ra in ('yes', 'y'):
            main()
            continue

        elif ra in ('no', 'n'):
            print("Program exit.")
            break

        else:
            print("\tPlease answer y/yes or n/no.")
