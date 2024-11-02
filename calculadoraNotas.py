try:
    quantidadeNotas = int(input("Quantas notas vai ser necessario para calcular a media: "))
except ValueError:
    print("Valor informado é invalido!")


totalNotas = 0

for i in range(quantidadeNotas):
    try:
        nota = float(input(f"Digite a nota {i + 1}: "))
        totalNotas = totalNotas + nota
    except ValueError:
        print("A nota informada é invalido!")

media = totalNotas / quantidadeNotas

if media >= 7:
    print(f"Parabeeeens!! Voce atingiu a media com nota {media}.")
else:
    print(f"Poxa, que pena :( Voce nao atingiu a media e esta de recuperação. Sua nota final foi {media}.")
