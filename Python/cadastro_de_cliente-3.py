#----------------Parte 3 – Dicionários (Sistema de Cadastro)----------------#

#----------------Exercício – Cadastro de cliente completo----------------#

cliente = {}

cliente["nome"] = input("Digite o nome do cliente: ")
cliente["idade"] = int(input("Digite a idade: "))
cliente["cidade"] = input("Digite a cidade: ")
cliente["telefone"] = input("Digite o telefone: ")

print("\n--- Informações do Cliente ---")
print(f"Nome: {cliente['nome']}")
print(f"Idade: {cliente['idade']}")
print(f"Cidade: {cliente['cidade']}")
print(f"Telefone: {cliente['telefone']}")

print("\nDicionário completo:", cliente)