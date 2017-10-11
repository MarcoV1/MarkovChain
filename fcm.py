import itertools

def lerFicheiro(ficheiro):
    with open(ficheiro) as f:
        texto = f.read()
    return texto

def statistical_info(ficheiro, order):

    texto = lerFicheiro(ficheiro).upper()
    dados = [i for i in texto if i.isalpha() or i == " "]
    alfabeto = list(set(dados))
    print(alfabeto)
    combinations = list(itertools.product(alfabeto, repeat = order))
    combinations_in_text = []
    for i in combinations:
        combinations_in_text.append(''.join(i))
    print(len(combinations_in_text))
    cmb = []
    for c in combinations_in_text:
        if(c in texto):
            cmb.append(c)

    print(len(cmb))









# depois mudem para uma diretoria em linux
statistical_info("texto.txt", 6)

