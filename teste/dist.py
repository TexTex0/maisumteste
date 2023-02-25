faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = sum(faturamento.values())

for estado, valor in faturamento.items():
    percentual = valor / total * 100
    print(f'{estado}: {percentual:.2f}%')


#Explicando o código:

#Primeiro, defini um dicionário chamado faturamento com os valores de faturamento mensal de cada estado.
#Em seguida, calculei o valor mensal total da distribuidora somando os valores do dicionário usando a função sum.
#Depois, usei um loop for para percorrer o dicionário e calcular o percentual de representação
# de cada estado dentro do valor total. Esse cálculo é feito dividindo o valor do estado pelo valor total
# e multiplicando por 100 para obter a porcentagem.
#Por fim, é impresso o resultado usando a função print. O formato da string de saída usa f-strings
# para substituir os valores de estado e percentual na mensagem de texto.
#A saída do programa com os dados fornecidos indicará algo como:
#o estado de São Paulo representa o maior faturamento da distribuidora,
# seguido pelo Rio de Janeiro, Minas Gerais,
# Espírito Santo  e outros estados.