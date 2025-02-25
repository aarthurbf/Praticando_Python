hora = int(input("Digite que horas são agora: "))

if hora > 18 or hora < 8:
    print("Acesso negado")
else:
    print("Acesso liberado")
    