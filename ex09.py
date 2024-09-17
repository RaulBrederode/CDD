lv = float(input("Quantos litros você colocou? "))
usuario = str(input("""G = Gasolina
E = Etanol:
"""))
if usuario == "G" or usuario == "g":
    valor = 5.8 * lv
    print("valor total a ser pago será de R${:.2f}.".format(valor))
elif usuario == "E" or usuario == "e":
    valor2 = 4.9 * lv
    print("Valor total a ser pago será de R${:.2f}.".format(valor2))
else:
    print("Tipo de combustível inválido, insira novamente o combustível.")
    exit()