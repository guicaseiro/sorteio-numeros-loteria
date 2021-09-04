"""
Script para realizar o sorteio de números para loteria

Apenas gerando números aleatórios considerando que não pode haver repetição deles

By. GFC
"""

#  Importando a biblioteca
from random import randint

#  Definindo que 'lista' e 'jogos' são lists dentro do script
lista = list()
jogos = list()

#  Perguntando ao usuário informações básicas para realizar o sorteio, podendo ser utilizando para inúmeras loterias
pergunta1 = int(input('Qual o MENOR número que pode ser sorteado? '))
pergunta2 = int(input('Qual o MAIOR número que pode ser sorteado? '))
pergunta3 = int(input('Quantos números deverão ser selecionados? '))
pergunta4 = int(input('Quantos jogos você quer vizualizar? '))
total = 1

#  Iniciando o scrpit >> tentei manter o máximo em portugês para faciliar como esta estruturado
while total <= pergunta4:
    cont = 0
    while True:
        num = randint(pergunta1, pergunta2)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= pergunta3:
            break
    soma = sum(lista)
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')



