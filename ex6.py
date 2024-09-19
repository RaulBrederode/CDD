p = float(input("(KG) Qual o seu peso? "))
a = float(input("(M) Qual a sua altura? "))
imc = p / (a ** 2)
print(f"O IMC dessa pessoa é de {imc: .2f}")
if imc < 18.5:
    print("Você está abaixo do peso")
elif imc >= 18.6 and imc < 25:
    print("Você está no peso ideal PARABÉNS!")
elif imc >= 25 and imc < 30:
    print("Você está levemente acima do peso")
elif imc >= 30 and imc < 35:
    print("Você está em obesidade grau I")
elif imc >= 35 and imc < 40:
    print("Você está em obesidade grau II (Severa)")
elif imc >= 40:
    print("Você está em obesidade grau III (Mórbida")
