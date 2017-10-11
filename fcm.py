import itertools
texto = ""
alfa = 0.000001
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

    for a in ocorr:
        for x in alfabeto():
            if x not in ocorr[a]:
                global alfa
                ocorr[a][x] = 0

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
    lac = letter_after_comb(order)
    cmb = combinations_in_text(order)
    print(lac)
    for key,value in lac.items():
        counter = 0
        for x,v in value.items():
            if(counter>0):
                letter_prob[key][x] = v/calc_ocorr(value)
            else:
                letter_prob[key] = { x : v/calc_ocorr(value) }
                counter += 1



    return letter_prob



# depois mudem para uma diretoria em linux
lerFicheiro("texto.txt")
print(letter_probability(3))
