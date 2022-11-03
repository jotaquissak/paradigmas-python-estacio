def soma_imposto(custo, taxa_imposto):
    return ((custo*taxa_imposto)/100)+custo


valorDoProduto = float(input("Digite o valor do produto: "))
valorPorcentagemImposto = float(input("Digite o valor (em porcentagem) do imposto sobre vendas: "))

valorFinalDoProduto = soma_imposto(valorDoProduto, valorPorcentagemImposto)

print(f"O valor final do produto é de R${valorFinalDoProduto:.2f}")