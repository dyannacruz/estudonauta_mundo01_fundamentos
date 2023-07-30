# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = int(float(input("Digite o velor do salário: ")))
aumento = (salario + (salario * 0.15))

print(f'\nO valor do salário + 15% de aumento = {aumento}')