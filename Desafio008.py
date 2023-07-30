# Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milimitros.

metro = int(float(input("Digite o valor em metros: ")))
centimetros = (metro*100)
milimetros = (metro*1000)

print(f'O valor em metros é {metro}\n O valor em centímetros é {centimetros} \n O valor em milímetros é {milimetros}')