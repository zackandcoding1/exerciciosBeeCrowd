'''
Com base na tabela (https://resources.beecrowd.com.br/gallery/images/problems/UOJ_1038_pt.png), escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

'''

codItem, qtdItem = [int(s) for s in input().split()]

if(codItem == 1):
  valorTotal = qtdItem * 4.00
elif(codItem == 2):
  valorTotal = qtdItem * 4.50
elif(codItem == 3):
  valorTotal = qtdItem * 5.00
elif(codItem == 4):
  valorTotal = qtdItem * 2.00
elif(codItem == 5):
  valorTotal = qtdItem * 1.50

print('Total: R$ %.2f' % valorTotal)