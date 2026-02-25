#----------------Parte 1 – Listas (Sistema de Mercado)----------------#

#----------------Exercício – Sistema de estoque do mercado----------------#

produtos = []
estoque = []

for i in range(4):
    nome = input(f"\nDigite o nome do produto {i+1}: ")
    quantidade = int(input(f"Digite a quantidade de {nome}: "))
    produtos.append(nome)
    estoque.append(quantidade)

print("\n--- RELATÓRIO DE ESTOQUE ---")
for i in range(len(produtos)):
    print(f"Produto: {produtos[i]} | Quantidade: {estoque[i]}")

print(f"\nExiste {len(produtos)} tipos de produtos no estoque, totalizando {sum(estoque)} itens no estoque.")