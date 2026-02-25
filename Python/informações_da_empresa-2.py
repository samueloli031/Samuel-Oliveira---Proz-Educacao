#----------------Parte 2 – Tuplas (Sistema Bancário e Empresarial)----------------#

#----------------Exercício – Informações fixas da empresa----------------#

empresa_nome = input("Digite o nome da empresa: ")
cnpj = input("Digite o CNPJ: ")
cidade = input("Digite a cidade: ")

empresa = (empresa_nome, cnpj, cidade)

print(f"\nTodas as informações: {empresa}")
print(f"Nome da empresa: {empresa[0]}")
print(f"Cidade: {empresa[2]}")