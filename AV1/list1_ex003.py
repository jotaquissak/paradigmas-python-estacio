#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#   a. salário bruto.
#   b. quanto pagou ao INSS.
#   c. quanto pagou ao sindicato.
#   d. o salário líquido.
#   e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
#   Obs.: Salário Bruto - Descontos = Salário Líquido.

while True:
    valorPorHora = float(input("Digite quanto você ganha por hora: "))
    if (valorPorHora <= 0):
        print(f"Valor {valorPorHora:.2f} inválido")
        break
    horasPorDia = float(input("Digite quantas horas você trabalha por dia: "))
    if (horasPorDia <= 0 and horasPorDia > 23):
        print(f"Horas {horasPorDia} inválida")
        break
    diasPorMes = int(input("Digite quantos dia você trabalha por mês: "))
    if (diasPorMes <= 0 and diasPorMes > 30):
        print(f"Horas {diasPorMes} inválida")
        break
    salarioBruto = valorPorHora * horasPorDia * diasPorMes
    descontoIR = (salarioBruto * 11) / 100
    descontoINSS = (salarioBruto * 8) / 100
    descontoSindical = (salarioBruto * 5) / 100
    descontos = descontoINSS + descontoIR + descontoSindical
    salarioLiquido = salarioBruto - descontos
    print(f"+ Salário Bruto : R${salarioBruto:.2f}\n- IR (11%) : R${descontoIR:.2f}\n- INSS (8%) : R${descontoINSS:.2f}\n- Sindicato (5%) : R${descontoSindical:.2f}\n= Salário Liquido : R${salarioLiquido:.2f}")
    break