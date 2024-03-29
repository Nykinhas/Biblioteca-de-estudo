# Enunciado
"""
Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).

Entrada
O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total percorrida (em Km), e um valor real Y representando o total de combustível gasto, com um dígito após o ponto decimal.

Saída
Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem "km/l".

Exemplo de Entrada	        |            Exemplo de Saída

500                         |            14.286 km/l
35.0                        |

2254                        |            18.119 km/l
124.4                       |

4554                        |            9.802 km/l
464.6                       |
"""
# Declaração de Variáveis
km = int(input(f"Digite a distância percorrida (em Km): "))
lts = float(input(f"Digite o total de combustível gasto (em litros): "))
# Processamento
consumo = km / lts
# Saída
print(f"{consumo:.3f} km/l")
