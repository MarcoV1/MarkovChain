from fcm import *
import numpy as np
import random

generate_size = 300  # tamanho do texto a ser gerado
generate_file = "generated_text.txt"  # ficheiro onde o texto vai ser gerado
# para alterar as outras variáveis globais (order,etc...) altere no fcm.py
# --------------------- GENERATE TEXT ----------------------------------------


def write_initial():
    global order
    while True:
        txt_input = input("Insira a combinação/frase inicial (com coerência se possível): \n").upper()
        if len(txt_input) < order:
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
            filtered_txt += i
    while len(filtered_txt) < size:
        last_cmb = filtered_txt[-order:]
        if last_cmb in list(lp.keys()):
            normalized_list = np.array(list(lp[last_cmb].values()))
            normalized_list /= normalized_list.sum()
            #a lista tem que ser normalizada qnd a soma das probabilidades da por exemplo
            #1.00000000234 isto pode acontecer devido a alphas elevados, ex: alpha = 0.9
            filtered_txt += ''.join(np.random.choice(list(lp[last_cmb].keys()), 1, p=normalized_list))
        else:
            filtered_txt += random.choice(al)
    file = open(generate_file, 'w')
    file.write(filtered_txt)
    file.close()
    return "Texto gerado!"


print(generate(generate_size))


