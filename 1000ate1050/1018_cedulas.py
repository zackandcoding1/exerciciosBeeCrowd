'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
'''

n = int(input())
valor = n

cedula100 = 0
cedula50 = 0
cedula20 = 0
cedula10 = 0
cedula5 = 0
cedula2 = 0
cedula1 = 0

while(n > 0):
  if(n >= 100):
    cedula100+= 1
    n-= 100
  elif(n >= 50):
    cedula50+= 1
    n-= 50
  elif(n >= 20):
    cedula20+= 1
    n-= 20
  elif(n >= 10):
    cedula10+= 1
    n-= 10
  elif(n >= 5):
    cedula5+= 1
    n-= 5
  elif(n >= 2):
    cedula2+= 1
    n-= 2
  elif(n == 1):
    cedula1+= 1
    n-= 1
    
print(valor)
print('%i nota(s) de R$ 100,00' % cedula100)
print('%i nota(s) de R$ 50,00' % cedula50)
print('%i nota(s) de R$ 20,00' % cedula20)
print('%i nota(s) de R$ 10,00' % cedula10)
print('%i nota(s) de R$ 5,00' % cedula5)
print('%i nota(s) de R$ 2,00' % cedula2)
print('%i nota(s) de R$ 1,00' % cedula1)