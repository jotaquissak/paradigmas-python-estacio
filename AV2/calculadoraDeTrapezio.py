def calculaArea(maior, menor, altura):
    return ((maior + menor) * altura)/2

altura = float(input("Digite a altura do trapezio: "))
baseMaior = float(input("Digite o tamanho da base maior: "))
baseMenor = float(input("Digite o tamanho da base menor: "))

resposta = calculaArea(baseMaior, baseMenor, altura)
print(f"A área do trapézio é de {resposta}")