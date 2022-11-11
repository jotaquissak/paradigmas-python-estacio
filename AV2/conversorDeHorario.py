def conversao(hora, minuto):
    am_pm = "A.M."
    if hora == 0 or hora == 00:
        hora = hora + 12
        am_pm = "P.M."
    if hora > 12:
        hora = hora - 12
        am_pm = "P.M."
    hora_formatada = hora
    minuto_formatado = minuto
    if hora < 10:
        hora_formatada = f"0{hora}"
    if minuto < 10:
        minuto_formatado = f"0{minuto}"
    formatado = f"{hora_formatada}:{minuto_formatado}"
    saida(formatado, am_pm)

def saida(formatado, am_pm):
    print(f"{formatado} {am_pm}")

while True:
    horas = int(input("Digite a hora: "))
    if horas > 24:
            print("\nora inválida.")
    elif horas < 0:
        print("\nEncerrando...")
        break
    else:
        minutos = int(input("Digite os minutos: "))
        if minutos > 60 or minutos < 0:
            print("\nMinuto inválido.")
        else:
            conversao(horas, minutos)
    print("\nPara sair do programa digite um horário negativo.\n")
