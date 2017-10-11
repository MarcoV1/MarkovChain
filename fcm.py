import itertools
import math
texto = ""
alpha = 0.00000000000000000001
def lerFicheiro(ficheiro):
    with open(ficheiro) as f:
        global texto
        texto = f.read().upper()

def alfabeto():
    dados = [i for i in texto if i.isalpha() or i == " "]
    alfabeto = list(set(dados))
    return alfabeto

def combinations_in_text(order):
    combinations = list(itertools.product(alfabeto(), repeat = order))
    combinations_in_text = []
    for i in combinations:
        combinations_in_text.append(''.join(i))
    cmb = []
    for c in combinations_in_text:
        if(c in texto):
            cmb.append(c)
    return cmb

def letter_after_comb(order):
    ocorr = {}

    cmb = combinations_in_text(order)
    for c in cmb:
        s = texto.split(c)
        for i in range(1,len(s)):
            if(s[i]!=""):
                letra = s[i][0]
                if c in ocorr:
                    if letra in ocorr[c]:
                        ocorr[c][letra]+=1
                    else:
                        ocorr[c][letra]=1
                else:
                    ocorr[c] = {letra : 1}
            elif(s[i]=="" and i<len(s)-1):
                letra = c[0]
                if c in ocorr:
                    if letra in ocorr[c]:
                        ocorr[c][letra]+=1
                    else:
                        ocorr[c][letra]=1
                else:
                    ocorr[c]= {letra : 1}
    global alpha
    for a in ocorr:
        for x in alfabeto():
            if x not in ocorr[a]:
                ocorr[a][x] = alpha

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
    alfab = alfabeto()
    global alpha
    lac = letter_after_comb(order)
    cmb = combinations_in_text(order)
    print(cmb)
    for key,value in lac.items():
        counter = 0
        for x,v in value.items():
            if(counter>0):
                if(v==alpha):
                    letter_prob[key][x] = v / calc_ocorr(value) + alpha
                else:
                    letter_prob[key][x] = v / calc_ocorr(value)
            else:
                if(v==alpha):
                    letter_prob[key] = {x: v / calc_ocorr(value) + alpha}
                else:
                    letter_prob[key] = {x: v / calc_ocorr(value)}
                counter += 1
    return letter_prob
""" para ver se as probabilidades das letras nas combs dá 1 tudo somado
def teste(letprob):
    print(letprob)
    soma = 0
    for k,v in letprob.items():
        soma = 0
        for x,y in v.items():
            soma+=y
        print(k,soma)
    return ""
"""

def entropy_calc(letprob):
    print(letprob)
    print(alfabeto())
    for k,v in letprob.items():
        entropy=0
        for x,y in v.items():
            entropy+=y*math.log(y,2)
        print("Combinação: "+k+"    Entropia: "+str(-entropy))
    return ""
# depois mudem para uma diretoria em linux
lerFicheiro("texto.txt")
print("1ª linha - combinações possíveis\n2ª linha combinações + prob de ocorrências de cada letra a seguir à comb.\n3ª linha alfabeto\n")
print(entropy_calc(letter_probability(3)))

