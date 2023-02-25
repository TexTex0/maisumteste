# Exemplo de string
string = "Deus é bom o tempo todo!"

# Converter a string em lista
lista = list(string)

# Definir os índices para troca
A = 0
B = len(lista) - 1

# Inverter os caracteres
while A < B:
    lista[A], lista[B] = lista[B], lista[A]
    A += 1
    B -= 1

# Converter a lista de volta para string
string_invertida = "".join(lista)

# Imprimir a string invertida
print(string_invertida)


#Neste programa, uma string inicial é definida na variável string. Em seguida, essa string é transformada em uma
# lista de caracteres, utilizando a função list(). A variável A é definida como o índice inicial da lista (0) e a
# variável B é definida como o índice final da lista ( len(lista) - 1).

#O loop while é usado para trocar os caracteres das posições A e B da lista. A cada iteração, os valores nessas posições
# são trocados e os índices são atualizados, até que A seja maior ou igual a B.

#Por fim, a lista invertida é convertida de volta para uma string, utilizando o método join(), e cada string invertida
# é impressa na tela.