'''
Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).

Se o ponto estiver na origem, escreva a mensagem “Origem”.

Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.

Entrada
A entrada contem as coordenadas de um ponto.

Saída
A saída deve apresentar o quadrante em que o ponto se encontra.
'''

x, y = [float(s) for s in input().split()]

if(x > 0 and y > 0):
  print('Q1')
if(x < 0 and y > 0):
  print('Q2')
if(x < 0 and y < 0):
  print('Q3')
if(x > 0 and y < 0):
  print('Q4')
if(x != 0 and y == 0):
  print('Eixo X')
if(y != 0 and x == 0):
  print('Eixo Y')
if(x == 0 and y == 0):
  print('Origem')