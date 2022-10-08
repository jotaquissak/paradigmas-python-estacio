#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas

while True:
    peso = float(input("Peso em quilos do total de peixes pescados: "))
    if(peso <= 0):
        print(f"Valor de {peso}Kg é inválido.")
        break
    if(peso > 50):
        multa = (peso - 50) * 4
        print(f"Será necessário pagar multa.\nO valor da multa a pagar é de R${multa:.2f}.")
        break
    elif(peso < 50):
        print(f"Não será necessário pagar multa.")
        break