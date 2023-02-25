#Segue abaixo um exemplo de programa em Python que calcula uma sequência de Fibonacci e
# verifica se um número fornecido pertence à sequência

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Digite um número: "))

pertence = False

for i in range(num+1):
    if fibonacci(i) == num:
        pertence = True
        break

if pertence:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")


#Explicação do programa:

#A função fibonacci(n)calcula o n-ésimo número da sequência de Fibonacci usando recursão.
# Se nfor igual a 0 ou 1, a função retorna o valor correspondente. Caso contrário, a função retorna a soma dos dois
# valores anteriores da sequência.

#O programa diz um número fornecido pelo usuário.

#O programa cria uma variável pertenceque é inicialmente falsa.

#O programa itera sobre os valores de 0 até num. Para cada valor i, o programa calcula o i-terceiro número
# da sequência de Fibonacci utilizando a função fibonacci(n).

#Se o valor calculado for igual a num, o programa atualiza a variável pertencepara Truee interromper o laço de repetição.

#Ao final do laço, o programa verifica o valor da variável pertencee exibe uma mensagem informando se o número informado
# pertence ou não à sequência de Fibonacci.

