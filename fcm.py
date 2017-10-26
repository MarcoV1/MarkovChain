
import math
import time

# STATISTICAL INFORMATION


def read_file(file):
    with open(file, encoding="utf8") as f:
        texto = f.read().upper()
        texto1 = ""
        for i in texto:
            if i.isalpha() or i == " " or i == "\n":
                texto1 += i
    return texto1


def alfabeto(texto):
    dados = [i for i in texto if i.isalpha() or i == " "]
    alfabeto = list(set(dados))
    return alfabeto


def combination_next_letter(order,texto):
    ocorr = dict()

    for i in range(0, len(texto) - order):
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


def letter_probability(cnl,alpha,texto):
    letter_prob = {}
    alfb = alfabeto(texto)

    for key, value in cnl.items():
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


def teste(letprob):
    soma = 0
    for k,v in letprob.items():
        soma = 0
        for x,y in v.items():
            soma+=y
    return ""



def get_every_ocorr(dictio):
    count = 0
    for key, value in dictio.items():
        for k, v in value.items():
            count += v
    return count


def entropy_calc(letprob, cnl):
    geo = get_every_ocorr(cnl)
    entropy_total = 0
    for k, v in letprob.items():
        entropy = 0
        for x, y in v.items():
            entropy -= y * math.log(y, 2)

        entropy_total += entropy * (calc_ocorr(cnl[k])/geo)
    return entropy_total



