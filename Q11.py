
numero_inteiro1 = int(input("Digite o primeiro número inteiro: "))
numero_inteiro2 = int(input("Digite o segundo número inteiro: "))
numero_real = float(input("Digite um número real: "))


print(f"Você digitou os números inteiros {numero_inteiro1} e {numero_inteiro2}, "
      f"e o número real {numero_real}.")

produto = (2 * numero_inteiro1) * (numero_inteiro2 / 2)
soma = (3 * numero_inteiro1) + numero_real
cubo = numero_real ** 3

print(f"O produto do dobro do primeiro com metade do segundo é: {produto}")
print(f"A soma do triplo do primeiro com o terceiro é: {soma}")
print(f"O terceiro elevado ao cubo é: {cubo}")