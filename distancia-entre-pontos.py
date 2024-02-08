# Enunciado:
"""
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia = raiz((x2-x1)²+(y2-y1)²)

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.

Exemplo de Entrada      |     	Exemplo de Saída

1.0 7.0                 |       4.4721
5.0 9.0                 |

-2.5 0.4                |       16.1484
12.1 7.3                |

2.5 -0.4                |       16.4575
-12.2 7.0               |
"""

# Declaração de Variáveis
x1,y1 = input("Informe os valores de x1 e y1: ").split()
x2,y2 = input("Informe os valores de x2 e y2: ").split()
x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

# Processamento
distancia = ((x2-x1)**2+(y2-y1)**2)**0.5
# Saída
print(f"A distância entre os pontos é: {distancia:.4f}")
