# Enunciado:

"""
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.

Exemplos de Entrada	           |            Exemplos de Saída

3.0 4.0 5.2                    |            TRIANGULO: 7.800
.                              |            CIRCULO: 84.949
.                              |            TRAPEZIO: 18.200
.                              |            QUADRADO: 16.000
.                              |            RETANGULO: 12.000

12.7 10.4 15.2                 |            TRIANGULO: 96.520
.                              |            CIRCULO: 725.833
.                              |            TRAPEZIO: 175.560
.                              |            QUADRADO: 108.160
.                              |            RETANGULO: 132.080
"""
# Declaração de variáveis
a,b,c = input("Informe os valores de A,B e C: ").split()

# Processamento
triangulo = ((float(a)) * (float(c))) / 2
circulo = 3.14159 * ((float(c))**2)
trapezio = (((float(a)) + (float(b))) * (float(c))) / 2
quadrado = (float(b))**2
retangulo = (float(a)) * (float(b))

# Saída
print(f"TRIANGULO: {triangulo:.3f}"
      f"\nCIRCULO: {circulo:.3f}"
      f"\nTRAPEZIO: {trapezio:.3f}"
      f"\nQUADRADO: {quadrado:.3f}"
      f"\nRETANGULO: {retangulo:.3f}")
