# Crie um script Python que leia o dia, mes e ano de nascimento de uma pessoa
# e mostre uma mensagem com a data formatada.

dia = int(input('Digite o dia do seu nascimento: '))
mes = int(input('Digite o mês do seu nascimento: '))
ano = int(input('Digite o ano do seu nascimento: '))

print('A data completa é {} / {} / {}'.format(dia, mes, ano))