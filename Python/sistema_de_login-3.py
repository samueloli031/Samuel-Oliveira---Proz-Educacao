#----------------Parte 3 – Dicionários (Sistema de Cadastro)----------------#

#----------------Exercício – Sistema de login----------------#

usuario = {}

usuario["nome"] = input("Digite o nome de usuário: ")
usuario["senha"] = input("Digite a senha: ")

print("\n--- Dados Cadastrados ---")
print(f"Usuário: {usuario['nome']}")
print(f"Senha: {usuario['senha']}")

print("\nDicionário completo:", usuario)