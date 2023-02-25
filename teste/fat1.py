import json

# Lendo o arquivo JSON com os dado
with open('dados.json', 'r') as fat:
    dados = json.load(fat)

# Cria uma lista com apenas os valores de faturamento diário
faturamento_diario = [dado['valor'] for dado in dados]

# Calcula o menor e maior valor de faturamento diário
menor_valor = min(faturamento_diario)
maior_valor = max(faturamento_diario)

# Calcula a média de faturamento diário, ignorando dias sem faturamento
media = sum([valor for valor in faturamento_diario if valor > 0]) / len([valor for valor in faturamento_diario if valor > 0])

# Calcula o número de dias em que o valor de faturamento diário foi superior à média mensal
dias_acima_media = len([valor for valor in faturamento_diario if valor > media])

# Imprime os resultados
print(f"O menor valor de faturamento ocorrido em um dia do mês: R$ {menor_valor:.2f}")
print(f"O maior valor de faturamento ocorrido em um dia do mês: R$ {maior_valor:.2f}")
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {dias_acima_media}")







