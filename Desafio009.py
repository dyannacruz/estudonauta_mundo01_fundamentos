# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input("Digite um número inteiro para saber a sua tabuada: "))
print(52*"-")
print(f'A tabuada do número {num}: ')
print(52*"-")

for i in range (11):
    print("{} x {} = {:2}".format(num,i,num*i))
