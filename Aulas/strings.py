# Para pegar um caractere específico em uma string, usamos colchetes [] e o índice do caractere desejado.

exemplo = "Python"

print(exemplo[0]) # Saída: P

# Para pegar um pedaço de texto, ou subtring, usamos dois pontos : dentro dos colchetes.

exemplo = "Python"

print(exemplo[0:3]) # Saída: Pyt
print(exemplo[2:])  # Saída: thon

# Escrever variáveis dentro de textos, usar o .format

exemplo = "Python"
exemplo2 = "VBA"

print("Hoje, estou a prendendo {}, mas eu já sei {}".format(exemplo, exemplo2))

# Métodos de string

# capitalize -> Coloca a primeira letra da string em maiuscula
# casefold -> deixa todo o texto em letra maiuscula
# count -> quantas vezes um texto aparece dentro de outro
# endswitch -> verifica se o texto termina como um valor específico (o usuário que da esse valor), retornando true or false
# startswitch -> verifica se o texto começa como um valor específico (o usuário que da esse valor), retornando true or false
# fing -> procura um texto dentro de outro texto e trás a posição
# isalnum -> verifica se o texto é composto de números e letras
# isnum -> verifica se o texto é composto de apenas números
# isalpha -> verifica se o texto é composto de apenas letras
# replace -> troca um texto por outro
# split -> separa uma string de acordo com um limitador
# splitlines -> igual o split, mas o delimitador é o enter
# strip -> retira caracteres indesejados, por padrão ele retira espaços em branco no início e no final
# title -> primeira letra de cada palavra na string fica maiuscula
# upper -> todas as letras ficam maiusculas
