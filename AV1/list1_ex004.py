#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

while True:
    metroQuadrado = float(input("Quantos m² deseja pintar? "))
    if(metroQuadrado <= 0):
        print(f"A medidade de {metroQuadrado}² não é válida.")
        break
    litro = (metroQuadrado / 3)
    if(metroQuadrado%3 != 0):
        litro += 1
    lata = litro / 18
    if(litro%18 != 0):
        lata += 1
    lataPreco = int(lata) * 80
    if(lata > 1):
        print(f"Você irá precisar de {int(lata)} latas, com o valor total de R${lataPreco:.2f}")
    elif(lata == 1):
        print(f"Você irá precisar de {int(lata)} lata, com o valor total de R${lataPreco:.2f}")