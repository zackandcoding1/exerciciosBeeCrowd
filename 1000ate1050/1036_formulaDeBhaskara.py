'''
Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

Entrada
Leia três valores de ponto flutuante (double) A, B e C.

Saída
Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.
'''

A, B, C = [float(s) for s in input().split()]

delta = pow(B, 2) - (4*A*C)

if delta <= 0 or A == 0:
  print('Impossivel calcular')
else:
  R1 = (-B + pow(delta, 0.5)) / (2*A)
  R2 = (-B - pow(delta, 0.5)) / (2*A)
  
  print('R1 = %.5f' % R1)
  print('R2 = %.5f' % R2)