# Faça um programa que leia a largura e a altura em metros, calcule a sua área e a quantidade de tinta necessária
# para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m^2.

print(70*"-")
print(f'Cálculo da área e a quantidade de tinta necessária para pinta-la')
print(70*"-")

print("Resposta do usuário")
l = int(float(input("\nDigite a largura em metros: ")))
h = int(float(input("\nDigite a altura em metros: ")))
a = (l*h)
tinta_por_litro = 2   # 1l para 2 metros

print(70*"-")
tinta_necessaria = (a / tinta_por_litro)
print(f'A quantidade de tinta para pintar uma área de {a} metros é = {tinta_necessaria} litro(s)')
print(70*"-")