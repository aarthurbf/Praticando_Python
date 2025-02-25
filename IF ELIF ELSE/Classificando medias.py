nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))
nota3 = float(input("Digite sua nota: "))

media = (nota1 + nota2 + nota3) / 3 

if media > 6:
    print(f"Você passou de ano com a seguinte nota {media} ")
else:
    print(f"Você reprovou com a seguinte nota {media}")
