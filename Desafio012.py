# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

produto = int(float(input("Digite o valor do produto: ")))
preco_novo = (produto - (produto * 0.05))

print(f'\nO produto teve desconto! \nDe {produto} ficou {preco_novo}')