'''
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia = sqrt((x2 - x1)² + (y2 - y1)²)

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.
'''

x1, y1 = [float(s) for s in input().split()]
x2, y2 = [float(s) for s in input().split()]

potencia = pow((x2 - x1), 2) + pow(y2 - y1, 2)
raiz = potencia ** 0.5
distancia = raiz

print('%.4f' % distancia)
