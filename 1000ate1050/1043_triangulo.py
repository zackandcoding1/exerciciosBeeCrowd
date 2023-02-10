'''
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:

Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem

Area = XX.X

Entrada
A entrada contém três valores reais.

Saída
O resultado deve ser apresentado com uma casa decimal.
'''

a, b, c = [float(s) for s in input().split()]

if(a+b > c and b+c > a and a+c > b):
  perimetroTriangulo = a+b+c
  print('Perimetro = %.1f' % perimetroTriangulo)
else:
  areaTrapezio = (a+b)*c/2
  print('Area = %.1f' % areaTrapezio)