# 5. Faça um Programa que leia uma estrutura A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos desta estrutura.

numeros = []

x = 1
while x <= 10:
    numeroRecebido = int(input(f"Digite o {x}° número: "))
    numeros.append(numeroRecebido)
    x+=1

tamanho = len(numeros)
z=soma=0
while z < tamanho:
    quadrado = numeros[z] * numeros[z]
    soma = soma + quadrado
    z+=1

print(soma)