atividadeA = int(input("Digite a quantidade de dias para a atividade A: "))
atividadeB = int(input("Digite a quantidade de dias para a atividade B: "))
atividadeC = int(input("Digite a quantidade de dias para a atividade C: "))

if atividadeA < 0 or atividadeB < 0 or atividadeC < 0:
    print("Número inválido")
else:
    tempoTotal = (atividadeA+atividadeB+atividadeC)
    print(f"Os dias de atividades foram {tempoTotal}")