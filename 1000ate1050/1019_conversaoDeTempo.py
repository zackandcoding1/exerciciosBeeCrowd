'''
Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
'''

n = int(input())

horas = n // 3600
restoSegundos = n % 3600
minutos = restoSegundos // 60
segundos = restoSegundos % 60


print('%i:%i:%i'% (horas, minutos, segundos))