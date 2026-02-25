#----------------Parte 2 – Tuplas (Sistema Bancário e Empresarial)----------------#

#----------------Exercício – Cadastro de conta bancária----------------#

numero = input("Digite o número da conta: ")
nome = input("Digite o nome do cliente: ")
saldo = float(input("Digite o saldo da conta: "))

conta = (numero, nome, saldo)

print(f"\nTupla completa: {conta}")
print(f"Nome do cliente: {conta[1]}")
print(f"Saldo: R$ {conta[2]:.2f}")