from fcm import *
import numpy as np
import random

generate_size = int(input("Número de caratéres do texto a ser gerado: "))  # tamanho do texto a ser gerado
generate_file = "generated_text.txt"  # ficheiro onde o texto vai ser gerado
order = int(input("Ordem: "))  # valor da ordem
alpha = float(input("Valor de alpha: "))   # valor de alpha
ficheiro = input("Ficheiro de texto a ser computado ([language](em inglês)_guess.txt): ")
texto = read_file("guess_texts\\"+ficheiro)
cnl = combination_next_letter(order,texto)
lp = letter_probability(cnl,alpha,texto)
print("Para o texto gerado verifique o ficheiro: generated_text.txt !")
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


def generate(size,lp,order,texto):
    al = alfabeto(texto)
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


print(generate(generate_size,lp,order,texto))


