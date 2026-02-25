#----------------Exercício – Sistema de produto completo----------------#

#----------------(Lista + Tupla + Dicionário)----------------#

produtos_lista = []
nomes_apenas = []

for i in range(3):
    nome = input(f"\nDigite o nome do {i+1}º produto: ")
    preco = float(input(f"Digite o preço de {nome}: "))
    quantidade = int(input(f"Digite a quantidade de {nome}: "))

    info_fixa = (nome, preco)
    estoque = {"quantidade": quantidade}

    produtos_lista.append(info_fixa)
    produtos_lista.append(estoque)
    nomes_apenas.append(nome)

print("\n--- INFORMAÇÕES CADASTRADAS ---")
for i in range(0, len(produtos_lista), 2):
    p = produtos_lista[i]
    q = produtos_lista[i+1]
    print(f"Produto: {p[0]} | Preço: R$ {p[1]:.2f} | Estoque: {q['quantidade']}")

print("\n--- Nome e preço em Tupla, quantidade em Dicionário: ---")
for item in produtos_lista:
    print(item)
    # Se o item for um dicionário, pula uma linha para separar do próximo bloco
    if type(item) == dict:
        print()

print("--- Todos os produtos em uma lista: ---")
print(nomes_apenas)