
import math
import time

texto = ""

# STATISTICAL INFORMATION


def lerFicheiro(ficheiro):
    global texto
    with open(ficheiro, encoding="utf8") as f:
        texto = f.read().upper()
        texto1 = ""
        for i in texto:
            if i.isalpha() or i == " " or i=="\n":
                texto1 += i
        texto = texto1
    return texto1


def alfabeto():
    global texto
    dados = [i for i in texto if i.isalpha() or i == " "]
    alfabeto = list(set(dados))
    return alfabeto


def combinations_in_text(order):
    global texto
    combinations_txt = []
    for c in range(len(texto)):
        cmb = ""
        if(c > (len(texto)) - order):
            break
        for i in range(c, order + c):
            cmb += texto[i]
        combinations_txt.append(cmb)
    return combinations_txt


def combination_next_letter(order):
    global texto

    ocorr = dict()
    alfab = alfabeto()

    for i in range(0, len(texto) - order):
        #print("Combinação: {}, Letra seguinte: {}".format(text[i : order + i], text[order + i]))
        cmb = texto[i : order + i]
        next_letter = texto[order + i]
        if cmb in ocorr:
            if next_letter in ocorr[cmb]:
                ocorr[cmb][next_letter] += 1
            else:
                ocorr[cmb][next_letter] = 1
        else:
            ocorr[cmb] = {next_letter : 1}
    return ocorr

def calc_ocorr(val):
    count = 0
    #print(val)
    lista_val = list(val.values())
    #print(lista_val)
    for x in lista_val:
        count+=x
    return count

def letter_probability(order):
    letter_prob={}
    alfb = alfabeto()
    global alpha
    lac = combination_next_letter(order)
    #print(lac)
    for key,value in lac.items():
        alf1 = alfb
        counter = 0
        alf1 = list(filter(lambda z: z not in list(value.keys()),alfb))
        #print(alf1)
        for x,v in value.items():
            if(counter>0):
                letter_prob[key][x] = (v+alpha) / (calc_ocorr(value) + alpha)
            else:
                letter_prob[key] = {x: (v+alpha) / (calc_ocorr(value) + alpha)}
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
    #print(letprob)
    #print(alfabeto())
    for k,v in letprob.items():
        entropy=0
        for x,y in v.items():
            entropy+=y*math.log(y,2)
        #print("Combinação: "+k+"    Entropia: "+str(-entropy))
    return ""

order = 4 #para alterar a ordem
ficheiro = "texto.txt" #path do ficheiro a ser lido
alpha = 0.00000000000000000001 #valor de alpha
lerFicheiro(ficheiro)
print("1ª linha - combinações possíveis\n2ª linha combinações + prob de ocorrências de cada letra a seguir à comb.\n3ª linha alfabeto\n")

s2 = time.time()
lp = letter_probability(order)

entropy_calc(lp)
print("Tempo de execução total: {} segundos".format(time.time() - s2))

combination_next_letter(order)
