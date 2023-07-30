# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

print(55*"-")
print(f'Valor disponível e conversão em dólares')
print(55*"-")

carteira = int(float(input("Digite o valor: ")))
cotacao = 4.925
iof = 0.01
dolares = ((carteira * cotacao) + ((carteira * cotacao)*iof))

print(f'Comprando R$ {carteira}, o valor em dólares + IOF = {dolares}')
print(55*"-")



# 1 USD = R$ 4,925. IOF (1.1%) = R$ 2,71. Valores para São Paulo/SP, com IOF incluso.