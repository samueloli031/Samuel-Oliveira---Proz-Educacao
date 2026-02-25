#----------------Parte 1 – Listas (Sistema de Mercado)----------------#

#----------------Exercício – Sistema completo de carrinho de compras----------------#

produtos = []
precos = []

for i in range(4):
    nome = input(f"\nDigite o nome do {i+1}º produto: ")
    produtos.append(nome)

    preco = float(input(f"Digite o preço de {nome}: "))
    precos.append(preco)
1

total_compra = sum(precos)

print(f"\nLista de produtos: {produtos}")
print(f"Lista de preços: {precos}")

print(f"\nPrimeiro produto: {produtos[0]} - R$ {precos[0]}")
print(f"Último produto: {produtos[-1]} - R$ {precos[-1]}")

print(f"\nVALOR TOTAL DA COMPRA: R$ {total_compra:.2f}")

# Parte nova: Substituição
novo_prod = input("\nDigite um novo produto para substituir o da posição 1: ")
novo_preco = float(input(f"Digite o preço de {novo_prod}: "))

produtos[1] = novo_prod
precos[1] = novo_preco

print("\nLista de produtos atualizada:", produtos)
print("Lista de preços atualizada:", precos)