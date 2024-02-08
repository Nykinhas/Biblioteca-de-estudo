# Enunciado:
"""
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:

MaiorAB = (a+b+abs(a-b))/2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

Exemplos de Entrada         |       	Exemplos de Saída
7 14 106                    |         106 eh o maior

217 14 6                    |         217 eh o maior
"""

# Declaração de Variáveis
a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

# Processamento
maiorAB = (a+b+abs(a-b))/2 
"""
A função abs() pode ser usada em diversas situações, como:
Calcular a distância entre dois pontos
Encontrar o valor máximo ou mínimo de uma lista de números
Determinar se um número é positivo ou negativo
"""
maiorABC = (maiorAB+c+abs(maiorAB-c))/2

# Saída
print(f"{int(maiorABC)} eh o maior")
