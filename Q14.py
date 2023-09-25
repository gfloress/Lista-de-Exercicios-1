peso_peixes = float(input("Digite o peso dos peixes em quilos: "))

limite_peso = 50.0  # 50 quilos

if peso_peixes > limite_peso:
    excesso = peso_peixes - limite_peso
    multa = excesso * 4.00
else:
    excesso = 0.0
    multa = 0.0

if excesso > 0:
    print(f"Peso de peixes excedeu o limite em {excesso:.2f} quilos.")
    print(f"Multa a ser paga será de: R$ {multa:.2f}")
else:
    print("Peso de peixes dentro do limite! Nenhuma multa é devida.")
