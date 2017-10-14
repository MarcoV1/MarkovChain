
import math
import time

texto = ""

# STATISTICAL INFORMATION


def lerFicheiro(ficheiro):
    global texto
    with open(ficheiro) as f:
        texto = f.read().upper()
        texto1 = ""
        for i in texto:
            if i.isalpha() or i == " ":
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
    text = lerFicheiro("textocurto.txt")

    ocorr = dict()
    alfab = alfabeto()

    for i in range(0, len(text) - order):
        print("Combinação: {}, Letra seguinte: {}".format(text[i : order + i], text[order + i]))
        cmb = text[i : order + i]
        next_letter = text[order + i]
        if cmb in ocorr:
            if next_letter in ocorr[cmb]:
                ocorr[cmb][next_letter] += 1
            else:
                ocorr[cmb][next_letter] = 1
        else:
            ocorr[cmb] = {next_letter : 1}
    for a in ocorr:
        for x in alfab:
            if x not in ocorr[a]:
                ocorr[a][x] = alpha
    return ocorr


'''
POUCO EFICIENTE
def letter_after_comb(order):
    ocorr = {}
    alfab = alfabeto()
    global texto
    cmb = combinations_in_text(order)
    s1 = time.time()
    for c in cmb:
        s = texto.split(c)
        for i in range(1, len(s)):
            if s[i] != "":
                letra = s[i][0]
                if c in ocorr:
                    if letra in ocorr[c]:
                        ocorr[c][letra] += 1
                    else:
                        ocorr[c][letra] = 1
                else:
                    ocorr[c] = {letra : 1}
            elif(s[i] == "" and i < len(s)):
                letra = c[0]
                if c in ocorr:
                    if letra in ocorr[c]:
                        ocorr[c][letra] += 1
                    else:
                        ocorr[c][letra] = 1
                else:
                    ocorr[c] = {letra : 1}
    print("For c in cmb: {}".format(time.time() - s1))
    global alpha
    for a in ocorr:
        for x in alfab:
            if x not in ocorr[a]:
                ocorr[a][x] = alpha
    return ocorr
'''


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
    global alpha

    lac = combination_next_letter(order)
    #cmb = combinations_in_text(order)

    for key,value in lac.items():
        counter = 0
        for x,v in value.items():
            if(counter>0):
                if(v==alpha):
                    letter_prob[key][x] = v / (calc_ocorr(value) + alpha)
                else:
                    letter_prob[key][x] = v / calc_ocorr(value)
            else:
                if(v==alpha):
                    letter_prob[key] = {x: v / (calc_ocorr(value) + alpha)}
                else:
                    letter_prob[key] = {x: v / calc_ocorr(value)}
                counter += 1
    return letter_prob


'''
def teste(letprob):
    print(letprob)
    soma = 0
    for k,v in letprob.items():
        soma = 0
        for x,y in v.items():
            soma+=y
        print(k,soma)
    return ""
'''


def entropy_calc(letprob):
    print(letprob)
    print(alfabeto())
    for k,v in letprob.items():
        entropy=0
        for x,y in v.items():
            entropy+=y*math.log(y,2)
        print("Combinação: "+k+"    Entropia: "+str(-entropy))
    return ""

order = 9 #para alterar a ordem
ficheiro = "texto.txt" #path do ficheiro
alpha = 0.00000000000000000001 #valor de alpha

print("1ª linha - combinações possíveis\n2ª linha combinações + prob de ocorrências de cada letra a seguir à comb.\n3ª linha alfabeto\n")

#lerFicheiro(ficheiro)

s2 = time.time()
lp = letter_probability(order)
# print(teste(lp))

entropy_calc(lp)
print("Tempo de execução total: {} segundos".format(time.time() - s2))

combination_next_letter(order)
