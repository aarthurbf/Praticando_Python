maça = int(input("Digite a quantidade de maçãs vendidas: "))
banana = int(input("Digite a quantidade de bananas vendidas: "))
print(f"A quantidade de maças vendidas foi {maça}")
print(f"A quantidade de bananas vendidas foi {banana}")

if maça > banana :
    print("A maça foi mais vendida")
elif maça == banana :
    print("AS frutas venderam igualmente")
else:
    print("A banana foi a mais vendida")