from fcm import *
import numpy as np
import random
generate_size = 1000 #tamanho do texto a ser gerado
generate_file = "generated_text.txt" #ficheiro onde o texto vai ser gerado
#para alterar as outras variáveis globais (order,etc...) altere no fcm.py
# --------------------- GENERATE TEXT ----------------------------------------

def write_initial():
    global order
    while True:
        txt_input = input("Insira a combinação/frase inicial (com coerência se possível): \n").upper()
        if(len(txt_input)<order):
            print("Ordem demasiado grande para texto tão pequeno!\n")
            continue
        else:
            break
    return txt_input

def generate(size):
    global lp
    global order
    al = alfabeto()
    initial_text = write_initial()
    filtered_txt = ""
    for i in initial_text:
        if i.isalpha() or i == " ":
            filtered_txt+= i
    while len(filtered_txt)<size:
        last_cmb = filtered_txt[-order:]
        if(last_cmb in list(lp.keys())):
            filtered_txt += ''.join(np.random.choice(list(lp[last_cmb].keys()),1,p=list(lp[last_cmb].values())))
        else:
            print(len(filtered_txt))
            filtered_txt += random.choice(al)
    file = open(generate_file,'w')
    file.write(filtered_txt)
    file.close()
    return "Texto gerado!"


print(generate(generate_size))


