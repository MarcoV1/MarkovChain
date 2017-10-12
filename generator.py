from fcm import *
import numpy as np
import random
generate_size = 300
generate_file = "generated_text.txt"
#para alterar as outras variáveis globais altere no fcm.py
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
    initial_text = write_initial()
    filtered_txt = ""
    for i in initial_text:
        if i.isalpha() or i == " ":
            filtered_txt+= i
    print("saiu")
    while len(filtered_txt)<size:
        last_cmb = filtered_txt[-order:]
        if(last_cmb in list(lp.keys())):
            filtered_txt += ''.join(np.random.choice(list(lp[last_cmb].keys()),1,p=list(lp[last_cmb].values())))
        else:
            filtered_txt += random.choice(alfabeto())

    file = open(generate_file,'w')
    file.write(filtered_txt)
    file.close()
    return "Texto gerado!"



generate(generate_size)


