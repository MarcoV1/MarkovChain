Para mudar certos parâmetros, como a ordem, o ficheiro, ou o alfa, pode ser alterado
no fim do ficheiro "fcm.py".
Para mudar o número de caracteres a ser gerado, é preciso alterar a variavel "generate_size" que se encontra no ficheiro generator.py

Caso esteja em Linux, é necessário ter o numpy instalado.
Se não tiver, só é preciso inserir no terminal:

$ sudo pip install numpy scipy


O ficheiro "texto.txt" contém mais de 850 mil caracteres.
Ao executar o generator.py tem que colocar um input inicial e o texto gerado é colocado no ficheiro "generated_text.txt".
Se executar o fcm.py obtem a entropia calculada através do modelo estatístico obtido do texto.
