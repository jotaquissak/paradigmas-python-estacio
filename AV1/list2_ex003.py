# 3. Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 

numero = float(input("Digite o número: "))
if(numero%2 == 0 or numero%3 == 0):
    print("Número inteiro")
elif(numero%2 != 0 or numero%3 != 0):
    print(("Número decimal"))
else:
    print(f"{numero} inválido")