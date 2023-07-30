# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

tipo_primitivo = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(tipo_primitivo))

# Mais informações
print('Tem espaço?', tipo_primitivo.isspace())
print('É um número?', tipo_primitivo.isnumeric())
print('É um alfabético?', tipo_primitivo.isalpha())
print('É um alfanumérico?', tipo_primitivo.isalnum())
print('É maiúscula?', tipo_primitivo.isupper())
print('É minúscula?', tipo_primitivo.islower())
print('Está em capitalizada?', tipo_primitivo.istitle())