altura = float(input("Digite sua altura em metros (ex: 1.75): "))

genero = input("Digite seu gênero (homem ou mulher): ").lower()

if genero == "homem":
    peso_ideal = (72.7 * altura) - 58
elif genero == "mulher":
    peso_ideal = (62.1 * altura) - 44.7
else:
    print("Gênero não reconhecido. Por favor, digite 'homem' ou 'mulher'.")

if genero in ["homem", "mulher"]:
    print(f"Seu peso ideal é aproximadamente {peso_ideal:.2f} kg.")
