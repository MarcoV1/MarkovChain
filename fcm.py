def main(ficheiro):

    dados = lerFicheiro(ficheiro)

    # criar uma lista de todas as letras
    dados = [i for i in dados if i != '']

    # passar tudo para maiusculo, mais espaços
    dados = [i.upper() for i in dados if i.isalpha() or i == " " ]

    # com numeros / remover se nao for preciso
    #dados = [i.upper() for i in dados ]

    # criar um dicionario com todas as letras
    chain = {i:[] for i in dados}

    # adicionar uma letra associada a uma letra, se essa mesma a seguir
    for j in range(len(dados) - 1):
        chain[dados[j]].append(dados[j + 1])

    temp = zip(range(len(chain)), list(chain))
    n_chain = dict(temp)
    #print(chain)
    # é necessário estimar a probabilidade de cada letra seguir uma letra já escolhida

    # escolher uma letra ao calhas do dicionario
    #letra = random.choice(n_chain.keys())


    # criar uma frase no fim com um numero minimo e maximo de letras
    #frase = random.randint(n, m)

    # retornar frase no final
    return None;

def lerFicheiro(ficheiro):
    with open(ficheiro) as f:
        texto = f.read()
    return texto

def calcularProbabilidade():
    next();


# depois mudem para uma diretoria em linux
print(main("C:/Users/Marco/Desktop/TAI/Lab1/texto.txt"))