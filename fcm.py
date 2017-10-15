
import math
import time

texto = ""

# STATISTICAL INFORMATION


def read_file(file):
    global texto
    with open(file, encoding="utf8") as f:
        texto = f.read().upper()
        texto1 = ""
        for i in texto:
            if i.isalpha() or i == " " or i == "\n":
                texto1 += i
        texto = texto1
    return texto1


def alfabeto():
    global texto
    dados = [i for i in texto if i.isalpha() or i == " "]
    alfabeto = list(set(dados))
    return alfabeto


def combination_next_letter(order):
    global texto

    ocorr = dict()

    for i in range(0, len(texto) - order):
        # print("Combinação: {}, Letra seguinte: {}".format(text[i : order + i], text[order + i]))
        cmb = texto[i: order + i]
        next_letter = texto[order + i]
        if cmb in ocorr:
            if next_letter in ocorr[cmb]:
                ocorr[cmb][next_letter] += 1
            else:
                ocorr[cmb][next_letter] = 1
        else:
            ocorr[cmb] = {next_letter: 1}
    return ocorr


def calc_ocorr(val):
    count = 0
    lista_val = list(val.values())
    for x in lista_val:
        count += x
    return count


def letter_probability(order):
    letter_prob = {}
    alfb = alfabeto()
    global alpha
    lac = combination_next_letter(order)
    for key, value in lac.items():
        alf1 = alfb
        counter = 0
        alf1 = list(filter(lambda z: z not in list(value.keys()), alfb))
        for x, v in value.items():
            if(counter > 0):
                letter_prob[key][x] = (v + alpha) / (calc_ocorr(value) + len(alfb) * alpha)
            else:
                letter_prob[key] = {x: (v + alpha) / (calc_ocorr(value) + len(alfb) * alpha)}
                counter += 1
        for l in alf1:
            letter_prob[key][l] = (alpha) / (calc_ocorr(value) + len(alfb) * alpha)
    return letter_prob


"""
def teste(letprob):
    soma = 0
    for k,v in letprob.items():
        soma = 0
        for x,y in v.items():
            soma+=y
        #print(k,soma)
    return ""
"""


def entropy_calc(letprob):

    entropy = 0
    for k, v in letprob.items():
        for x, y in v.items():
            entropy -= y * math.log(y, 2)

    print("Entropia total estimada do texto: {}".format(entropy))
    print("Entropia Média: {}".format(entropy/len(letprob.keys())))
    return ""


order = 9  # para alterar a ordem
ficheiro = "texto.txt"  # path do ficheiro a ser lido
alpha = 0.0000000000001  # valor de alpha
read_file(ficheiro)
# print("1ª linha - combinações possíveis\n2ª linha combinações + prob de ocorrências de cada letra a seguir à comb.\n3ª linha alfabeto\n")

s2 = time.time()
lp = letter_probability(order)

entropy_calc(lp)
print("Tempo de execução total: {} segundos".format(time.time() - s2))

combination_next_letter(order)
