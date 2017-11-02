from fcm import *

def bit_estimation_for_guess(text_class,lp,cnl):
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


lang_bit = []
order = int(input("Ordem: "))  # valor da ordem
alpha = float(input("Valor de alpha: "))   # valor de alpha
text_class = input("Nome do txtfile a ser adivinhado ([language(em inglês)]_guess.txt) : ")
text_class = read_file('guess_texts\\' + text_class)


ficheiro = "Idioms\\english.txt"
texto = read_file(ficheiro)
cnl = combination_next_letter(order,texto)
lp = letter_probability(cnl,alpha,texto)
lang_bit.append(("English",bit_estimation_for_guess(text_class,lp,cnl)))


ficheiro = "Idioms\\french.txt"
texto = read_file(ficheiro)
cnl = combination_next_letter(order,texto)
lp = letter_probability(cnl,alpha,texto)
lang_bit.append(("French",bit_estimation_for_guess(text_class,lp,cnl)))



ficheiro = "Idioms\\portuguese.txt"
texto = read_file(ficheiro)
cnl = combination_next_letter(order,texto)
lp = letter_probability(cnl,alpha,texto)
lang_bit.append(("Portuguese",bit_estimation_for_guess(text_class,lp,cnl)))



ficheiro = "Idioms\\german.txt"
texto = read_file(ficheiro)
cnl = combination_next_letter(order,texto)
lp = letter_probability(cnl,alpha,texto)
lang_bit.append(("German",bit_estimation_for_guess(text_class,lp,cnl)))
print("Formato: (Linguagem, Estimação de bits)")
print(lang_bit)
print("\nThe text is in: "+(min(lang_bit, key=lambda t: t[1])[0]))





