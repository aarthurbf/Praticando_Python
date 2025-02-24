peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso/(altura**2)

if imc <= 18.5:
    print("Você está a baixo do peso")
elif imc <= 25:
    print("Você está no peso normal")
else:
    print("Você está a cima do peso")
