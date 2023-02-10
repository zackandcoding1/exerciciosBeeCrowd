'''
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
'''

a, b, c = [int(s) for s in input().split()]

if(a < b and a < c):
  print(a)
  if(b < c):
    print(b)
    print(c)
  else:
    print(c)
    print(b)
elif(b < a and b < c):
  print(b)
  if(a < c):
    print(a)
    print(c)
  else:
    print(c)
    print(a)
elif(c < a and c < b):
  print(c)
  if(a < b):
    print(a)
    print(b)
  else:
    print(b)
    print(a)
print()
print(a)
print(b)
print(c)